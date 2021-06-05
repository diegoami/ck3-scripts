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
    #_f("Slaine nig Abban, 1220-1282, Briain")
    #_c("Mathieu,1220,,Duke of Orleans,Antoing")
    #_c("Inwaer Stephaniason,1295,,Duke of Wessex,Briain")
    #_f("Duke Inwaer Stephaniason of Wessex, 1295-, Briain")
    #_c("Wulfgar,1282,,Duke of Berry,Randolph")
    #_c("Alienora,1275,,Duke of Normandy,Corbeil")
    #_f("Duke Alienora of Normandy, 1275-, Corbeil")
    #_c("Fuacarta,1283,,Duke of Anjou,gCais-Sherwood")
    #_f("Duke Fuacarta of Anjou, 1283-, gCais-Sherwood")
    #_c("Sverrir Drifason,1272,,Duke of Champagne,Hagalin")
    #_f("Duke Sverrir Drifason of Champagne, 1272-, Hagalin")
    #_c("Natfraich,1280,,Duke of Bar,Cathasaigh")
    #_f("Duke Natfraich of Bar, 1280-, Cathasaigh")
    #_c("Seoan,1261,,Count of Guines,Briain")
    #_f("Count Seoan of Guines, 1261-, Briain")
    #_c("Gerroc Airmedachdohtor,1289,,Countess of Clermont,gCais-Mathrafal")
    #_f("Countess Gerroc Airmedachdohtor of Clermont, 1289-, gCais-Mathrafal")
    #_f("Countess Gerroc Airmedachdohtor of Clermont, 1289-, gCais-Mathrafal")
    #_c("Coblaith nic Cairech,1277,,Count of Vermandois,gCais-Trefynwy")
    #_f("Count Coblaith nic Cairech of Vermandois, 1277-, gCais-Trefynwy")
    #_c("Erc mac Cathan,1264,,Duke of Cornwall,Briain")
    #_f("Duke Erc mac Cathan of Cornwall, 1264-, Briain")
    #_c("Morag,1274,,Countess of Dunbar,Briain")
    #_f("Countess Morag of Dunbar, 1274-, Briain")
    #_c("Swietoslawa,1259,,Countess of Amiens,Olesnicy")
    #_f("Countess Swietoslawa of Amiens, 1259-, Olesnicy")
    #_c("Cenwulf,1309,,Earl of Valois,Senlis")
    #_c("Mauda nic Cairech,1255,,Petty Queen of Deheubarth,Briain")
    #_f("Duke Muirchertach mac Cairech of Gwynedd, 1272-, Briain")
    #_c("Muirchertach mac Cairech,1272,,Duke of Gwynedd,Briain")
    #_c("Cathan Cathandohtor,1270,,Duchess of Gwynedd,Briain")
    #_c("Cathan Cathandohtor,1247,1308,Duchess of Cornwall,Briain")

    #_f("Duchess Cathan Cathandohtor of Gwynedd, 1270-, Briain")
    #_c("Sybilla,1248,,Court Chaplain,Clare")
    #_f("Court Chaplain Sybilla, 1248-, Clare")
    #_c("Cynehelm Ben-Uladson,1270,,Earl of Lindsey,Briain")
    #_c("Ben-Mide,1282,,Countess of Chartres,gCais-Mathrafal")
    #_f("Countess Ben-Mide of Chartres, 1282-, gCais-Mathrafal")
    #_c("Aethelberht Tailefhlaithson,1274,,Earl of Buccingahamm,Got")
    #_f("Earl Aethelberht Tailefhlaithson of Buccingahamm, 1274-, Got")
    #_c("Eysteinn Lethlobursson,1271,,Earl of Northumberland,Braghde")
    #_f("Earl Eysteinn Lethlobursson of Northumberland, 1271-, Braghde")
    #_c("Kjartan,1274,,Earl of Angus,Braghde")
    #_c("Aethelburg Giseledohtor,1283,,Countess of Worcestershire,Kiil")
    #_f("Countess Aethelburg Giseledohtor of Worcestershire, 1283-, Kiil")
    #_c("Coscrach Wulfwynnson,1290,,Earl of Herefordshire,Llewellyn")
    #_c("Wulfgifu Ermessindedohtor,1282,,Countess of South Seaxe,Briain")
    #_f("Countess Wulfgifu Ermessindedohtor of South Seaxe, 1282-, Briain")
    #_c("Beorhtwynn,1265,,Countess of Lusignan,Dall")
    #_c("Eithne Slainedohtor,1285,,Countess of Chalon,gCais-Mathrafal")
    #_f("Countess Eithne Slainedohtor of Chalon, 1285-, gCais-Mathrafal")
    #_c("Aelfstan Aedson,1279,,Earl of Macon,Got")
    #_f("Earl Aelfstan Aedson of Macon, 1279-, Got")
    #_c("Aelfthryth,1275,,Countess of Nevers,Hayles")
    #_c("Aelfthryth,1275,,Countess of Nevers,Hayles")
    #_c("Wulfrun,1282,,Countess of Avalois,Pudsey")
    #_c("Scule Stephaniason,1302,,Earl of Wight,Briain")
    #_c("Wulfgar,1282,,Duke of Berry,Randolph")
    #_c("Comgan mag Aine,1302,,Count of Issoudun,gCais-Berkhamsted")
    #_f("Count Comgan mag Aine of Issoudun, 1302-, gCais-Berkhamsted")
    _c("Dimmasach mag Aine,1218,1279,,gCais-Berkhamsted")
