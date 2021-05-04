import os
import re
from collections import namedtuple
zz_groups = []
Ckperson = namedtuple('Ckperson', ['name', 'file_name', 'years', 'titles' ])

dir_mds = os.environ.get("CK3_DIR")
ppl_file = os.path.join(dir_mds, 'people.md')

with open(ppl_file, 'r') as fp:
    for line in fp.readlines():
        zm = re.search('\[([\w\s\-\+]+)\]\((.*?)\)\s+\(([0-9\-\s]+)\).*\*(.*)\*', line)
        if zm:
            zz_groups.append(zm.groups(1))

dps = {}
            
work_all = []
for zz_s in zz_groups:
    work_info = [] 
    full_file = os.path.join(dir_mds, zz_s[1])
    short_list = zz_s[1].split('/')[1].split('_')[:-1]
    name_list = zz_s[0].strip().lower().split()
    word_list = set(name_list + [zz_s[2].strip()]+zz_s[3].replace(',',' ').lower().strip().split())

   

    with open(full_file, 'r') as f:
        olines = []
        in_family_tree = False
        for i, line in enumerate(f.readlines()):
             if i == 0:
                  
                  title_list = set(line[2:].replace(',',' ').replace('(',' ').replace(')',' ').strip().lower().split())
                  #print(title_list)
             if in_family_tree:
                  
                  if "```" in line:
                       in_family_tree = False
                       break
                  else:
                       olines.append(line.rstrip())
             else:
                  if "```" in line:
                       in_family_tree = True
                       continue

        first_line = set(olines[0].lower().replace(',',' ').replace('(',' ').replace(')',' ').strip().split())
        
        #print(first_line)
        if not (first_line == title_list == word_list):
             print(word_list)
             print(title_list)
             print(first_line)
        else:
            #dps[date_str].add(lines[0].strip().split(',')[0].strip()
             for oline in olines[1:]:
                  print(oline)
                  if ',' in oline:

                      name, years = [ x.strip() for x in oline.strip().split(',')[:2]]
                      if not years in dps:
                          dps[years] = set()
                      dps[years].add(name)                   

dpkeys = sorted(dps.keys())


for key in dpkeys:
    if len(dps[key]) > 1:
        print("========================")
        print(key)
        print("========================")
   
        for vls in sorted(dps[key]):
            print(vls)

    
