
import os
import shutil


def copy_files_recursive(source_dir, dest_dir):

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir, exist_ok=True)

    _copy_recursive(source_dir, dest_dir)


def _copy_recursive(src, dst):

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isdir(src_path):
            os.makedirs(dst_path, exist_ok=True)
            _copy_recursive(src_path, dst_path)
        else:
            shutil.copy2(src_path, dst_path)
            print(f"Copied file: {src_path} -> {dst_path}")