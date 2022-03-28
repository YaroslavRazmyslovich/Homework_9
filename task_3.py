from pathlib import Path
from random import randint
from loguru import logger
import os
import shutil


logger.add ('logs.log', format = '{time} {level} {message}', level = 'DEBUG')
try:
    dir_path = 'directory'
    shutil.rmtree(dir_path)
    logger.info ('delete old directory')
except FileNotFoundError:
    logger.debug ('папка \'directory\' не существует, удалять нечего')
Path ('directory').mkdir (exist_ok = True)
for i in range (15):
    Path ( f'directory/'
        f'{randint (2020,2022)}-'
        f'{randint (1,12)}-'
        f'{randint (1,31)}.txt').touch ()
logger.info ('added new directory')
@logger.catch
def name_folder ():
    logger.info ('start function')
    path = '.\directory'
    list_of_files = list(sorted(os.listdir(path)))
    for file in list_of_files:
        fold_1 = (file.split('-')[0])
        fold_2 = (file.split('-')[1])
        fl = (file.split('-')[2])
        Path (f'directory/{fold_1}/{fold_2}/').mkdir(parents=True, exist_ok=True)
        path_1 = f'.\directory/{file}'
        path_2 = f'.\directory/{fold_1}/{fold_2}/{fl}/'
        os.replace(path_1, path_2)
        logger.info (f'added /{fold_1}/{fold_2}/{fl}')
    logger.info ('finish function')

name_folder ()



