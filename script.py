import os
from time import sleep

#dropletpath = '/fullpathtodroplet'
watch_folder_path = './testwatchfolder/'
folder_list = os.listdir(watch_folder_path) # get list of files in the folder
suffix = 'pdf'


def watch_folder():
    print(f"watch folder location: {watch_folder_path}")
    print(f"folders in the watch folder: {folder_list}")
    print()

    for folder in folder_list:
        if folder.endswith("-DONE"):
            print(f"skipped '{folder}' - already labeled '-DONE'")
            continue

        elif 'PSDCONVERT' in folder:
            sleep(1)
            print()
            print(f"converting {folder}")
            # set working folder path
            working_folder_path = f"{watch_folder_path}{folder}"

            files = os.listdir(working_folder_path)

            # print()
            print(f"checking these files for pdfs: {files}")
            # run droplet to convert files to psd
            for file in files:
                sleep(1)
                print()
                if file.endswith(suffix):
                    filepath = f"{working_folder_path}/{file}"
                    print(f"running droplet on {filepath}")
                    # TODO: run droplet with subprocess
                    # "open -a dropletpath filepath"

                else:
                    print(f"{file} skipped - not a pdf file.")

            # append "-DONE" to foldername
            print()
            print("appending '-DONE' to foldername")
            os.rename(working_folder_path, working_folder_path+"-DONE")
            # TODO: print all output to a log file, delete pdfs

        else:
            # print()
            print(f"skipped '{folder}' - no PSDCONVERT found")


if __name__ == "__main__":
    watch_folder()
