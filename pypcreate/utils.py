import yaml
import os
import re

def load_yaml(file, opt=None):
    """
    Load yaml file and return a dictionary.

    Parameters
    ----------
    file : string
        yaml file path.

    opt : argparser
         Argparser.
    Returns
    -------
    param : dict
        A dictionary that contains defined parameters.
    """
    if opt and opt.model_dir:
        file = os.path.join(opt.model_dir, 'config.yaml')

    stream = open(file, 'r')
    loader = yaml.Loader
    loader.add_implicit_resolver(
        u'tag:yaml.org,2002:float',
        re.compile(u'''^(?:
         [-+]?(?:[0-9][0-9_]*)\\.[0-9_]*(?:[eE][-+]?[0-9]+)?
        |[-+]?(?:[0-9][0-9_]*)(?:[eE][-+]?[0-9]+)
        |\\.[0-9_]+(?:[eE][-+][0-9]+)?
        |[-+]?[0-9][0-9_]*(?::[0-5]?[0-9])+\\.[0-9_]*
        |[-+]?\\.(?:inf|Inf|INF)
        |\\.(?:nan|NaN|NAN))$''', re.X),
        list(u'-+0123456789.'))
    param = yaml.load(stream, Loader=loader)
    if "yaml_parser" in param:
        param = eval(param["yaml_parser"])(param)

    return param

def create_files(folder,files):
    for i in files:
        file_path = os.path.join(folder,i)
        create_a_file(file_path)

def create_a_file(file_path):
    if not os.path.exists(file_path):
        open(file_path, "x")
    else:
        print(file_path," already exists.")

def mk_subdir(directory,parent_path):
    dir_key = list(directory.keys())
    for item in dir_key:
        if item == 'dir_name':  
            dir_name = directory['dir_name']
            mkdir(dir_name)
        elif item == 'files':
            create_files(dir_name,directory['files'])
        else:
            if parent_path == 'root':
                mk_subdir(directory[item],'None')   
            else:
                directory[item]['dir_name'] = os.path.join(dir_name,directory[item]['dir_name'])
                mk_subdir(directory[item],dir_name) 