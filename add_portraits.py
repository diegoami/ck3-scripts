import os

from find_references_history import find_references
from ck_people import get_ck_people
from file_parse import split_portrait_references
from people_walk import get_all_names


def add_portraits(dir_mds, ck_people, all_names):

    for ck_person in ck_people:
        full_file = os.path.join(dir_mds, ck_person.file_name)
        dir_name, file_extension = os.path.splitext(ck_person.file_name)
        dir_img = os.path.join(dir_mds, dir_name)
        if os.path.isdir(dir_img):
            before_lines, ref_lines, after_lines = split_portrait_references(full_file)
            write_lines = [] + before_lines

            write_lines.append('\n')
            write_lines.append("# PORTRAITS\n")
            write_lines.append("\n")

            for img_name in os.listdir(dir_img):
                img_year, img_ext =  os.path.splitext(img_name)
                write_lines.append("## {}\n".format(img_year))
                write_lines.append("![{}]({})\n\n".format(img_year, dir_name.split('/')[-1]+ '/' +img_name))

            write_lines.append("#### END PORTRAITS\n")
            write_lines.append("\n")
            write_lines += after_lines
            with open(full_file, 'w') as f:
                f.writelines(write_lines)

if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")

    ck_people = get_ck_people()
    ppl_file = os.path.join(dir_mds, 'people.md')
    all_names = get_all_names(dir_mds, ppl_file, ck_people)

    add_portraits(dir_mds, ck_people, all_names)