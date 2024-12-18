import os
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_dir'])

log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file_info.log')
logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(message)s')

def scan_directory(path):
    path = os.path.abspath(path)
    if not os.path.isdir(path):
        logging.error(f'"{path}" is not a valid directory')
        return

    for root, dirs, files in os.walk(path):
        parent_dir = os.path.basename(root)
        
        for name in dirs + files:
            file_path = os.path.join(root, name)
            is_directory = os.path.isdir(file_path)
            name_without_ext, ext = os.path.splitext(name)
            extension = ext.lstrip('.')
            file_info = FileInfo(name_without_ext, extension, is_directory, parent_dir)
            
            logging.info(f"{file_info}")
            print(file_info)

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    scan_directory(path)
