import re

def extract_metrics_from_file(file_path):                   #reading contents of file

    with open(file_path, 'r') as file:
        content = file.read()

    cpu_match = re.search(r'%Cpu\(s\):\s+([\d.]+) us,\s+([\d.]+) sy', content)      #Regular expression (Regex) search to find the required pattern
    cpu_us = float(cpu_match.group(1))
    cpu_sy = float(cpu_match.group(2))
    total_cpu = cpu_us + cpu_sy             #total cpu = system + user value (in %)

    memory_match = re.search(r'MiB\s+Mem\s+:\s+([\d.]+)\stotal,\s+[\d.]+\sfree,\s+([\d.]+)\sused', content)     #regex search to find the required pattern
    total_mem=float(memory_match.group(1))                      #total memory value is from the first group captured
    used_mem = float(memory_match.group(2))                     #used memory value is from the second group captured
    
    return total_cpu , used_mem, total_mem  


def write_metrics_to_file(output_file_path, total_cpu, used_mem, total_mem):        #writing to a output text file
    with open(output_file_path, 'a') as file:
        file.write(f'{total_cpu:.1f}, ')                #Write the total cpu % value onto the output file   
        file.write(f'{used_mem / total_mem * 100:.1f}, ')  #write the used memory % value onto the output file

