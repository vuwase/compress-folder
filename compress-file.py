import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    try:
        folder_name = os.path.basename(folder_path)
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_file_name = f"{folder_name}_{current_date}.{compress_type}"

        if compress_type == "zip":
            with zipfile.ZipFile(compressed_file_name, "w") as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file),
                                   arcname=os.path.relpath(
                                       os.path.join(root, file), folder_path))

        elif compress_type == "tar":
            with tarfile.open(compressed_file_name, "w") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))

        elif compress_type == "tgz":
            with tarfile.open(f"{compressed_file_name}.gz", "w:gz") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))

        print(f"Compression successful: {compressed_file_name}")
    except Exception as e:
        print(f"Compression failed: {e}")

def main():
    folder_path = input("Enter the folder path to compress: ")
    compress_types = ["zip", "tar", "tgz", "rar", "mint"]
    
    print("Available compressed file types:")
    for idx, ctype in enumerate(compress_types, start=1):
        print(f"{idx}. {ctype}")
    
    try:
        choice = int(input("Enter the number corresponding to the desired compressed file type: "))
        if 1 <= choice <= len(compress_types):
            compress_type = compress_types[choice - 1]
            compress_folder(folder_path, compress_type)
        else:
            print("Invalid choice. Please enter a number corresponding to the desired compressed file type.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
