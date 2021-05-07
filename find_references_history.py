import os
import re
from collections import defaultdict

def find_references(history_mds):
    history_maps = defaultdict(set)
    for file_name in os.listdir(history_mds):
        if ('.md' in file_name):
            with open(os.path.join(history_mds, file_name), 'r') as fp:
                full_text = fp.read()
                zms = re.findall(r'\[([\w\*\s\-\+]+)\]\(([\w\.\/\_]+)\)', full_text)
            for zm in zms:
                text, url = zm[0].replace('*',''), zm[1]
                if not os.path.isfile(os.path.join(history_mds, url)):
                    print("Cannot find {} in {}".format(url, file_name))
                l_url = url.split('/')
                l_words = l_url[2].split('_')[:-1]
                if not ( all([x.lower() in text.lower() for x in l_words]) or all([x in l_words for x in text.lower().split()]) ) :
                    print("{} : {} and {} do not match".format(file_name, text, url))

                history_maps['p/{}'.format(l_url[2])].add(file_name)
    print(history_maps)
    return history_maps

if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")
    history_mds = os.path.join(dir_mds, 'h')
    find_references(history_mds)