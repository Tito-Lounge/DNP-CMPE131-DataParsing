import sys
import csv
import json
import xml.etree.ElementTree as ET

# Define the conversion functions
def convert_to_csv(data):
    output = io.StringIO()
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)
    return output.getvalue()

def convert_to_json(data):
    return json.dumps(data)

def convert_to_xml(data):
    root = ET.Element('data')
    for row in data:
        child = ET.SubElement(root, 'row')
        for i, col in enumerate(row):
            ET.SubElement(child, f'col{i}').text = col
    return ET.tostring(root, encoding='unicode')

# Get the filename and output format from command-line arguments
filename = sys.argv[1]
output_format = sys.argv[2]

# Read the data from the file
with open(filename, 'r') as f:
    data = [line.strip().split('\t') for line in f]

# Convert the data to the requested format
if output_format == '-c':
    output = convert_to_csv(data)
    output_filename = f'{filename}.csv'
elif output_format == '-j':
    output = convert_to_json(data)
    output_filename = f'{filename}.json'
elif output_format == '-x':
    output = convert_to_xml(data)
    output_filename = f'{filename}.xml'
else:
    print('Unknown output format')
    sys.exit(1)

# Save the output to a file
with open(output_filename, 'w') as f:
    f.write(output)

print(f'File saved as {output_filename}')