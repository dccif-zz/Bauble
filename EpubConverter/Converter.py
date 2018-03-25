import os
import shutil
import tkinter as tk
import zipfile
from tkinter import filedialog

from hanziconv import HanziConv


def translate(translate_file_path):
    with open(file=translate_file_path, mode="r", encoding="utf-8") as file:
        content = file.read()
    with open(file=translate_file_path, mode="w", encoding="utf-8") as file:
        if content:
            content = HanziConv.toSimplified(content)
            file.write(content)


def get_filename(file_path):
    return ".".join(file_path.split(".")[:-1])


def main(epub_file):
    temp_path = "temp"
    with zipfile.ZipFile(epub_file, 'r') as zip_ref:
        zip_ref.extractall(temp_path)
    for root, dirs, files in os.walk(temp_path, topdown=False):
        for file in files:
            if file.endswith("html") or file.endswith("opf"):
                file_abs_path = os.path.abspath(os.path.join(root, file))
                translate(file_abs_path)

    file_name = get_filename(epub_file)
    archive_file = shutil.make_archive(file_name, 'zip', root_dir=temp_path)
    os.replace(archive_file, HanziConv.toSimplified(file_name) + "(translated).epub")
    shutil.rmtree(temp_path, ignore_errors=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    epub_file_path = filedialog.askopenfilename(**dict(filetypes=[('Epub file', '*.epub'), ('All files', '*.*')]))
    main(epub_file_path)
