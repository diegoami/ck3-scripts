import os
import sys
from file_parse import find_family_tree


from find_references_history import find_references
from ck_people import get_ck_people
from file_parse import find_family_tree, split_file_references
from people_walk import get_all_names


def find_best_dinasty(person_mds, s):

    best_files, most_tabs = [], 100
    for file_name in os.listdir(person_mds):
        if ('.md' in file_name):

            with open(os.path.join(person_mds, file_name), 'r', encoding='latin1') as fp:
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
        full_file = os.path.join(person_mds, best_file)
        olines, plines, alines = find_family_tree(full_file)
        for line in olines:
            print(line)


def find_best_family(fathers, mothers, s, depth=4):
    if depth >= 0:
        sn = (4-depth)*4*' '
        print("{}{}".format(sn, s))
        for father in fathers[s]:
            find_best_family(fathers, mothers, father, depth-1)
        for mother in mothers[s]:
            find_best_family(fathers, mothers, mother, depth-1)

if __name__ == "__main__":
    s = sys.argv[1]
    #find_best_dinasty(person_mds, s)
    dir_mds = os.environ.get("CK_DIR")
    ppl_file = os.path.join(dir_mds, 'people.md')

    ck_people = get_ck_people(ppl_file)
    all_names = get_all_names(dir_mds, ppl_file, ck_people)
    fathers, mothers = all_names["fathers"], all_names["mothers"]
    find_family(fathers, mothers, "Duchess Rhiandrech, 1116-1187", 4)