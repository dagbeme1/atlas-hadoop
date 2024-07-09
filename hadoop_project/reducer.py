#!/usr/bin/python2.7
"""Reducer for the Hadoop project. Gives top ten salaries from mapper output."""
import sys

# Initialize the highest salaries list
highest_salaries = []

# Read and process input from stdin
for line in sys.stdin:  # Iterate over each line of input from standard input
    # Strip whitespace and split the line by tab or comma
    line = line.strip()  # Remove leading and trailing whitespace
    fields = line.split('\t')  # Split the line by tab
    if len(fields) < 3:  # If the split result has less than 3 fields
        fields = line.split(',')  # Split the line by comma

    # Ensure the line has three fields
    if len(fields) == 3:  # Proceed only if there are exactly three fields
        try:
            employee_id, company, salary = fields  # Unpack the fields into variables
            employee_id = int(employee_id)  # Convert employee_id to an integer
            salary = float(salary)  # Convert salary to a float

            # Add the new entry to the highest salaries list
            if len(highest_salaries) < 10:  # If the list has less than 10 entries
                highest_salaries.append((employee_id, salary, company))  # Append the new entry
                highest_salaries.sort(key=lambda x: x[1], reverse=True)  # Sort the list by salary in descending order
            else:
                if salary > highest_salaries[-1][1]:  # If the new salary is higher than the lowest in the top 10
                    highest_salaries[-1] = (employee_id, salary, company)  # Replace the lowest entry
                    highest_salaries.sort(key=lambda x: x[1], reverse=True)  # Sort the list again
        except ValueError:  # Catch any value conversion errors
            pass  # Ignore lines with conversion errors

# Print the highest salaries
print("id\tSalary\tcompany")  # Print the header
for entry in highest_salaries:  # Iterate over the top 10 entries
    print(f"{entry[0]}\t{entry[1]}\t{entry[2]}")  # Print each entry in the required format
