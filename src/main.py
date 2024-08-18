import sys
import os

from kaan import kaan

if __name__ == "__main__":
    args = sys.argv
    filePath = sys.argv[1]
    if filePath.endswith(".kaan"):
        kaan(filePath=f"{os.getcwd()}/{filePath}")
    else:
        print("Supported file type is .kaan")