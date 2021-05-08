import re
from collections import namedtuple
import os
CkPerson = namedtuple('CkPerson', ['name', 'file_name', 'birth_year', 'death_year', 'title', 'house', 'long_name', 'full_line' ])

def get_long_name_from_person(name, title, birth_year, death_year, house):
    if title:
        if 'of' in title:
            title_s, location = title.split(' of ')
            long_name = title_s + ' ' + name + ' of ' + location + ', ' + birth_year + '-' + death_year + ', ' + house
        else:
            long_name = title + ' ' + name + ', ' + birth_year + '-' + death_year + ', ' + house
    else:
        long_name = name + ', ' + birth_year + '-' + death_year + ', ' + house
    return long_name

def get_ck_person(line):
    full_line = line
    name = file_name = title = house = birth_year = death_year = ''
    zm = re.search(r'\[([\w\s\-\+]+)\]\((.*?)\)\s+\(([0-9\-\s]+)\)', line)
    zo = re.search(r'\*(.*)\*', line)
    if zm:
        name = zm.group(1).strip()
        file_name = zm.group(2).strip()
        years = zm.group(3)
        years_a = years.split('-')
        birth_year = years_a[0].strip()
        if (len(years_a) > 0) and len(years_a[1].strip()) > 0:
            death_year = years_a[1].strip()
    if zo:
        title_house = zo.group(1)
        if title_house.strip().startswith(','):
            title_house = title_house[1:]
        title_house_a = title_house.strip().split(',')
        if (len(title_house_a)) > 0:
            if (len(title_house_a)) > 1:
                title = title_house_a[0].strip()
                house = title_house_a[1].strip()
            else:
                house = title_house_a[0].strip()
    if name and file_name:
        long_name = get_long_name_from_person(name, title, birth_year, death_year, house)

        ck_person = CkPerson(name=name, file_name=file_name, birth_year=birth_year, death_year=death_year,
                             title=title, house=house, long_name=long_name, full_line=full_line)
        return ck_person
    return None

def complete_person(ck_person):
    ck_person = ck_person._replace(long_name=get_long_name_from_person(ck_person.name, ck_person.title, ck_person.birth_year, ck_person.death_year, ck_person.house))
    ck_person = ck_person._replace(file_name=(ck_person.name + " " + ck_person.birth_year+".md").replace(' ', '_').lower())

    if ck_person.title:
        ck_person = ck_person._replace(full_line="- [{}](p/{}) ({}-{}), *{}, {}*".format(
            ck_person.name, ck_person.file_name, ck_person.birth_year, ck_person.death_year, ck_person.title, ck_person.house))
    else:
        ck_person = ck_person._replace(full_line="- [{}](p/{}) ({}-{}), *{}*".format(
            ck_person.name, ck_person.file_name, ck_person.birth_year, ck_person.death_year, ck_person.house))
    return ck_person

def get_ck_people(ppl_file):
    ck_people = []
    with open(ppl_file, 'r') as fp:
        for line in fp.readlines():
            ck_person = get_ck_person(line)
            if ck_person:
                ck_people.append(ck_person)
    return ck_people

def add_ck_person(ck_people, ppl_file, new_person):
    new_person = complete_person(new_person)
    print(new_person)
    with open(ppl_file, 'w') as fp:
        fp.write('# PEOPLE\n\n')
        added_person = False
        for ck_person in ck_people:
            if new_person.name == ck_person.name:
                print("{} exists".format(new_person.name))
                added_person = True
                continue
            if new_person.name < ck_person.name and not added_person:
                fp.write('{}\n'.format(new_person.full_line.rstrip()))
                print("{} added".format(new_person.name))

                added_person = True
            fp.write('{}\n'.format(ck_person.full_line.rstrip()))


def add_person(s):
    dir_mds = os.environ.get("CK_DIR")
    full_file = os.path.join(dir_mds, 'people.md')
    ck_people = get_ck_people(full_file)
    out_file = os.path.join(dir_mds, 'people.md')
    sl = s.split(',')
    to_add_person = CkPerson(name=sl[0], birth_year=sl[1], death_year=sl[2], title=sl[3], house=sl[4], file_name=None, long_name=None, full_line=None)
    to_add_person = complete_person(to_add_person)
    add_ck_person(ck_people, out_file, to_add_person)
    full_file_name = os.path.join(dir_mds, 'p', to_add_person.file_name)
    if not os.path.isfile(full_file_name):
        with open(full_file_name, 'w') as fw:
            fw.write("# {}\n".format(to_add_person.long_name))
            fw.write("\n")
            fw.write("## FAMILY TREE\n")
            fw.write("```\n")
            fw.write("{}\n".format(to_add_person.long_name))
            fw.write("```\n")
            print("{} added".format(full_file_name))

    else:
        print("{} exists".format(full_file_name))


