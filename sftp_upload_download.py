### This notebook moves files from SFTP to Azure Blob Storage to Blob Storage by taking user input to go back in dates and pull all the files based on Last modified date on server

### can be used to download either to local or Blob or S3 if mounted

import pysftp
import json 
import warnings
from datetime import datetime, timedelta

%md Widgets
# Read file storage path from Widgets 
dbutils.widgets.removeAll()

date_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
dbutils.widgets.text("remote_dir", "", label = "1. Remote Directory ") 
dbutils.widgets.text("blob_dir", "", label = "2. Blob Directory")
dbutils.widgets.dropdown("days_back",  defaultValue ='1', label = "3. Days Back", choices = date_list)

remote_dir = dbutils.widgets.get("remote_dir")
blob_dir = dbutils.widgets.get("blob_dir")
days_back = dbutils.widgets.get("days_back")

Username = 'username'
Password = 'password'
hostname = 'hostname'

### Connecting to server by accepting any Key
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
sftp = pysftp.Connection(host=hostname, username=Username, password=Password, cnopts=cnopts)

### Connecting to server by accepting any Key
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
sftp = pysftp.Connection(host=hostname, username=Username, password=Password, cnopts=cnopts)

date_limit = past_date(days_back)

sftp.cwd(remote_dir)
directory_structure = sftp.listdir_attr()

###list files on server 
def list_files():
  for attr in directory_structure:
      print(attr.filename)
  

def download_files()
  for attr in directory_structure:
      last_modified = attr.st_mtime
      last_modified_date = datetime.fromtimestamp(last_modified).date()
      if last_modified_date > date_limit:
        remote_file = remote_dir + "/" + attr.filename
        blob_file = blob_dir + attr.filename
        try:
          sftp.get(remote_file, blob_file)
          print(f"Downloaded {attr.filename} to Blob Storage")
        except Exception as e:
          print(e)
          
list_files()
download_files()
sftp.close()


