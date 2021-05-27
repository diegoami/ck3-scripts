import ck_people

import sys
import os
from functools import partial

from find_best_dinasty import find_best_dinasty, find_best_family
from people_walk import fix_short_deaths, get_all_names

if __name__ == "__main__":


    dir_mds = os.environ.get("CK_DIR")
    person_mds = os.path.join(dir_mds, 'p')
    all_names = get_all_names(dir_mds)
    mothers, fathers = all_names["mothers"], all_names["fathers"]

    _c = ck_people.add_person
    def _f(s):

        return find_best_family(fathers, mothers, s, 4)
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
    #_c("Catriona nic Bruatur,1261,,Lady of Ceredigion,Llewellyn")
    #_c("Coilboth mag Etain,1287,,Lord of Brycheiniog,Briain")
    #_c("Der-Lugdach,1266,,Duchess of Westfalen,gCais-Mathrafal")
    #_c("Slaine Eithnedohtor,1268,,,gCais-Mathrafal")
    #_c("Gruffydd III ap Maredudd,1064,1140,Petty King of Deheubarth,Caerloyw-Penfro")
    #_c("Gruffydd ap Maredudd,1116,1177,,Caerloyw-Penfro")
    #_c("Domnall mag Ailpin,1119,1180,,gCais-Fathain")
    #_f("Earl Idwal ap Gruffydd of Perfeddwlad, 1054-1112, Seisyll")
    #_c("Meilys I ap Rhiwallon,1110,1165,Duke of Powys,gCais-Fathain")
    #_c("Flann nig Olav,1097,1161,Countess of Ui Mhaine,Vedrafjord")
    #_c("Bruatur mac Enguerrand,1108,1135,,gCais-Inis")
    #_c("Aed mac Domnall,1078,1147,Earl of Ennis,Neill Noigiallaich")
    #_c("Idwal ap Gruffydd,1054,1112,Earl of Perfeddwlad, Seisyll")
    #_c("Muirenn II nic Pierre,1275,,Duchess of Lancaster, Congalaigh")
    #_f("Duke Hlothere Muirennson of Kent, 1278-, Kiil")
    #_c("Ermessinde, 1264,,Duchess of East Anglia,Adelsward")
    #_c("Gruoch nic Glenn, 1273,,Duchess of Munster,Braenain")
    #_c("Hlothere Muirennson,1278,,Duke of Kent,Kiil")
    #_c("Eadbald Mael-Muireson,1286,,Duke of Poitou,hEochadha")
    #_f("Duke Brian Airmedachson of Burgundy, 1281-, gCais-Mathrafal")
    #_c("Brian Airmedachson,1281,,Duke of Burgundy,gCais-Mathrafal")
    #_c("Slaine nig Abban,1220,1282,,Briain")
    _f("Slaine nig Abban, 1220-1282, Briain")