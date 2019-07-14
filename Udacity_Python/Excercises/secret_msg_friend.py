import os

def rename_file():
    file_list = os.listdir(r"/Users/archananagaraja/Desktop/AN_Personal/Udacity_Python/alphabet_secret_msg")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory:" +saved_path)
    os.chdir(r"/Users/archananagaraja/Desktop/AN_Personal/Udacity_Python/alphabet_secret_msg")
    print(os.getcwd())
    for file_name in file_list:
        print("Old File Name: " +file_name)
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print("New File Name:" +file_name)
rename_file()