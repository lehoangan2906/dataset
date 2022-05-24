import os.path
from os import path
import shutil
import glob

root_folder = "/home/saplap/Giangnh/Unlabel"
copy_folder = ["home/saplap/Giangnh/tolabel/Giangcoi", "home/saplap/Giangnh/tolabel/An", "home/saplap/Giangnh/tolabel/Giangbeo", "home/saplap/Giangnh/tolabel/Datden"
        , "home/saplap/Giangnh/tolabel/Datvang" ,"home/saplap/Giangnh/tolabel/DuyTung", "home/saplap/Giangnh/tolabel/Hieu", "home/saplap/Giangnh/tolabel/HuyHoang", "home/saplap/Giangnh/tolabel/HoangSon"
        , "home/saplap/Giangnh/tolabel/GiaBinh", "home/saplap/Giangnh/tolabel/TheHung", "home/saplap/Giangnh/tolabel/KienHoang", "home/saplap/Giangnh/tolabel/ThanhTra", "home/saplap/Giangnh/tolabel/KhanhDuong",
        "home/saplap/Giangnh/tolabel/DoKhai", "home/saplap/Giangnh/tolabel/huytuan"]

# split into equal amount of images for each person
m = len(root_folder)
n = len(copy_folder) - 1
alpha = m/n
i = 0
# traverse through every image files in root_folder
for indx, label in enumerate(root_folder):
     # i represents the index of each person in the copy_folder
    
    # if index of the image not exceed the amount of images given to the user
    if (indx < i*alpha):
        
        # if the folder storing data for the initital user exist 
        if (path.exists(copy_folder[i])):
            try:
                # copy the image to the folder
                shutil.copyfile(label, copy_folder[i])
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
            except IsADirectoryError:
                print("Destination is a directory")
            except PermissionError:
                print("Permission denied.")
            except:
                print("Error occured while copying file.")
    else:
        # index of the image exceed the limit of the initial user,
        # proceed to the next user
        i += 1
