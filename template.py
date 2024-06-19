import os
import pathlib
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s] : %(message)s :')

project_name = 'skim-lit'

list_of_files = [
    ".github/workflows/.gatekeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utrils/__init__.py",
    f"src/{project_name}/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for file_path in list_of_files:
    file_path = pathlib.Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"directory created: {file_dir} for file: {file_name} ")
    
    if (not file_path.exists()) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as file:
            pass
        logging.error(f"creating an empty file: {file_path}")
        
    else:
        logging.info(f"file already exists: {file_name}")
