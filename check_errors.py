import os

from find_references_history import find_references
from ck_people import get_ck_people
from file_parse import find_family_tree, split_file_references
from people_walk import get_all_names


if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")

    ck_people = get_ck_people()
    ppl_file = os.path.join(dir_mds, 'people.md')
    all_names = get_all_names(dir_mds, ppl_file, ck_people)

