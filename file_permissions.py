#This program modifies file permission based on user Input 
# Takes file name from User and search for it in the current working directory



import os,stat

file_name = input("Enter file name to modify permissions : ")
current_directory=os.getcwd()
file_path = current_directory+"/"+file_name

read, write, execute = input("Enter y or n for read & write & execute : ").split()

if read == 'y' and write == 'n' and execute == 'n':
    os.chmod(file_path, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH )
    print("Successfully updated Read permissions for all users ")

if read == 'y' and write == 'y' and execute == 'n':
    os.chmod(file_path, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH | stat.S_IWRITE | stat.S_IWGRP | stat.S_IWOTH)
    print("Successfully updated Read and Write permissions for all users")

if read == 'y' and write == 'y' and execute == 'y':
    os.chmod(file_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    print("Successfully updated Read, Write & Execute for all users")

if read == 'n' and write == 'n' and execute == 'y':
    os.chmod(file_path, stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
    print("Successfully updated Execution permission for all users")

if read == 'n' and write == 'y' and execute == 'n':
    os.chmod(file_path, stat.S_IWRITE | stat.S_IWGRP | stat.S_IWOTH)
    print("Successfully updated Write permission for all users")

if read == 'n' and write == 'y' and execute == 'y':
    os.chmod(file_path, stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
    print("Successfully updated Write, Execute for all users")
