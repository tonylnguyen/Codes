import os

def rename_files():
    files = os.listdir(r"/Users/tonynguyen/Desktop/prank")
    print(files)

    os.chdir("/Users/tonynguyen/Desktop/prank")
    digits = list(range(101))

    for pictures in files:
        os.rename(pictures, pictures.strip(str(digits)))

rename_files()
