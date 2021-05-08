import ck_people

import sys
import os

from find_best_dinasty import find_best_dinasty

if __name__ == "__main__":
    #s = sys.argv[1]
    #ck_people.add_person(s)
    ck_people.add_person("Faelan mac Brian,1084,1136,High King of Ireland,Briain")
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
