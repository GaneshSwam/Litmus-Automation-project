# Project Documentation

## List of Environment Variables
- `LE_API_USERNAME_TOKEN`
- `LE_HOST_IP_ADDRESS`
- `LE_SSH_USERNAME`
- `LE_SSH_PASSWORD`

## List of Sub-folders
- device templates (.json templates)
- csvs (tags csv files)
- test (containing the code files)

## List of Associated Files
### Python Files:
1. `nats_msg_count_ssh.py`: Establishes an SSH connection, runs SSH commands, and downloads a specific file using the Paramiko library with exception handling.
2. `top_ssh.py`: Establishes an SSH connection, executes a specified (top) command, extracts the latest iteration's output, and handles errors.
3. `ssh_loopedge_restart.py`: Establishes an SSH connection, restarts a process through commands, handles errors, and closes the connection.
4. `extract_nats_msg_data.py`: Extracts and processes message counts from a file using regular expressions, calculates maximum counts, and appends output.
5. `extract_top_data.py`: Extracts CPU and memory metrics from a file, calculates percentages, and writes results.
6. `extract_total_topics.py`: Extracts total topic count from an input file and appends to an output file.
7. `report_generator_in_excel.py`: Creates and formats an Excel workbook with initial content, headers, and line charts.
8. `wrapper_script.py`: Orchestrates function calls and generates required output files.
9. `standalone_ssh_restart.py`: Restarts a process on a remote host using Paramiko and os libraries, with optional SSH details.

## Brief Information about Generated Files
1. `top_data.txt`: Contains system performance metrics from the 'top' command.
2. `top_data_latest.txt`: Holds the latest iteration of performance metrics from the 'top' command.
3. `msg_data.txt`: Contains message-related data.
4. `output_file.txt`: Comma-separated values including device info, message counts, CPU utilization, etc.
5. `output_file.csv`: Same data as `output_file.txt` in CSV format.
6. `output.xlsx`: Main output file with tables and charts for analysis.

## Libraries Used
- `requests`
- `urllib3`
- `openpyxl`
- `paramiko`
- `tqdm`

## Steps Before Execution
1. Obtain authorization token and set as environment variable.
2. Define and store host IP, SSH username, and password as environment variables.
3. Ensure required Python libraries are installed.
4. Install NATS tool on SSH client (inside /home/root/)
5. Obtain and activate any license key reuqired for the LE version for uploading templates 

## Running the Code
1. Run `wrapper_script.py` from terminal with path 'C:\..\gateway-performance-test\' and command 'python test/wrapper_script.py' .
2. Observe terminal messages.
3. Files like `top_data.txt`, `msg_data.txt`, etc., will be created and updated.
4. Once iterations are done, `output_file.csv` and `output.xlsx` will be generated.

## Additional Points
1. Adjust time delays in `wrapper_script.py` based on gateway.
2. Use `devices_list` with '1' included for debugging to overwrite `output_file.txt`.
3. `output_file.csv` aids in cross-checking data before creating `output.xlsx`.
