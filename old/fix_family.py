from lib.people_walk import find_family_tree
import os

if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")
    people_mds = os.path.join(dir_mds, 'p')
    for file in os.listdir(people_mds):
        full_file = os.path.join(people_mds, file)

        if '.md' in file:
            ol, bl, al = find_family_tree(full_file)
            print("============\n")
            print(full_file+"\n")
            print("============\n")
            print(ol)