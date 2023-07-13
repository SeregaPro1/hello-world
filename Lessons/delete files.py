import os
import shutil

path = 'D:\\test2.txt'

try:
    os.remove(path) #delete a file
    os.rmdir(path) #delete a file or empy folder
    shutil.rmtree(path) # dele files and or folders
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('You do not have permission to delete that function')
except OSError:
    print('That folder contains files')
else:
    print(path+" was deleted")