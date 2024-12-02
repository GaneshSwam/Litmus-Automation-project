import re

def extract_total_messages_count(file_contents):  
          
    pattern = r'total messages\s+(\d+)'             # Regular expression pattern to match 'total messages' followed by numbers

    messages_counts = []
    matches = re.findall(pattern, file_contents)        # Find all matches in the file contents using the pattern

    for match in matches:
        messages_counts.append(int(match))              # Convert matched strings to integers and add to the list

    return messages_counts

def find_max_total_messages_count(file_contents):               
    messages_counts = extract_total_messages_count(file_contents)       # Get total message counts using the helper function
    if messages_counts:
        return max(messages_counts)             # Return the maximum value from the list of message counts
    else:
        return None         # Return None if no message counts were found

def read_file(file_path):                           
    with open(file_path, 'r') as file:
        return file.read()      # Read and return the contents of the file

def write_output_to_file(file_path, output):        
    with open(file_path, 'a') as file:
        file.write(f"{output}, ")       # Append the output followed by a comma and a space to the file

