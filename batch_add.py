import ck_people

import sys
import os
from functools import partial

from find_best_dinasty import find_best_dinasty
from people_walk import fix_short_deaths, get_all_names

if __name__ == "__main__":


    dir_mds = os.environ.get("CK_DIR")
    person_mds = os.path.join(dir_mds, 'p')
    all_names = get_all_names(dir_mds)
    _c = ck_people.add_person
    def _f(s):
        return find_best_dinasty(person_mds, s)
    def _s(short_name, birth_year, death_year):
        return fix_short_deaths(all_names, short_name, birth_year, death_year)

    #_c("Mael-Muire Gormflaithdohtor,1268,,Duchess of East Seaxe,hEochadha")
    #_f("Princess Marthoc")
    #_s("Martha Kyle", 1210, )
    _c("Udalschalk mag Eilika,1096,1162,Duke of Meath,Cilli")
