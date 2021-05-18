import ck_people

import sys
import os
from functools import partial

from find_best_dinasty import find_best_dinasty

if __name__ == "__main__":


    dir_mds = os.environ.get("CK_DIR")
    person_mds = os.path.join(dir_mds, 'p')
    _c = ck_people.add_person
    def _f(s):
        return find_best_dinasty(person_mds, s)
    #_c("Hunydd ferch Bleddyn,1042,1099,,Mathrafal")
    _f("Hunydd")
    #find_best_dinasty(person_mds, "Gruffydd Caerloyw-Penfro")
    #ck_people.add_person("Clydog ap Talorc,1227,,Lord of Ynys Mon,Ruairc")
    #ck_people.add_person("Elen ferch Idwal,1092,1174,Lady of Penllyn,Seisyll")

    #ck_people.add_person("Baethine Dubhson,1205,,King of England,Briain")
   # ck_people.add_person("Martha Kyle,1210,,,Kyle")
    #find_best_dinasty(person_mds, "Duke Aengus I")
    #find_best_dinasty(person_mds, "Duchess Rhiandrech")
    #find_best_dinasty(person_mds, "Duke Owain II")
    #find_best_dinasty(person_mds, "Agata de Lacon")
    #ck_people.add_person("Eithne nic Baethine,1238,,Princess of England,Briain")
    #ck_people.add_person("Maccus Baethineson,1273,,Prince of England,Briain")
    #ck_people.add_person("Stephanie Baethinedohtor,1276,,Princess of England,Briain")
    #ck_people.add_person("Morien nic Lorcan,1221,,Princess of England,Briain")
    #ck_people.add_person("Rois nic Lorcan,1225,,Princess of England,Briain")
    #ck_people.add_person("Rodan mac Narbflaith,1263,,Prince of England,Briain")
    #ck_people.add_person("Gormflaith Abeldohtor,1211,1274,Princess of Ireland,Briain")
    #ck_people.add_person("Caintigern Abeldohtor,1215,-,Princess of Ireland,Briain")
    #ck_people.add_person("Cathan Abeldohtor,1218,-,Princess of Ireland,Briain")
    #ck_people.add_person("Cathalan mag Abel,1220,1242,Princess of Ireland,Briain")
    #ck_people.add_person("Dubh mac Somhairle,1183,1234,,Briain")
    #ck_people.add_person("Tadg Barrdubson,1257,,Duke of Deira,Got")
    #find_best_dinasty(person_mds, "Aed Got")
    #find_best_dinasty(person_mds, "Tailefhlaith Got")
    #find_best_dinasty(person_mds, "Earl Eoganan")
    #find_best_dinasty(person_mds, "Countess Sioban")
    #ck_people.add_person("Morien,1226,,Duchess of Lancaster,gClais-Macclesfield")
    #ck_people.add_person("Scellan,1255,,Duke of Hwicce,Briain")
    #find_best_dinasty(person_mds, "Earl Fuacarta")
    # ck_people.add_person("Muirenn Gelgeisdohtor,1245,,Duchess of Leinster,Briain")
    #find_best_dinasty(person_mds, "Duchess Slaine")
    find_best_dinasty(person_mds, "Hunydd")
    #ck_people.add_person("Pierre mac Muirenn,1256,,Duke of Ulster,gCais-Macclesfield")
    #ck_people.add_person("Farannan,1239,,Duke of Munster, gCais-Mathrafal")
    #ck_people.add_person("Aed Barrdubson,1261,,Earl of West Riding, Got")
    #ck_people.add_person("Flanchad,1231,,Earl of Lincolnshire, Michael")
    #ck_people.add_person("Tailefhlaith Barrdubdohtor,1252,,Countess of Breifne, Got")
    #ck_people.add_person("Muirenn I nic Gilla-Ruad,1165,1230,, gCais-Cruachu")
    #ck_people.add_person("David,1231,,Earl of Berkshire,Clare")
    #ck_people.add_person("Cairech nic Faelchu,1235,,Duchess of Deheubarth,Briain")
    #ck_people.add_person("Glenn mac Mael-Ruanaid,1242,,Earl of Desmond,Braenain")
    ##ck_people.add_person("Humbert mac Muirenn,1258,,Earl of Oriel,gCais-Macclesfield")
    #ck_people.add_person("William,1247,,Duke of Guoladat,Sigurdr-York")
    #ck_people.add_person("Etain nig Aindle,1267,,Lady of Brycheniog,Briain")
    #ck_people.add_person("Hywela ferch LLes,1242,,Lady of Merionnydd,Ynys Cybi")
    #ck_people.add_person("Elidyr ab Iorwerth,1085,1150,,Caerloyw-Tyddewi")
