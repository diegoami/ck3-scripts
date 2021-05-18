import os
from ck_people import get_ck_people
from file_parse import find_family_tree, split_file_references
from collections import defaultdict
from itertools import chain
import fileinput

def living_in(target_year, all_names):
    all_birthdays = []
    for year, lines in chain(all_names["short_lines_in_years"].items(), all_names["long_lines_in_years"].items()):
        if target_year >= year:
            for line in lines:
                life_years = line.split(',')[1].split('-')
                if len(life_years) > 1 and life_years[1]:
                    birth_year, death_year = int(life_years[0]), int(life_years[1])
                    if death_year-target_year > 0:
                        all_birthdays.append((target_year - birth_year, line, death_year-target_year))
                else:
                    birth_year = int(life_years[0])
                    all_birthdays.append((target_year-birth_year, line, "UNKNOWN"))
                    #print('{} is now {} years old, death unknown.'.format(line, target_year-birth_year) )
    allbs = sorted(all_birthdays, key=lambda x:x[0], reverse=True)
    for x in allbs:
        print('{} is now {} years old, will die in {}'.format(x[1], x[0], x[2]))

def check_photos(target_year, all_names, dir_mds):
    all_birthdays = []
    for year, lines in all_names["long_lines_in_years"].items():
        if target_year >= year:
            for line in lines:
                life_years = line.split(',')[1].split('-')
                long_name = line.split(',')[0]
                file_name = all_names["long_name_to_file"][line]
                dir_name, file_extension = os.path.splitext(file_name)
                dir_img = os.path.join(dir_mds, dir_name)
                age_years = []
                if len(life_years) > 1 and life_years[1]:
                    birth_year, death_year = int(life_years[0]), int(life_years[1])
                else:
                    birth_year, death_year = int(life_years[0]), None
                if os.path.isdir(dir_img):
                    for img_name in os.listdir(dir_img):
                        img_year_s, img_ext = os.path.splitext(img_name)
                        img_year = int(img_year_s)
                        age_years.append(img_year-birth_year)
                if not death_year or death_year > target_year:
                    all_birthdays.append((target_year - birth_year, long_name, age_years, death_year, birth_year))
    allbs = sorted(all_birthdays, key=lambda x: x[0], reverse=True)
    for x in allbs:
        if x[2]:
            print('{}, born in {}, is now {} years old, photos at {} '.format(x[1], x[4], x[0], x[2]))
        else:
            print('{}, born in {}, is now {} years old, NO PHOTOS'.format(x[1], x[4], x[0], x[2]))

def get_all_names(dir_mds=None, ppl_file=None, ck_people=None):
    if not dir_mds:
        dir_mds = os.environ.get("CK_DIR")

    if not ppl_file:
        ppl_file = os.path.join(dir_mds, 'people.md')
    if not ck_people:
        ck_people = get_ck_people(ppl_file)
    long_names_in_years = defaultdict(set)
    short_names_in_years = defaultdict(set)
    short_lines_in_years = defaultdict(set)
    long_lines_in_years = defaultdict(set)
    death_fixes = defaultdict(set)
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
            plines[0] = "# {}".format(ck_person.long_name)
            olines[0] = ck_person.long_name.strip()
            print("Fixing {}".format(ck_person.long_name))
            death_fixes.add(ck_person)
        else:
            long_name_to_file[ck_person.long_name] = ck_person.file_name
            file_to_long_name[ck_person.file_name] = ck_person.long_name
            long_names_in_years[int(ck_person.birth_year)].add(ck_person.long_name)
            long_lines_in_years[int(ck_person.birth_year)].add(first_line)

            for oline in olines[1:]:
                oline = oline.strip()
                if ',' in oline:
                    name, years = [x.strip() for x in oline.strip().split(',')[:2]]
                    years_first = int(years.split('-')[0])
                    short_names_in_years[years_first].add(name)
                    short_lines_in_years[years_first].add(oline)
                    short_names_in_file[ck_person.file_name].add(name)
                    files_containing_short_names[name].add(ck_person.file_name)
                    if '  ' in oline:
                        print('{}:{} : suspicious spaces'.format(ck_person.file_name, name))

    years_keys = sorted(long_names_in_years.keys())
    for key in years_keys:
        for long_name in long_names_in_years[key]:
            for short_name in short_names_in_years[key]:

                if all([x in long_name.split() for x in short_name.split()]):
                    if long_name in long_name_to_short_name:
                        print("Short name ambigous {}, {} for {}".format(short_name, long_name_to_short_name[long_name], key))
                    short_name_to_long_name[short_name] = long_name
                    long_name_to_short_name[long_name] = short_name

    return {"long_name_to_file": long_name_to_file,
            "file_to_long_name": file_to_long_name,
            "long_names_in_years": long_names_in_years,
            "short_names_in_years": short_names_in_years,
            "short_names_in_file": short_names_in_file,
            "files_containing_short_names": files_containing_short_names,
            "short_name_to_long_name": short_name_to_long_name,
            "long_name_to_short_name": long_name_to_short_name,
            "short_lines_in_years": short_lines_in_years,
            "long_lines_in_years": long_lines_in_years,
            "death_fixes": death_fixes }

def fix_deaths(dir_mds, all_names):
    death_fixes = all_names["death_fixes"]
    for ck_person in death_fixes:
        long_name = ck_person.long_name
        short_name = all_names["long_name_to_short_name"][long_name]
        file_names = all_names["files_containing_short_names"][short_name]
        orig = "{}, {}-".format(short_name, ck_person.birth_year)
        target = "{}, {}-{}".format(short_name, ck_person.birth_year, ck_person.death_year)
        for file_name in file_names:
            full_file = os.path.join(dir_mds, file_name)
            with fileinput.FileInput(full_file, inplace=True) as file:
                for line in file:
                    print(line.replace(orig, target), end='')