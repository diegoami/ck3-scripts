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
    #_f("Beorthflaed")
    #_s("Martha Kyle", 1210, )
    #_c("Udalschalk mag Eilika,1096,1162,Duke of Meath,Cilli")
    #_c("Ylva Drifadohtor,1261,,Duchess of Mercia,Hagalin")
    #_c("Cathan Cathandohtor,1247,,Duchess of Cornwall,Briain")
    #_c("Beorhtric Muirennson,1265,,Duke,Briain")
    #_c("Wulfwynn Riandohtor,1273,,Duchess of Herefordshire,Llewellyn")
    #_c("Cristina nic Cristina,1277,,Duchess of Connacht,gCais-Macclesfield")
    #_c("Gormlaith nic Gormlaith,1231,,Countess of Ui-Mhaine,gCais-Gaillimhe")
    #_c("Muirenne nic Pierre,1275,,Duchess of Ulster,gCais-Macclesfield")
    _c("Catriona nic Bruatur,1261,,Lady of Ceredigion,Llewellyn")