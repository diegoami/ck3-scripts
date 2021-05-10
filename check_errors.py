import os
from collections import defaultdict
from find_references_history import find_references
from ck_people import get_ck_people
from file_parse import find_family_tree, split_file_references
from people_walk import get_all_names


if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")
    history_mds = os.path.join(dir_mds, 'h')
    history_references = find_references(history_mds)
    ck_people = get_ck_people()
    ppl_file = os.path.join(dir_mds, 'people.md')
    all_names = get_all_names(dir_mds, ppl_file, ck_people)

    for ck_person in ck_people:
        full_file = os.path.join(dir_mds, ck_person.file_name)
        before_lines, ref_lines, after_lines = split_file_references(full_file)
        write_lines = [] + before_lines

        write_lines.append('\n')
        write_lines.append("# REFERENCES\n")
        write_lines.append("\n")

        write_lines.append("## ANCESTORS\n")
        for short_name in all_names["short_names_in_file"][ck_person.file_name]:

            if short_name in all_names["short_name_to_long_name"]:
                long_name = all_names["short_name_to_long_name"][short_name]
                file_l_name = all_names["long_name_to_file"][long_name].split('/')[1]
                write_lines.append("* [{}]({})\n".format(long_name, file_l_name))
        write_lines.append("\n")
        write_lines.append("## HISTORY")
        write_lines.append("\n")
        if ck_person.file_name in history_references:
            for history_name in sorted(history_references[ck_person.file_name]):
                write_lines.append("* [{}](../h/{})\n".format(history_name, history_name))
        write_lines.append("\n#### END REFERENCES\n")
        write_lines += after_lines
        with open(full_file, 'w') as f:
            f.writelines(write_lines)