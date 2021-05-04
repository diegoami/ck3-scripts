import os
import re
from collections import namedtuple
from collections import defaultdict
zz_groups = []
CkPerson = namedtuple('CkPerson', ['name', 'file_name', 'birth_year', 'death_year', 'title', 'house', 'long_name' ])

dir_mds = os.environ.get("CK_DIR")
ppl_file = os.path.join(dir_mds, 'people.md')
ck_people = []
dps = defaultdict(set)

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
            print(ck_person)
            print(long_name)
            ck_people.append(ck_person)
dps = {}

for ck_person in ck_people:
     full_file = os.path.join(dir_mds, ck_person.file_name)

     with open(full_file, 'r') as f:
         olines = []
         in_family_tree = False
         for i, line in enumerate(f.readlines()):
              if i == 0:

                   long_name_title = line[2:].strip()
              if in_family_tree:

                   if "`" in line:
                        in_family_tree = False
                        break
                   else:
                        olines.append(line.rstrip())
              else:
                   if "`" in line:
                        in_family_tree = True
                        continue

         first_line = olines[0].strip()
         print("===================================================")
         if not (first_line == long_name_title == ck_person.long_name):
              print(first_line)
              print(long_name_title)
              print(ck_person.long_name.strip())
         else:
             for oline in olines[1:]:
                 oline = oline.strip()
                 if len(oline) > 0 and not re.match('[\w\s\-\'\+]+\,\s+[0-9\-\s]+', oline) and not '?' in oline:
                     print(ck_person.file_name)
                     print(oline)

             for oline in olines:
                 if ',' in oline:
                      name, years = [ x.strip() for x in oline.strip().split(',')[:2]]
                      years_first = int(years.split('-')[0])
                      if not years_first in dps:
                          dps[years_first] = set()
                      dps[years_first].add(oline.strip())

dpkeys = sorted( dps.keys())


for key in dpkeys:
    if len(dps[key]) > 1:
        print("========================")
        print(key)
        print("========================")

        for vls in sorted(dps[key]):
            print(vls)


