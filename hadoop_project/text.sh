#!/bin/bash
# The following command reads and displays the content of a file stored in the Hadoop Distributed File System (HDFS).
# 'hadoop fs' is the file system shell command used to interact with HDFS.
# The '-cat' option reads and prints the contents of the specified file to the standard output (console).
# '/holbies/input/lao.txt' is the path to the file in HDFS that we want to display.

hadoop fs -cat /holbies/input/lao.txt
