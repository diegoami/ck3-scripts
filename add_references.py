import os

from find_references_history import find_references
from ck_people import get_ck_people
from file_parse import find_family_tree, split_file_references, split_file_relatives
from people_walk import get_all_names
from collections import defaultdict


def add_references(dir_mds, ck_people, all_names):
    history_mds = os.path.join(dir_mds, 'h')
    history_references = find_references(history_mds)
    ancestors = defaultdict(set)
    descendents = defaultdict(set)

    for ck_person in ck_people:
        full_file = os.path.join(dir_mds, ck_person.file_name)
        before_lines, ref_lines, after_lines = split_file_references(full_file)
        write_lines = [] + before_lines

        write_lines.append('\n')
        write_lines.append("# REFERENCES\n")
        ancestor_lines, descendant_lines = [], []
        for short_name in all_names["short_names_in_file"][ck_person.file_name]:
            if short_name in all_names["short_name_to_long_name"]:
                long_name = all_names["short_name_to_long_name"][short_name]
                file_l_name = all_names["long_name_to_file"][long_name].split('/')[1]
                ancestors[ck_person.long_name].add(long_name)
                ancestor_lines.append((long_name, file_l_name))
        if ck_person.long_name in all_names["long_name_to_short_name"]:
            curr_short_name = all_names["long_name_to_short_name"][ck_person.long_name]
            for file_name in sorted(all_names["files_containing_short_names"][curr_short_name]):
                long_name = all_names["file_to_long_name"][file_name]
                file_l_name = file_name.split('/')[1]
                descendents[ck_person.long_name].add(long_name)
                descendant_lines.append((long_name, file_l_name))

        ancestor_lines = sorted(ancestor_lines, key=lambda x: x[1])
        descendant_lines = sorted(descendant_lines, key=lambda x: x[1])

        write_lines.append("\n")
        write_lines.append("## ANCESTORS\n")
        for long_name, file_name in ancestor_lines:
            write_lines.append("* [{}]({})\n".format(long_name, file_name))

        write_lines.append("\n")
        write_lines.append("## DESCENDANTS\n")
        for long_name, file_name in descendant_lines:
            write_lines.append("* [{}]({})\n".format(long_name, file_name))

        write_lines.append("\n")
        write_lines.append("## RELATIVES\n")
        write_lines.append("\n")
        write_lines.append("##### END RELATIVES \n")

        write_lines.append("## HISTORY")
        write_lines.append("\n")
        if ck_person.file_name in history_references:
            for history_name in sorted(history_references[ck_person.file_name]):
                write_lines.append("* [{}](../h/{})\n".format(history_name, history_name))
        write_lines.append("\n#### END REFERENCES\n")
        write_lines += after_lines
        with open(full_file, 'w', encoding='latin1') as f:
            f.writelines(write_lines)

    return ancestors, descendents


def add_relatives(dir_mds, ck_people, all_names, ancestors, descendants):
    relatives = defaultdict(set)
    for ck_person in ck_people:
        full_file = os.path.join(dir_mds, ck_person.file_name)
        sbirth, sdeath = int(ck_person.birth_year), int(ck_person.death_year) if ck_person.death_year else 9999
        before_lines, ref_lines, after_lines = split_file_relatives(full_file)
        write_lines = [] + before_lines
        write_lines.append("## RELATIVES \n")
        write_lines.append("\n")
        curr_ancestors = ancestors[ck_person.long_name]
        relatives_lines = set()
        for curr_ancestor_long_name in curr_ancestors:
            curr_descendants = descendants[curr_ancestor_long_name]
            for curr_descendant_long_name in curr_descendants:
                life_years = curr_descendant_long_name.split(',')[1].split('-')

                obirth, odeath = int(life_years[0]),  int(life_years[1]) if len (life_years) > 1 and life_years[1] else 9999
                file_name = all_names["long_name_to_file"][curr_descendant_long_name].split('/')[1]
                rr = (range(max(obirth, sbirth), min(odeath, sdeath) +1))
                print(rr)
                if rr:
                    relatives[curr_ancestor_long_name].add(curr_descendant_long_name)
                    relatives_lines.add((curr_descendant_long_name, file_name))
        relatives_lines = sorted(list(relatives_lines), key=lambda x: x[1])
        for long_name, file_name in relatives_lines:
            write_lines.append("* [{}]({})\n".format(long_name, file_name))
        write_lines.append("\n")
        write_lines.append("##### END RELATIVES \n")
        write_lines += after_lines
        with open(full_file, 'w', encoding='latin1') as f:
            f.writelines(write_lines)
    return relatives

if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")

    ck_people = get_ck_people()
    ppl_file = os.path.join(dir_mds, 'people.md')
    all_names = get_all_names(dir_mds, ppl_file, ck_people)

    ancestors, descendents = add_references(dir_mds, ck_people, all_names)
    #relatives = add_relatives(dir_mds, ck_people, all_names, ancestors, descendents)