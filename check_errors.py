import os
import sys
from collections import defaultdict
from find_references_history import find_references
from ck_people import get_ck_people
from file_parse import find_family_tree

def get_all_names(dir_mds=None, ppl_file=None, ck_people=None):
    if not dir_mds:
        dir_mds = os.environ.get("CK_DIR")

    if not ppl_file:
        ppl_file = os.path.join(dir_mds, 'people.md')
    if not ck_people:
        ck_people = get_ck_people(ppl_file)
    long_names_in_years = defaultdict(set)
    short_names_in_years = defaultdict(set)
    short_name_to_long_name = {}
    long_name_to_short_name = {}
    long_name_to_file = {}
    file_to_long_name = {}
    short_names_in_file = defaultdict(set)
    files_containing_short_names = defaultdict(set)



    for ck_person in ck_people:
        full_file = os.path.join(dir_mds, ck_person.file_name)
        olines, plines, alines = find_family_tree(full_file)
        long_name_title = plines[0][2:].strip()
        first_line = olines[0].strip()
        if not (first_line == long_name_title == ck_person.long_name):
            print(first_line)
            print(long_name_title)
            print(ck_person.long_name.strip())
        else:
            long_name_to_file[ck_person.long_name] = ck_person.file_name
            file_to_long_name[ck_person.file_name] = ck_person.long_name
            long_names_in_years[int(ck_person.birth_year)].add(ck_person.long_name)
            for oline in olines[1:]:
                oline = oline.strip()
                if ',' in oline:
                    name, years = [x.strip() for x in oline.strip().split(',')[:2]]
                    years_first = int(years.split('-')[0])
                    short_names_in_years[years_first].add(name)
                    short_names_in_file[ck_person.file_name].add(name)
                    files_containing_short_names[name].add(ck_person.file_name)
                    if '  ' in oline:
                        print('{}:{} : suspicious spaces'.format(ck_person.file_name, name))

    years_keys = sorted(long_names_in_years.keys())
    for key in years_keys:
        for long_name in long_names_in_years[key]:
            for short_name in short_names_in_years[key]:

                if all([x in long_name for x in short_name.split()]):
                    if long_name in long_name_to_short_name:
                        print("Short name ambigous {}, {}".format(short_name, long_name_to_short_name[long_name]))
                    short_name_to_long_name[short_name] = long_name
                    long_name_to_short_name[long_name] = short_name

    return {"long_name_to_file": long_name_to_file,
            "file_to_long_name": file_to_long_name,
            "long_names_in_years": long_names_in_years,
            "short_names_in_years": short_names_in_years,
            "short_names_in_file": short_names_in_file,
            "files_containing_short_names": files_containing_short_names,
            "short_name_to_long_name": short_name_to_long_name,
            "long_name_to_short_name": long_name_to_short_name}


if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")
    history_mds = os.path.join(dir_mds, 'h')
    history_references = find_references(history_mds)
    ck_people = get_ck_people()
    ppl_file = os.path.join(dir_mds, 'people.md')
    all_names = get_all_names(dir_mds, ppl_file, ck_people)

    for ck_person in ck_people:
        full_file = os.path.join(dir_mds, ck_person.file_name)
        with open(full_file, 'r') as f:
            write_lines = []
            all_lines = f.readlines()
            empty_lines = 0
            in_reference = 0
            for all_line in all_lines:
                if "ANCESTORS" in all_line or "REFERENCES" in all_line or all_line.startswith("* "):
                    in_reference = 1
                    continue
                if "END REFERENCES" in all_line:
                    in_reference = 2
                    continue
                if in_reference == 0 and len(all_line.strip()) == 0 :
                    empty_lines += 1
                    if empty_lines <= 1:
                        write_lines.append(all_line)
                elif in_reference == 0:
                    empty_lines = 0
                    write_lines.append(all_line)

        write_lines.append('\n')
        write_lines.append("# REFERENCES\n")
        write_lines.append("\n")

        write_lines.append("## ANCESTORS\n")
        for short_name in all_names["short_names_in_file"][ck_person.file_name]:

            if short_name in all_names["short_name_to_long_name"]:
                long_name = all_names["short_name_to_long_name"][short_name]
                file_l_name = all_names["long_name_to_file"][long_name].split('/')[1]
                write_lines.append("* [{}]({})\n".format(long_name, file_l_name))
        write_lines.append("\n")
        write_lines.append("## HISTORY")
        write_lines.append("\n")
        if ck_person.file_name in history_references:
            for history_name in sorted(history_references[ck_person.file_name]):
                write_lines.append("* [{}](../h/{})\n".format(history_name, history_name))
                write_lines.append("#### END REFERENCES")
        with open(full_file, 'w') as f:
            f.writelines(write_lines)