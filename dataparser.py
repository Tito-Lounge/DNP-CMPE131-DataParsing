import os
import csv
import json
import xml.etree.ElementTree as ET
import io

# Define the conversion functions

def convert_to_csv(data):
    """Converts a list of lists to CSV format"""
    output = io.StringIO() # Create a buffer to hold the output
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) # Create a CSV writer
    for row in data:
        writer.writerow(row) # Write each row to the buffer
    return output.getvalue() # Return the contents of the buffer as a string

def convert_to_json(data):
    """Converts a list of lists to JSON format"""
    return json.dumps(data) # Return the data as a JSON string

def convert_to_xml(data):
    """Converts a list of lists to XML format"""
    root = ET.Element('data') # Create an XML root element
    for row in data:
        child = ET.SubElement(root, 'row') # Create a child element for each row
        for i, col in enumerate(row):
            ET.SubElement(child, f'col{i}').text = col # Create a child element for each column
    return ET.tostring(root, encoding='unicode') # Return the XML as a string

# Prompt the user for a file name
filename = input('Enter the name of the file to convert (including extension): ')

# Check that the file exists
if not os.path.exists(filename):
    print(f'Error: File "{filename}" not found in the current directory.')
    exit()

# Get the output format from the user
output_format = input('Enter the output format (c for CSV, j for JSON, x for XML): ')

# Read the data from the file
with open(filename, 'r') as f:
    data = [line.strip().split('\t') for line in f]

# Convert the data to the requested format
if output_format == 'c':
    output = convert_to_csv(data)
    output_filename = f'{os.path.splitext(filename)[0]}.csv'
elif output_format == 'j':
    output = convert_to_json(data)
    output_filename = f'{os.path.splitext(filename)[0]}.json'
elif output_format == 'x':
    output = convert_to_xml(data)
    output_filename = f'{os.path.splitext(filename)[0]}.xml'
else:
    print('Error: Invalid output format. Please enter c, j, or x.')
    exit()

# Save the output to a file
with open(output_filename, 'w') as f:
    f.write(output)

print(f'File saved as {output_filename} in the current directory.')
