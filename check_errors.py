import os
import re
import sys
from collections import namedtuple
from collections import defaultdict
zz_groups = []
CkPerson = namedtuple('CkPerson', ['name', 'file_name', 'birth_year', 'death_year', 'title', 'house', 'long_name' ])

dir_mds = os.environ.get("CK_DIR")
ppl_file = os.path.join(dir_mds, 'people.md')
ck_people = []
long_names_in_years = defaultdict(set)

with open(ppl_file, 'r') as fp:
    for line in fp.readlines():
        name = file_name = title = house = birth_year = death_year = ''

        zm = re.search('\[([\w\s\-\+]+)\]\((.*?)\)\s+\(([0-9\-\s]+)\)', line)
        zo = re.search('\*(.*)\*', line)

        if zm:
            zz_groups.append(zm.groups())
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
            if title:
                if 'of' in title:
                    title_s, location = title.split(' of ')
                    long_name = title_s + ' ' + name + ' of '+location + ', ' + birth_year + '-' + death_year + ', ' + house
                else:
                    long_name = title + ' ' + name + ', ' + birth_year + '-' + death_year + ', ' + house
            else:
                long_name = name + ', ' + birth_year + '-' + death_year + ', ' + house
            ck_person = CkPerson(name=name, file_name=file_name, birth_year=birth_year, death_year=death_year, title=title, house=house, long_name=long_name)
            ck_people.append(ck_person)

long_names_in_years = defaultdict(set)
short_names_in_years = defaultdict(set)


short_name_to_long_name = {}
long_name_to_short_name = {}
long_name_to_file = {}
file_to_long_name = {}
years_to_long_names = {}

short_names_in_file = defaultdict(set)
files_containing_short_names = defaultdict(set)

for ck_person in ck_people:
     full_file = os.path.join(dir_mds, ck_person.file_name)
     with open(full_file, 'r') as f:
         olines = []
         in_family_tree = 0
         for i, line in enumerate(f.readlines()):
              if i == 0:
                   long_name_title = line[2:].strip()
              if "FAMILY TREE" in line:
                  in_family_tree = 1
                  continue
              if "`" in line and in_family_tree == 1:
                  in_family_tree = 2
                  continue

              if in_family_tree == 2:
                   if "`" in line:
                        in_family_tree = 0
                        break
                   else:
                        olines.append(line.rstrip())

         if not olines or in_family_tree != 0:
             print("{} is invalid".format(full_file))
             sys.exit(1)
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


years_keys = sorted(long_names_in_years.keys())
for key in years_keys:
    for long_name in long_names_in_years[key]:
        write_lines = []
        for short_name in short_names_in_years[key]:

            if all([x in long_name for x in short_name.split()]):
                if long_name in long_name_to_short_name:
                    print("Short name ambigous {}, {}".format(short_name, long_name_to_short_name[long_name]))
                short_name_to_long_name[short_name] = long_name
                long_name_to_short_name[long_name] = short_name

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
                in_reference = 0
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
        for short_name in short_names_in_file[ck_person.file_name]:

            if short_name in short_name_to_long_name:
                long_name = short_name_to_long_name[short_name]
                file_l_name = long_name_to_file[long_name].split('/')[1]
                write_lines.append("* [{}]({})\n".format(long_name, file_l_name))
        write_lines.append("#### END REFERENCES")
    with open(full_file, 'w') as f:
        f.writelines(write_lines)