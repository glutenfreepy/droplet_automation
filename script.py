import os

path = '/fullpath/to/folder/with/pdfs' # define folder with pdfs to be processed
dropletpath = '/fullpathtodroplet'
suffix = 'pdf'
files = os.listdir(path) # get list of files in the folder
filepath = f'{path}{f}'

for f in files:
    if filepath.endswith(suffix):
        open -a dropletpath filepath
    else:
        print("File skipped since it is not a pdf.")