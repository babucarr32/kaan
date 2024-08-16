import sys

from kaan import kaan

if __name__ == "__main__":
    args = sys.argv
    filePath = sys.argv[1]
    kaan(filePath=filePath)