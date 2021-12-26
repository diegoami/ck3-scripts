import os
from lib.people_walk import get_all_names
import difflib

def remove_titles(s):
    return s

if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")
    all_names = get_all_names(dir_mds)
    short_name_in_years = all_names["short_names_in_years"]
    skeys = sorted(short_name_in_years.keys())
    long_name_in_years = all_names["long_names_in_years"]
    print(short_name_in_years)
    for skey in skeys:
        values = short_name_in_years[skey]
        if (len(values) > 1):
            for value in values:
                vcopy = list(values)
                vcopy.remove(value)

                close_matches = difflib.get_close_matches(remove_titles(value), [remove_titles(x) for x in vcopy])
                if close_matches:
                    print("{}: {}, {}".format(skey, value, close_matches))