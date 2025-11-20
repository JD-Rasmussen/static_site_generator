
import os
import shutil


def copy_files_recursive(source_dir, dest_dir):

    if not os.path.exists(source_dir):
        raise Exception "source directory invalid"

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)





