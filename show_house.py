import os
from ck_people import get_ck_people, write_houses


if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")
    people_mds = os.path.join(dir_mds, 'p')
    ck_people = get_ck_people()
    houses = write_houses(ck_people)
    file_houses = os.path.join(dir_mds, 'houses.md')
    with open(file_houses, 'w') as f:
        f.write("# HOUSES\n")
        house_keys = sorted(houses.keys(), key=lambda x: x.lower())
        for house_key in house_keys:
            f.write("\n## {}\n".format(house_key))
            for person, file in houses[house_key]:
                f.write("- [{}]({})\n".format(person, file))