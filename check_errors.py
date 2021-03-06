import os

from lib.ck_people import get_ck_people
from lib.people_walk import get_all_names


if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")
    ppl_file = os.path.join(dir_mds, 'people.md')

    ck_people = get_ck_people(ppl_file)
    # Implicitly fixes errors in titles
    all_names = get_all_names(dir_mds, ppl_file, ck_people)
    #print(all_names["short_name_to_long_name"])
    #print(all_names["long_name_to_short_name"])
    #
    #for key, value in all_names["fathers"].items():
     #   print(key, value)

    #for key, value in all_names["mothers"].items():
    #    print(key, value)