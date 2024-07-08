#!/usr/bin/python2.7
import sys

# Process input from stdin (standard input)
for line in sys.stdin:
    # Split the line into fields based on comma separation and strip whitespace
    fields = [field.strip() for field in line.split(',')]
    
    # Ensure the line has at least four fields (assuming id, company, and totalyearlycompensation)
    if len(fields) >= 4:
        employee_id, company, _, total_compensation = fields[:4]  # Assuming totalyearlycompensation is at index 3
        
        # Print the output in the required format: id \t company, totalyearlycompensation
        print(f"{employee_id}\t{company},{total_compensation}")
