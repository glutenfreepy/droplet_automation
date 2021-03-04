import os
import re

watch_folder_path = './testwatchfolder/'
folder_list = os.listdir(watch_folder_path) # get list of files in the folder
#dropletpath = '/fullpathtodroplet'
suffix = 'pdf'


def watch_folder():
    print()
    print(f"the watch folder is set to {watch_folder_path}")
    print()
    print(f"i see these folders in the watch folder: {folder_list}")
    print()
    for folder in folder_list:
        if 'PSDCONVERT' in folder: # TODO: add logic to look for endswith -DONE
            print(folder)
            # set working folder path
            working_folder_path = f"{watch_folder_path}{folder}"
            print(f"the working folder path is: {working_folder_path}")

            # convert files
            run_droplet(working_folder_path)

            # TODO: rename folder with foldername-DONE
            os.rename(working_folder_path, working_folder_path+"-DONE")
        else:
            print('skipped')


def run_droplet(pdffolder):
    for f in pdffolder:
        if f.endswith(suffix):
            filepath = f"{pdffolder}{f}"
            print(filepath)
            # TODO: rn droplet
            # "open -a dropletpath filepath"
        else:
            print("File skipped since it is not a pdf.")


watch_folder()
