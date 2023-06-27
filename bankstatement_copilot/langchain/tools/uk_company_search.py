class UkCompanyHouseSearch(object):
    name = "Search UK company info"
    desscription = "Search UK company info"

    def run(self, text: str) -> str:
        text = text.strip()
        if len(text) == 0:
            return
        reply = f"UkCompanyHouseSearch Q:{text}"
        print(reply)
        return reply
