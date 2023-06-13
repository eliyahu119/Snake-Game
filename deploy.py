import zipfile
import os

def create_zip(files, folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                zipf.write(file_path, arcname=file)

# Example usage
files =['apple.py', 'board.py', 'snake.py', 'snake_game.py', 'snake_main.py', 'snake_types.py',
  'utils.py', 'wall.py',"AUTHORS"]
# Example usage
current_folder = os.getcwd()  # Get the current working directory
zip_name = os.path.join(current_folder, 'archive.zip')

create_zip(files, current_folder, zip_name)
