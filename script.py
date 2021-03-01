import os

path = '/fullpath/to/folder/with/pdfs' # define folder with pdfs to be processed
dropletpath = '/fullpathtodroplet'
suffix = 'pdf'
files = os.listdir(path) # get list of files in the folder
filepath = f'{path}{f}'

def run_droplet():
    for f in files:
        if filepath.endswith(suffix):
            open -a dropletpath filepath
        else:
            print("File skipped since it is not a pdf.")

def watch_folder():


    # get a list of folders
    watchfolder = "/path/to/watchfolder"
    folderlist = os.listdir(watchfolder)

    # get name of folder from list and see PSD-DONE folder exists
    pdffolder = folderlist

    # convert files

    # create new folder <foldername_PSD-DONE> and move psds to it
