import sys


def find_family_tree(full_file):
    olines, plines, alines = [], [], []
    with open(full_file, 'r', encoding='latin1') as f:
        in_family_tree = 0
        for i, line in enumerate(f.readlines()):

            if "FAMILY TREE" in line:
                in_family_tree = 1
                continue
            if "`" in line and in_family_tree == 1:
                in_family_tree = 2
                continue

            if in_family_tree == 2:
                if "`" in line:
                    in_family_tree = 3
                    continue
                else:
                    olines.append(line.rstrip())

            if in_family_tree == 0:
                plines.append(line)

            if in_family_tree == 3:
                alines.append(line)

        if not olines or in_family_tree != 3:
            print("{} is invalid".format(full_file))
            sys.exit(1)
    return olines, plines, alines


def split_file_references(full_file):
    before_lines, ref_lines, after_lines = [], [], []
    with open(full_file, 'r', encoding='latin1') as f:
       
        all_lines = f.readlines()
        empty_lines = 0
        in_reference = 0
        for all_line in all_lines:
            if "ANCESTORS" in all_line or "REFERENCES" in all_line or all_line.startswith("* "):
                in_reference = 1
                continue
            elif "END REFERENCES" in all_line:
                in_reference = 2
                continue
            elif in_reference == 0 and len(all_line.strip()) == 0:
                empty_lines += 1
                if empty_lines <= 1:
                    before_lines.append(all_line)
            elif in_reference == 0:
                empty_lines = 0
                before_lines.append(all_line)
            elif in_reference == 1:
                ref_lines.append(all_line)
            elif in_reference == 2 and not "END REFERENCES" in all_line :
                after_lines.append(all_line)
    return before_lines, ref_lines, after_lines


def split_file_relatives(full_file):
    before_lines, ref_lines, after_lines = [], [], []
    with open(full_file, 'r', encoding='latin1') as f:

        all_lines = f.readlines()
        empty_lines = 0
        in_reference = 0
        for all_line in all_lines:
            if "RELATIVES" in all_line:
                in_reference = 1
                continue
            elif "END RELATIVES" in all_line:
                in_reference = 2
                continue
            elif in_reference == 0 and len(all_line.strip()) == 0:
                empty_lines += 1
                if empty_lines <= 1:
                    before_lines.append(all_line)
            elif in_reference == 0:
                empty_lines = 0
                before_lines.append(all_line)
            elif in_reference == 1:
                ref_lines.append(all_line)
            elif in_reference == 2 and not "END RELATIVES" in all_line:
                after_lines.append(all_line)
    return before_lines, ref_lines, after_lines


def split_portrait_references(full_file):
    before_lines, ref_lines, after_lines = [], [], []
    with open(full_file, 'r', encoding='latin1') as f:

        all_lines = f.readlines()
        empty_lines = 0
        in_portraits = 0
        for all_line in all_lines:
            if "PORTRAITS" in all_line:
                in_portraits = 1
                continue
            elif "END PORTRAIS" in all_line:
                in_portraits = 2
                continue
            elif in_portraits == 0 and len(all_line.strip()) == 0:
                empty_lines += 1
                if empty_lines <= 1:
                    before_lines.append(all_line)
            elif in_portraits == 0:
                empty_lines = 0
                before_lines.append(all_line)
            elif in_portraits == 1:
                ref_lines.append(all_line)
            elif in_portraits == 2 and not "END PORTRAITS" in all_line:
                after_lines.append(all_line)
    return before_lines, ref_lines, after_lines
