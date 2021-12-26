
from lib.ck_people import get_ck_people
from people_walk import get_all_names
import os
from collections import defaultdict

class MainPerson:

    def __init__(self):
        self.father = None
        self.mother = None
        self.children = set()
        self.long_name = None
        self.short_name = None

    def get_name(self):
        if self.long_name:
            return self.long_name

        if self.short_name:
            return self.short_name

        return ""
    def set_name(self, name):
        if name == '?':
            return
        if len(name.split(',')) == 2:
            if self.short_name and name != self.short_name:
                print("Duplicates {} : {}".format(self.short_name, name))
            else:
                self.short_name = name
        elif len(name.split(',')) == 3:
            if self.long_name and name != self.long_name:
                print("Duplicates {} : {}".format(self.long_name, name))
            else:
                self.long_name = name
        else:
            print("{} not recognized".format(name))

    def __str__ (self):
        return "name={}, short_name={}, father={}, mother={}, children={}".format(self.long_name, self.short_name,
                   self.father.get_name() if self.father else "",
                   self.mother.get_name() if self.mother else "",
                   [x.get_name() for x in self.children])

def get_all_persons(all_names):
    all_persons = defaultdict(MainPerson)
    fathers = all_names["fathers"]
    mothers = all_names["mothers"]
    long_name_to_short_name = all_names["long_name_to_short_name"]
    short_name_to_long_name = all_names["short_name_to_long_name"]

    long_name_lines_to_short_name_lines = all_names["long_name_lines_to_short_name_lines"]
    short_name_lines_to_long_name_lines = all_names["short_name_lines_to_long_name_lines"]

    def process_rel_list(relatives, is_father=True):
        for child, rels in relatives.items():
            if (len(rels) > 1):
                print("{} has too many parents: {}".format(child, rels))
            for rel in rels:
                if child in short_name_lines_to_long_name_lines:
                    key_name = list(short_name_lines_to_long_name_lines[child]).pop()
                else:
                    key_name = child
                all_persons[key_name].set_name(child)
                if is_father:
                    all_persons[key_name].father = all_persons[rel]
                else:
                    all_persons[key_name].mother = all_persons[rel]
                all_persons[rel].set_name(rel)
                all_persons[rel].children.add(all_persons[key_name])
                if rel in short_name_lines_to_long_name_lines:
                    long_rel_names = short_name_lines_to_long_name_lines[rel]
                    for long_rel_name in long_rel_names:
                        all_persons[long_rel_name].set_name(long_rel_name)
                        all_persons[long_rel_name].children = all_persons[long_rel_name].children.union(all_persons[rel].children)
                        all_persons[rel].set_name(long_rel_name)

    process_rel_list(fathers)
    process_rel_list(mothers, False)
    return all_persons


if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")

    ck_people = get_ck_people()
    ppl_file = os.path.join(dir_mds, 'people.md')
    all_names = get_all_names(dir_mds, ppl_file, ck_people)
    persons = get_all_persons(all_names)
    for person_key, person in persons.items():
        print(person)



