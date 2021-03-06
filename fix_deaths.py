import os
from lib.people_walk import get_all_names, fix_deaths
from lib.ck_people import get_ck_people

if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")

    ppl_file = os.path.join(dir_mds, 'people.md')
    ck_people = get_ck_people(ppl_file)
    all_names = get_all_names(dir_mds)
    fix_deaths(dir_mds, all_names)
