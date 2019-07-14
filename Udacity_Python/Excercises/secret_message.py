import os

def rename_files():
    #(1)get file names from a folder
    file_list = os.listdir(r"/Users/archananagaraja/Desktop/AN_Personal/Udacity_Python/alphabet")
    print(file_list)
    current_dir = os.getcwd()
    print("My current directory is: "+current_dir)
    os.chdir(r"/Users/archananagaraja/Desktop/AN_Personal/Udacity_Python/prank")
    #(2) for each file rename filename
    for file_name in file_list:
        print("Old File Name: " +file_name)
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print("New File Name:" +file_name)
    os.chdir(current_dir)
rename_files()