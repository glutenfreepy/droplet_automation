import os


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
        if folder.endswith("-DONE"):
            print(f"skipping DONE folder {folder}")
            continue

        elif 'PSDCONVERT' in folder:
            print(f"converting {folder}")
            # set working folder path
            working_folder_path = f"{watch_folder_path}{folder}"

            print(f"the working folder path is: {working_folder_path}")

            files = os.listdir(working_folder_path)

            print(f"checking these files for pdfs: {files}")

            # run droplet to convert files to psd
            for file in files:
                if file.endswith(suffix):
                    filepath = f"{working_folder_path}/{file}"
                    # TODO: run droplet
                    print(f"running droplet on {filepath}")
                    # "open -a dropletpath filepath"

                else:
                    print(f"{file} was skipped since it is not a pdf.")

            # append "-DONE" to foldername
            print("appending '-DONE' to foldername")
            os.rename(working_folder_path, working_folder_path+"-DONE")

        else:
            print(f'skipped folder {folder} - no PSDCONVERT found')



watch_folder()
