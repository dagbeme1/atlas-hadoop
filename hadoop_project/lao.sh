#!/bin/bash
# lao.sh - A script to upload the file lao.txt to the /holbies/input directory on HDFS.

# Define the local file to be uploaded
#local_file="./lao.txt"  # Specify the local file path

# Define the target HDFS directory
#hdfs_directory="/holbies/input"  # Specify the HDFS directory

# Create the HDFS directory if it does not exist
#hadoop fs -mkdir -p /holbies/input  # Create the target directory on HDFS

# Upload the file to the HDFS directory
hdfs dfs -put -f lao.txt/holbies/input  # Use 'put' to upload the file

# Verify the upload by listing the files in the HDFS directory
#hadoop fs -ls /holbies/input  # List the contents of the target HDFS directory
