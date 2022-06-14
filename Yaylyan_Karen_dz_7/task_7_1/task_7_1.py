import os


def create_starter_project(project_structure, root=''):
    for dir_path, dir_name_lst in project_structure.items():
        dir_path_all = os.path.join(root, dir_path)
        if not os.path.exists(dir_path_all):
            os.mkdir(dir_path_all)
        for dir_name in dir_name_lst:
            if isinstance(dir_name, dict):
                create_starter_project(dir_name, dir_path_all)
            else:
                new_dir = os.path.join(dir_path_all, dir_name)
                if not os.path.exists(new_dir):
                    os.mkdir(new_dir)


project_structure = {
    'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']
}
create_starter_project(project_structure)
