from heic2png import HEIC2PNG

if __name__ == "__main__":
    heic_img = HEIC2PNG("/Users/shaoshuai.shao/Desktop/IMG_7397.HEIC", quality=90)
    heic_img.save()
