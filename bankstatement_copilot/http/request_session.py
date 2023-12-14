import contextlib
from functools import wraps
import aiohttp


@contextlib.asynccontextmanager
async def getClientSession():
    session = aiohttp.ClientSession("http://8.211.11.142:8000")
    try:
        yield session
    except Exception as e:
        raise e
    finally:
        await session.close()


def provide_request_session(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        arg_session = "session"

        func_params = func.__code__.co_varnames
        session_in_args = arg_session in func_params and func_params.index(
            arg_session
        ) < len(args)
        session_in_kwargs = arg_session in kwargs

        if session_in_kwargs or session_in_args:
            return await func(*args, **kwargs)
        else:
            async with getClientSession() as session:
                kwargs[arg_session] = session
                return await func(*args, **kwargs)

    return wrapper
