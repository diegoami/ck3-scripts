import os

import sys


dir_mds = os.environ.get("CK_DIR")
person_mds = os.path.join(dir_mds, 'p')

def find_best_dinasty(person_mds, s):
    fathers, mothers = set(), set()
    best_files, most_tabs = [], 100
    for file_name in os.listdir(person_mds):
        if ('.md' in file_name):

            with open(os.path.join(person_mds, file_name), 'r') as fp:
                lines = fp.readlines()
                if (len(lines) < 37):
                    continue
                for line in lines:
                    num_tabs = len(line) - len(line.lstrip())
                    if s in line:
                        if num_tabs > 0:
                            if num_tabs < most_tabs:
                                best_files, most_tabs = [file_name], num_tabs
                            elif num_tabs == most_tabs:
                                best_files.append(file_name)
                            else:
                                break


    for best_file in best_files:
        print(best_file)
        print("\n")
        with open(os.path.join(person_mds, best_file), 'r') as fp:
            for line in fp.readlines():
                if len(line.strip()) > 0:
                    print(line.rstrip())


if __name__ == "__main__":
    s = sys.argv[1]
    find_best_dinasty(person_mds, s)