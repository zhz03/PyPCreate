# importing the requests module
import requests
from zipfile import ZipFile

print('Downloading started')
url = 'https://github.com/zhz03/mkdocs_sample/blob/main/mkdocs_sample.zip?raw=true'

# Downloading the file by sending the request to the URL
req = requests.get(url)
 
# Split URL to get the file name
filename = url.split('/')[-1].split('?')[0]
 
# Writing the file to the local file system
with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')