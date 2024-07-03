#!/bin/bash
# This script creates two directories in HDFS

# Create the 'holbies' directory in HDFS root
hdfs dfs -mkdir /holbies

# Create the 'input' directory inside the 'holbies' directory
hdfs dfs -mkdir /holbies/input
