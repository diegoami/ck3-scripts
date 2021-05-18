import os
from people_walk import living_in, check_photos
from people_walk import get_all_names, fix_deaths
from ck_people import get_ck_people
import sys

if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")

    ppl_file = os.path.join(dir_mds, 'people.md')
    ck_people = get_ck_people(ppl_file)
    all_names = get_all_names(dir_mds)
    fix_deaths(dir_mds, dir_mds, all_names["death_fixes"])