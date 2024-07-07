#!/usr/bin/python2.7
# Import the Client class from the snakebite.client module to interact with HDFS
from snakebite.client import Client

def createdir(dir_list):
    """
    Create directories in HDFS.
    
    Parameters:
    dir_list (list): A list of directory paths to be created in HDFS.
    """
    # Check if the directory list is not empty
    if dir_list:
        # Initialize Snakebite client to connect to HDFS
        client = Client("localhost", 9000)

        try:
            # Iterate over the list of directories to be created
            for result in client.mkdir(dir_list):
                # Print the result of the mkdir operation for each directory
                print(result)
        except Exception as e:
            # Print the error message if an exception occurs
            print("Error: {}".format(e))
    else:
        # Print a message if the directory list is empty
        print("No directories specified to create.")

# Uncomment the following lines to run the script directly
# if __name__ == '__main__':
#     # Define a list of directories to be created in HDFS
#     dir_list = ["/Betty", "/Betty/Holberton"]
#     # Call the createdir function with the list of directories
#     createdir(dir_listi)
