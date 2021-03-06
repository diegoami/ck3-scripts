import os

from find_references_history import find_references
from lib.ck_people import get_ck_people
from lib.file_parse import split_file_references, split_file_relatives
from lib.people_walk import get_all_names
from collections import defaultdict
from lib.main_person import get_all_persons




def add_references(dir_mds, ck_people, all_names, all_persons):
    history_mds = os.path.join(dir_mds, 'h')
    history_references = find_references(history_mds)
    parents = defaultdict(set)
    children = defaultdict(set)
    great_parents = defaultdict(set)
    great_great_parents = defaultdict(set)
    siblings = defaultdict(set)
    long_name_to_file = all_names["long_name_to_file"]
    for ck_person in ck_people:
        full_file = os.path.join(dir_mds, ck_person.file_name)
        current_person = all_persons[ck_person.long_name]
        before_lines, ref_lines, after_lines = split_file_references(full_file)
        write_lines = [] + before_lines

        write_lines.append('\n')
        write_lines.append("# REFERENCES\n")
        parents_lines, children_lines = [], []

        parents[ck_person.long_name].add(current_person.father)
        parents[ck_person.long_name].add(current_person.mother)

        parents_lines += [current_person.father, current_person.mother]

        children[ck_person.long_name] = set(current_person.children)
        children_lines += current_person.children

        great_parents_lines, great_great_parents_lines = [], []
        siblings_lines = []

        for parent in parents[ck_person.long_name]:
            if parent:
                person_parent = all_persons[parent.get_name()]
                if person_parent:
                    if person_parent.father:
                        great_parents[ck_person.long_name].add(person_parent.father)
                        great_parents_lines.append(person_parent.father)
                    if person_parent.mother:
                        great_parents[ck_person.long_name].add(person_parent.mother)
                        great_parents_lines.append(person_parent.mother)
                    siblings[ck_person.long_name] = siblings[ck_person.long_name].union(person_parent.children)

        siblings_lines = list(siblings[ck_person.long_name])
        for great_parent in great_parents[ck_person.long_name]:
            if great_parent:
                person_great_parent = all_persons[great_parent.get_name()]
                if person_great_parent:
                    if person_great_parent.father:
                        great_great_parents[ck_person.long_name].add(person_great_parent.father)
                        great_great_parents_lines.append(person_great_parent.father)
                    if person_great_parent.mother:
                        great_great_parents[ck_person.long_name].add(person_great_parent.mother)
                        great_great_parents_lines.append(person_great_parent.mother)

        write_lines.append("\n")
        write_lines.append("## PARENTS \n")
        for parent in parents_lines:
            #write_lines.append("* [{}]({})\n".format(long_name, file_name))
            if parent:
                if parent.long_name:
                    write_lines.append("* [{}]({})\n".format(parent.get_name(), long_name_to_file[parent.get_name()].split('/')[1]))
                #if parent.get_name():
                #    write_lines.append("* {}\n".format(parent.get_name()))


        write_lines.append("\n")
        write_lines.append("## CHILDREN \n")
        for child in children_lines:
            #write_lines.append("* [{}]({})\n".format(long_name, file_name))
            if child.long_name:
                write_lines.append("* [{}]({})\n".format(child.get_name(), long_name_to_file[child.get_name()].split('/')[1]))
            #if child.get_name():
            #    write_lines.append("* {}\n".format(child.get_name()))


        write_lines.append("\n")
        write_lines.append("## GREAT-PARENTS \n")
        for great_parent in great_parents_lines:
            # write_lines.append("* [{}]({})\n".format(long_name, file_name))
            if great_parent.long_name:
                write_lines.append("* [{}]({})\n".format(great_parent.get_name(), long_name_to_file[great_parent.get_name()].split('/')[1]))
            #if great_parent.get_name():
            #    write_lines.append("* {}\n".format(great_parent.get_name()))


        write_lines.append("\n")
        write_lines.append("## GREAT-GREAT-PARENTS \n")
        for great_great_parent in great_great_parents_lines:
            # write_lines.append("* [{}]({})\n".format(long_name, file_name))
            if great_great_parent.long_name:
                write_lines.append("* [{}]({})\n".format(great_great_parent.get_name(), long_name_to_file[great_great_parent.get_name()].split('/')[1]))
            #if great_great_parent.get_name():
            #   write_lines.append("* {}\n".format(great_great_parent.get_name()))


        write_lines.append("## SIBLINGS\n")
        for sibling in siblings_lines:
            if sibling.long_name and sibling.long_name != ck_person.long_name:
                write_lines.append("* [{}]({})\n".format(sibling.get_name(), long_name_to_file[sibling.get_name()].split('/')[1]))


        write_lines.append(" \n## HISTORY")
        write_lines.append("\n")
        if ck_person.file_name in history_references:
            for history_name in sorted(history_references[ck_person.file_name]):
                write_lines.append("* [{}](../h/{})\n".format(history_name, history_name))
        write_lines.append("\n#### END REFERENCES\n")
        write_lines += after_lines
        with open(full_file, 'w', encoding='latin1') as f:
            f.writelines(write_lines)

    return parents, children


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

    #ancestors, descendents = add_references(dir_mds, ck_people, all_names)
    all_persons = get_all_persons(all_names)
    add_references(dir_mds, ck_people, all_names, all_persons)
    #relatives = add_relatives(dir_mds, ck_people, all_names, ancestors, descendents)