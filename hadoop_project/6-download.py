#!/usr/bin/python2.7
# Import the Client class from the snakebite.client module to interact with HDFS
from snakebite.client import Client

def download(l):
    """
    Download files from HDFS to the local file system.
    
    Parameters:
    l (list): A list of file paths to be downloaded from HDFS.
    """
    # Check if the list is not empty
    if l:
        # Initialize Snakebite client to connect to HDFS
        client = Client("localhost", 9000)

        try:
            # Iterate over the list of files to be downloaded
            for result in client.copyToLocal(l, '/tmp'):
                # Print the result of the copyToLocal operation for each file
                print(result)
        except Exception as e:
            # Print the error message if an exception occurs
            print("Error: {}".format(e))
    else:
        # Print a message if the list is empty
        print("No files specified to download.")

# Uncomment the following lines to run the script directly
if __name__ == '__main__':
    # Define a list of files to be downloaded from HDFS
    l = ["/holbies/input/lao.txt"]
    # Call the download function with the list of files
    download(l)
