import os
import re

import sys

file_names = []
#s = sys.argv[0]
s = "Earl Farannan"    

best_files, most_tabs = [], 100
for file_name in os.listdir(os.getcwd()):
    if ('.md' in file_name):
        with open(file_name, 'r') as fp:
            for line in fp.readlines():
                num_tabs = len([x for x in line if x == '\t'])
                if s in line:
                    if num_tabs < most_tabs:
                        best_files, most_tabs = [file_name], num_tabs
                    elif num_tabs == most_tabs:
                        best_files.append(file_name)

for best_file in best_files:
    print(best_file)
    print("\n")
    with open(best_file, 'r') as fp:
        for line in fp.readlines():
            if len(line.strip()) > 0:
                print(line.rstrip())
        
