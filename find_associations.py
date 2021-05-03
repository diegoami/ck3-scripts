import os
import re

def do_replace(source, zz_st, format_tt):
     for zz_s in zz_st:   
        with open(source, 'r') as fa:
            file_source = fa.read()
            old, new = zz_s[1][1], format_tt.format(zz_s[0])
            print('replacing {} with {}'.format(old, new))
            replace_file = file_source.replace(old, new)
            
        with open(source, 'w') as fw:
            fw.write(replace_file)    

dir_mds = 'C:\Users\diego\ck3aars\ck3-murchad\p'
ppl_file = "C:\\Users\\diego\\ck3aars\\ck3-murchad\\refpeople.md"
ppl_newfile = 'C:\Users\diego\ck3aars\ck3-murchad\people.md'
history_dirs = 'C:\Users\diego\ck3aars\ck3-murchad\h'
history_ffs = history_oos = ['1209.md', '1227.md', '1249.md']

file_names = []  
for file_name in os.listdir(dir_mds):
    if ('.md' in file_name):
       file_names.append(file_name)

zz_groups = []

    
with open(ppl_file, 'r') as fp:
    for line in fp.readlines():
        zm = re.search('\[([\w\s\-\+]+)\]\((.*?)\)', line)
        if zm:
            zz_groups.append(zm.groups(1))
            

zz_all = zz_groups[:len(file_names)]

zz_st = zip(file_names, zz_all)
for zz_s in zz_st:
    print(zz_s)

if True:
    for history_ff, history_oo in zip(history_ffs, history_oos):
        file_to_ana = os.path.join(history_dirs, history_ff)
        do_replace(file_to_ana, zz_st, '../p/{}')
        
    do_replace(ppl_newfile, zz_st, 'p/{}')
    
