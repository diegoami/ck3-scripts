import ck_people

import sys
import os

from find_best_dinasty import find_best_dinasty

if __name__ == "__main__":
    #s = sys.argv[1]
    #ck_people.add_person(s)
    #ck_people.add_person("Faelan mac Brian,1084,1136,High King of Ireland,Briain")
    #ck_people.add_person("Rhufon ap Gruffydd,1140,1166,Petty King of Deheubarth,Caerloyw-Penfro")
    #ck_people.add_person("Elisabet Gudrodsdatter,1083,1148,,Crovan")
    #find_best_dinasty("Elisabet Crovan")
    dir_mds = os.environ.get("CK_DIR")
    person_mds = os.path.join(dir_mds, 'p')
    #ck_people.add_person("Haer,1132,1197,,Brycheiniog")
    #find_best_dinasty(person_mds, "Haer Brycheiniog")
    #ck_people.add_person("Haraldr II,1125,1213,Duke of the Isles,Crovan")
    #find_best_dinasty(person_mds, "Duke Haraldr I")
    #ck_people.add_person("Cynddylan ap Gruffydd,1099,1154,Lord of Merionnydd,Caerloyw-Penfro")
    #find_best_dinasty(person_mds, "Lord Cynddylan" )
    #find_best_dinasty(person_mds, "Petty King Gruffydd III" )
    #ck_people.add_person("Sean mac Briain,1101,1135,Earl of Oriel,Briain")
    #ck_people.add_person("Cathan nic Briain,1078,1144,Countess of Ennis,Briain")
    # ck_people.add_person("Faelan mac Brian,1084,1136,High King of Ireland,Briain")
    #ck_people.add_person("Brian mac Murchad,1048,1111,High King of Munster,Briain")
    #find_best_dinasty(person_mds, "High King Murchad")
    # ck_people.add_person("Brian mac Murchad,1048,1111,High King of Munster,Briain")
    find_best_dinasty(person_mds, "Petty King Gruffydd I,")
    #ck_people.add_person("Donnchad mac Murchad,1068,1109,Earl of Ailech,Briain")
    #ck_people.add_person("Enguerrand mac Murchad,1081,1148,Duke of Ulster,gCais-Inis")
    #ck_people.add_person("Nest ferch Morien,1104,1172,Lady of Eryri,Caerloyw-Tyddewi")
    #ck_people.add_person("Meilys II ab Owain,1163,1181,Duke of Powys,Ynys-Cybi")
    #ck_people.add_person("Murchad mag Enguerrand,1102,1164,,gCais-Inis")
    #ck_people.add_person("Sean mac Cuanu,1139,1209,,Laighin")
    #ck_people.add_person("Cuanu mac Sean,1121,1152,Earl of Oriel,Laighin")
    #ck_people.add_person("Aelfmaer mag Osraed,1128,1167,Earl of Ui Mhaine,Hayles")
   # ck_people.add_person("Efyrddyl ferch Gruffydd,1124,1194,,Seisyll")
    #ck_people.add_person("Elen ferch Idwal,1092,1174,Lady of Penllyn,Seisyll")