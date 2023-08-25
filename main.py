import os
import glob
from datetime import datetime


def rename_images_with_sequence(folder_path, prefix="User-", start_sequence=1):
    image_files = glob.glob(os.path.join(folder_path, "*.png")) + \
                  glob.glob(os.path.join(folder_path, "*.jpg")) + \
                  glob.glob(os.path.join(folder_path, "*.jpeg")) + \
                  glob.glob(os.path.join(folder_path, "*.gif")) + \
                  glob.glob(os.path.join(folder_path, "*.bmp"))

    image_files.sort(key=os.path.getmtime)  # 根據時間進行排序
    for i, file_path in enumerate(image_files):
        extension = os.path.splitext(file_path)[1]
        new_file_name = f"{prefix}{start_sequence + i:04d}{extension}"
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(file_path, new_file_path)


if __name__ == "__main__":
    USER_NAME = f"{os.getenv('USER_NAME', None)}-"
    FOLDER_NAME = os.getenv("FOLDER_NAME", "./")
    if not USER_NAME:
        print("[X]未填寫 USER_NAME 請將 .env 內容進行修改")
    rename_images_with_sequence(folder_path=FOLDER_NAME, prefix=USER_NAME, start_sequence=1)
    print("[V]圖片修改完成")
