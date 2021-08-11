# download_blobs.py
# Python program to bulk download blob files from azure storage
# Uses latest python SDK() for Azure blob storage
# Requires python 3.6 or above
# Code courtesy of: https://www.quickprogrammingtips.com/azure/how-to-download-blobs-from-azure-storage-using-python.html

import os
from azure.storage.blob import BlobServiceClient, BlobClient
from azure.storage.blob import ContentSettings, ContainerClient
 
# IMPORTANT: Replace connection string with your storage account connection string
# Usually starts with DefaultEndpointsProtocol=https;...
MY_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=azureacct;AccountKey=azurekey;EndpointSuffix=core.windows.net"
 
# Replace with the local folder where you want files to be downloaded
LOCAL_BLOB_PATH = "./"
 
class AzureBlobFileDownloader:
  def __init__(self):
    print("Intializing AzureBlobFileDownloader")
 
    # Initialize the connection to Azure storage account
    self.blob_service_client =  BlobServiceClient.from_connection_string(MY_CONNECTION_STRING)
    self.my_container = self.blob_service_client.get_container_client(MY_BLOB_CONTAINER)
 
 
  def save_blob(self,file_name,file_content):
    # Get full path to the file
    download_file_path = os.path.join(LOCAL_BLOB_PATH, file_name)
 
    # for nested blobs, create local path as well!
    try:
        os.makedirs(os.path.dirname(download_file_path))
    except Exception as e:
        print(e)

    with open(download_file_path, "wb") as file:
      file.write(file_content)
 
  def download_all_blobs_in_container(self):
    my_blobs = self.my_container.list_blobs()
    for blob in my_blobs:
      print(blob.name)
      bytes = self.my_container.get_blob_client(blob).download_blob().readall()
      self.save_blob(blob.name, bytes)
 
# Initialize class and upload files
MY_BLOB_CONTAINER = "azurecontainer"
azure_blob_file_downloader = AzureBlobFileDownloader()
azure_blob_file_downloader.download_all_blobs_in_container()

MY_BLOB_CONTAINER = "azurecontainer"
azure_blob_file_downloader = AzureBlobFileDownloader()
azure_blob_file_downloader.download_all_blobs_in_container()

MY_BLOB_CONTAINER = "azurecontainer"
azure_blob_file_downloader = AzureBlobFileDownloader()
azure_blob_file_downloader.download_all_blobs_in_container()
