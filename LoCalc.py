import os
from util.logging import *
___CONFIG___ = {
    "file_type" : "py",
    "path" : "."
}


def match_the_files() -> list:
    matches = []
    obj = os.walk(___CONFIG___["path"])
    for root, dirs, files in obj:
        for file in files:
            if file[-2:] == ___CONFIG___["file_type"]: matches.append(os.path.join(root,file))
    for dir in matches:
        log_green("Founded: {}".format(dir))
    
    return matches

def calculate_lines_of_code(path: list[str]) -> int:
    c = 0
    for file in path:
        with open(file=file, mode="r", encoding="utf-8") as fp:
            for line in fp:
                c = c + 1
    
    return c

def main():
    founded = match_the_files()
    totalLOC = calculate_lines_of_code(founded)
    log_green("Total LOC: {}".format(totalLOC))

main()


    