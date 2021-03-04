import os
import re

watch_folder_path = './testwatchfolder/'
#working_folder_path = '/fullpath/to/folder/with/pdfs' # define folder with pdfs to be processed
folder_list = os.listdir(watch_folder_path) # get list of files in the folder
#dropletpath = '/fullpathtodroplet'
#filepath = f'{working_folder_path}{f}'
suffix = 'pdf'


def watch_folder():
    print()
    print(f"the watch folder is set to {watch_folder_path}")
    print()
    print(f"i see these folders in the watch folder: {folder_list}")
    print()
    for folder in folder_list:
        if 'PSDCONVERT' in folder:
            print(folder)
            # TODO: set working folder path
            working_folder_path = f"{watch_folder_path}{folder}"
            print(f"the working folder path is: {working_folder_path}")
            # TODO: convert files
            # TODO: rename folder to PSDCOMPLETE
            os.rename(working_folder_path, working_folder_path+"-DONE")
        else:
            print('skipped')


"""

        pdffolder = folderlist

    # convert files

      
def run_droplet():
    for f in files:
        if filepath.endswith(suffix):
            open -a dropletpath filepath
        else:
            print("File skipped since it is not a pdf.")
"""

watch_folder()
