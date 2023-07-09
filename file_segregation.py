import os
import shutil

from_directory = "C:/Users/Duvashi Family/Downloads"
to_directory = "C:/Users/Duvashi Family/Downloads/documents"

fileList = os.listdir(from_directory) 
#print(fileList)

for filename in fileList:
    name, extension = os.path.splitext(filename)
    #print(name)
    #print(extension)

    if extension == '': 
        continue

    if extension in [".docx", ".txt", ".doc", ".pdf"]:
        path1 = from_directory+'/'+filename
        path2 = to_directory+'/'+filename

        if os.path.exists(to_directory): 
            print("moving")
            shutil.move(path1,path2)

        else: 
            os.mkdirs(to_directory)
            print("moving")
            shutil.move(path1,path2) 


