import os


def create_starter_project(project_structure, root=''):
    for dir_path, dir_name_lst in project_structure.items():
        dir_path_all = os.path.join(root, dir_path)
        if not os.path.exists(dir_path_all):
            if '.' in dir_path_all:
                os.mknod(dir_path_all)
            else:
                os.mkdir(dir_path_all)
        for dir_name in dir_name_lst:
            if isinstance(dir_name, dict):
                create_starter_project(dir_name, dir_path_all)
            else:
                new_dir = os.path.join(dir_path_all, dir_name)
                if not os.path.exists(new_dir):
                    if '.' in new_dir:
                        os.mknod(new_dir)
                    else:
                        os.mkdir(new_dir)


def project_create(config):
    def parser(config, i=0, deep=0):
        lst = []
        while i < len(config):
            inx_defice = config[i].find('-')
            new_deep = config[i][:inx_defice].count(' ')
            if new_deep == deep:
                file_name = config[i].strip().split()[-1]
                lst.append(file_name)
            elif new_deep > deep:
                new_value, step = parser(config, i, new_deep)
                lst.pop()
                file_name = config[i-1].strip().split()[-1][:-1]
                lst.append({file_name: new_value})
                i = step
                continue
            else:
                return lst, i
            i += 1
        return lst, i
    project, *_ = parser(config)
    return project[0]


with open('config.yaml', encoding='utf-8') as f:
    config = f.readlines()

project = project_create(config)
create_starter_project(project)
