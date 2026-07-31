import zipfile 
import os 

from google.colab import drive 
drive.mount('/content/drive') 
drive_path = "/content/drive/MyDrive/Stylie"


zips = [ #note that the names of drive and folders are different depending on what you named them
    "faceshapearchive.zip",
    "skintonearchive (2).zip",
    "hairtypearchive (1).zip"
]


for zip_file in zips:

    print("\n==========================") 
    print(zip_file)
    print("==========================")

    path = os.path.join(drive_path, zip_file)

    with zipfile.ZipFile(path, 'r') as z: 

        folders = set() 

        for name in z.namelist():

            parts = name.split("/") 

            if len(parts) > 1:
                folders.add(parts[1]) 

        print("Classes/folders:")
        print(folders)
