from os import path
import shutil

"""
This script duplicates an audio file,
naming the copies according to filenames supplied in a text file.
"""

def main():
    # get original audio
    src = path.realpath("noise.mp3")
    # head, tail = path.split(src)

    # get list of names
    with open("filenames.txt", 'r', encoding="utf-8") as filenames_file:
        filenames = filenames_file.readlines()
        filenames = [filename.strip() for filename in filenames]
        print(filenames)

    for filename in filenames:
        shutil.copy(src, "files/" + filename)


if __name__ == "__main__":
    main()
