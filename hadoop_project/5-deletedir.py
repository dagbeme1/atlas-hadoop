#!/usr/bin/python2.7
# Import the Client class from the snakebite.client module to interact with HDFS
from snakebite.client import Client

def deletedir(dir_list):
    """
    Delete directories in HDFS.
    
    Parameters:
    dir_list (list): A list of directory paths to be deleted in HDFS.
    """
    # Check if the directory list is not empty
    if dir_list:
        # Initialize Snakebite client to connect to HDFS
        client = Client("localhost", 9000)

        # Sort the directory list in reverse order to delete nested directories first
        dir_list.sort(reverse=True)
        try:
            # Iterate over the list of directories to be deleted
            for result in client.rmdir(dir_list):
                # Print the result of the rmdir operation for each directory
                print(result)
        except Exception as e:
            # Print the error message if an exception occurs
            print("Error: {}".format(e))
    else:
        # Print a message if the directory list is empty
        print("No directories specified to delete.")

# Uncomment the following lines to run the script directly
if __name__ == '__main__':
    # Define a list of directories to be deleted in HDFS
    dir_list = ["/Betty", "/Betty/Holberton"]
    # Call the deletedir function with the list of directories
    deletedir(dir_list)
