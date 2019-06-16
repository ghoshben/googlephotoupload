import threading
import os


def videolist(sd):
    my_list = []
    for file in os.listdir(sd):
        if file.endswith(".mkv"):
            name = (os.path.join(series_directory, file))
            my_list.append(name)
            # threading.Thread(os.system("upload-gphotos "+name+" -c a.json")).start()
    return my_list


def upload(name):
    os.system("upload-gphotos " + name + " -c a.json")


upload_type = input("enter the you want to upload movie[m] or series[s]")
if upload_type == 'm':
    input("enter the file name[with directory]")
if upload_type == 's':
    series_directory = input("enter the folder directory")
    filenames = videolist(series_directory)
    for fname in filenames:
        t = threading.Thread(target=upload, args=(fname,)).start()
