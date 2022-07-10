# PyPCreate

Pypcreate is a easy to use Python package creation tool.

## Installation

```shell
pip install pypcreate

# to upgrade 
pip install --upgrade pypcreate
```

## Usage

### 1 mkdir

To create a directory with empty`__init__.py` and `README.md` :

```shell
pypcreate --mkdir directory_name
```

### 2 yamlmkdir

To create a set up directories from a yaml file:

```shell
pycreate --yamlmkdir yamlname.yaml
```

The format of yaml file should follow the following format:

```yaml
name: example

root:
  dir_1:
    dir_name: 'example1' # directory name
    files: ['__init__.py','README.md','example.py'] # specify the empty files in the directory 
    dir_1: 
      dir_name: 'sub_example1' # directory name
      files: ['hello.py'] 

  dir_2:
    dir_name: 'example2' # here is the name of directory 2 
    files: ['__init__.py'] 
```

Notes:

- You must specify root
- For the sub-folder, you need to start with `dir_1` variable
- For the directory name, the variable name should be `dir_name`
- For creating files, the variable name should be `files`

