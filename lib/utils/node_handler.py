"""This module is responsible for handling operations on folders/files (nodes) on system"""
import os


def create_file(file_abs_path: str, content: str):
    "Create file"
    create_directory(os.path.dirname(file_abs_path))
    with open(file_abs_path, '') as f_handler:
        f_handler.write(content)


def create_directory(directory: str):
    "Create directory"
    os.makedirs(directory, mode=0o666, exist_ok=True)
