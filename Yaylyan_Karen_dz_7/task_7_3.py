import os
import shutil

root_dir = 'my_project'
dst_dir = os.path.join(root_dir, 'templates')
if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)

for root, dirs, files in os.walk(root_dir):
    if root != dst_dir and os.path.basename(root) == 'templates':
        for r, d, f in os.walk(root):
            for directory in d:
                rel_path_directory = os.path.relpath(os.path.join(r, directory), root)
                os.makedirs(os.path.join(dst_dir, rel_path_directory), exist_ok=True)

            for file in f:
                src_dir_file = os.path.join(r, file)
                rel_path_file = os.path.relpath(src_dir_file, root)
                dst_dir_file = os.path.join(dst_dir, rel_path_file)
                shutil.copy(src_dir_file, dst_dir_file)
