
from ck_people import get_ck_people
from file_parse import find_family_tree, split_file_references, split_file_relatives
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
                   self.father.short_name if self.father else "",
                   self.mother.short_name if self.mother else "",
                   [x.short_name for x in self.children])

def get_all_persons(all_names):
    all_persons = defaultdict(MainPerson)
    fathers = all_names["fathers"]
    mothers = all_names["mothers"]
    long_name_to_short_name = all_names["long_name_to_short_name"]
    short_name_to_long_name = all_names["short_name_to_long_name"]

    def process_rel_list(relatives):
        for child, rels in relatives.items():
            if (len(rels) > 1):
                print("{} has too many parents: {}".format(child, rels))
            for rel in rels:
                if child in short_name_to_long_name:
                    key_name = short_name_to_long_name[child]
                else:
                    key_name = child
                all_persons[key_name].set_name(child)
                all_persons[key_name].father = all_persons[rel]
                all_persons[rel].set_name(rel)
                all_persons[rel].children.add(all_persons[key_name])

    process_rel_list(fathers)
    process_rel_list(mothers)
    return all_persons


if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")

    ck_people = get_ck_people()
    ppl_file = os.path.join(dir_mds, 'people.md')
    all_names = get_all_names(dir_mds, ppl_file, ck_people)
    persons = get_all_persons(all_names)
    for person_key, person in persons.items():
        print(person)



