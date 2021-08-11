import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
    
    connect_str = "DefaultEndpointsProtocol=https;AccountName=azurestorageacct;AccountKey=azurestorageacctkey;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    containers = blob_service_client.list_containers()
    for container in containers: 
        print ("Container name: {}".format(container.name))

except Exception as ex:
    print('Exception:')
    print(ex)
