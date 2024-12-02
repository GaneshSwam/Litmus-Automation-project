#this helper function is optional, can be added to the output txt file get a count of the total topics being printed

import re

def extract_number_of_topics(input_file_path, output_file_path):
    # Regular expression pattern to match the "total number of topics" value
    pattern = r'total number of topics\s+(\d+)'

    # Open the input file for reading
    with open(input_file_path, 'r') as input_file:
        contents = input_file.read()

    # Find all occurrences of the pattern in the contents
    matches = re.findall(pattern, contents)

    # If there are matches, extract the last one as the latest value
    if matches:
        number_of_topics = int(matches[-1])
    else:
        number_of_topics = 0

    # Open the output file for writing the extracted value
    with open(output_file_path, 'a') as output_file:
        output_file.write(str(number_of_topics) + ', ')
