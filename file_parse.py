import sys
import ck_people

def find_family_tree(full_file):
    olines, plines, alines = [], [], []
    with open(full_file, 'r') as f:
        in_family_tree = 0
        for i, line in enumerate(f.readlines()):

            if "FAMILY TREE" in line:
                in_family_tree = 1
                continue
            if "`" in line and in_family_tree == 1:
                in_family_tree = 2
                continue

            if in_family_tree == 2:
                if "`" in line:
                    in_family_tree = 3
                    continue
                else:
                    olines.append(line.rstrip())

            if in_family_tree == 0:
                plines.append(line)

            if in_family_tree == 3:
                alines.append(line)

        if not olines or in_family_tree != 3:
            print("{} is invalid".format(full_file))
            sys.exit(1)
    return olines, plines, alines


