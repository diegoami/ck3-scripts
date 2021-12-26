import os
from lib.people_walk import check_photos
from lib.people_walk import get_all_names
import sys

if __name__ == "__main__":
    dir_mds = os.environ.get("CK_DIR")
    all_names = get_all_names(dir_mds)
    s = sys.argv[1]
    check_photos(int(s), all_names, dir_mds)