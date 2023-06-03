import shutil
import os
import subprocess
from datetime import datetime

def remove_folder(path):
    shutil.rmtree(path)
    print(f"Папку уебал")

def copy_folder(source, destination):
    shutil.copytree(source, destination)
    print(f"Потом ебать перекинул новую версию")

def backup_folder(source, destination):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = os.path.basename(source)
    backup_folder_name = f"{folder_name}_{timestamp}"
    backup_folder_path = os.path.join(destination, backup_folder_name)
    shutil.copytree(source, backup_folder_path)
    print(f"Ебнул бэкап")

def run_batch_file(file_path):
    subprocess.call(file_path, shell=True)
    print(f"Запускаю Родину")

folder_to_remove = 'C:/Users/nikitabogdanov/Desktop/rodina/frontend'
folder_to_copy = 'C:/Users/nikitabogdanov/Desktop/Rodina-frontend/frontend'
destination_folder = 'C:/Users/nikitabogdanov/Desktop/rodina'
backup_folder = 'C:/Users/nikitabogdanov/Desktop/Rodina-frontend/backup'
batch_file_path = 'C:/Users/nikitabogdanov/Desktop/asd.bat'

run_batch_file(batch_file_path)
remove_folder(folder_to_remove)
copy_folder(folder_to_copy, destination_folder)
backup_folder(folder_to_copy, backup_folder)
