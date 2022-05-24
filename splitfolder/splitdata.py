import os
from os import path
import shutil
import glob
from typing import List
import pathlib

root_folder = "/home/saplap/Giangnh/Unlabel"
copy_folder = [" ", "/home/saplap/Giangnh/tolabel/Giangcoi",
               "/home/saplap/Giangnh/tolabel/An",
               "/home/saplap/Giangnh/tolabel/Giangbeo",
               "/home/saplap/Giangnh/tolabel/Datden",
               "/home/saplap/Giangnh/tolabel/Datvang",
               "/home/saplap/Giangnh/tolabel/DuyTung",
               "/home/saplap/Giangnh/tolabel/Hieu",
               "/home/saplap/Giangnh/tolabel/HuyHoang",
               "/home/saplap/Giangnh/tolabel/GiaBinh",
               "/home/saplap/Giangnh/tolabel/TheHung",
               "/home/saplap/Giangnh/tolabel/KienHoang",
               "/home/saplap/Giangnh/tolabel/ThanhTra",
               "/home/saplap/Giangnh/tolabel/KhanhDuong",
               "/home/saplap/Giangnh/tolabel/DoKhai",
               "/home/saplap/Giangnh/tolabel/HuyTuan"]

# split into equal amount of images for each person

n = len(copy_folder) - 1
m = len(os.listdir(root_folder))
alpha = m/n
print(alpha)

i = 1   # i represents the index of each person in the copy_folder
# traverse through every image files in root_folder
for indx, label in enumerate(os.listdir(root_folder)):

    label_path = os.path.join(root_folder, label)
    # if index of the image not exceed the amount of images given to the user
    print(i)
    if (indx >= int(i*alpha)):
        i += 1
    if (indx < i*alpha):
        # if the folder storing data for the initital user exist
        if (os.path.exists(copy_folder[i])):
            try:
                new_file = copy_folder[i] + "/" + label
                f = pathlib.Path(new_file)
                f.touch()
                shutil.copyfile(label_path, new_file)
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
            except IsADirectoryError:
                print("Destination is a directory")
            except PermissionError:
                print("Permission denied.")
            except:
                print("Error occured while copying file.")
        else:
            os.mkdir(copy_folder[i])
            newfile = copy_folder[i] + "/" + label
            f = pathlib.Path(new_file)
            f.touch()
            shutil.copyfile(label_path, new_file)
