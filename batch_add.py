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

    dir_mds = os.environ.get("CK_DIR")
    person_mds = os.path.join(dir_mds, 'p')
    #find_best_dinasty(person_mds, "Gruffydd Caerloyw-Penfro")
    #ck_people.add_person("Clydog ap Talorc,1227,,Lord of Ynys Mon,Ruairc")
    #ck_people.add_person("Elen ferch Idwal,1092,1174,Lady of Penllyn,Seisyll")

    #ck_people.add_person("Baethine Dubhson,1205,,King of England,Briain")
   # ck_people.add_person("Martha Kyle,1210,,,Kyle")
    find_best_dinasty(person_mds, "Slebine Briain")
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
