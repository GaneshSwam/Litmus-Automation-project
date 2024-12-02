import paramiko

def run_ssh_top_command(hostname, username, password, command):
    ssh = paramiko.SSHClient()                                          # create an instance of SSHClient from the paramiko library and set the host key policy to automatically accept unknown host keys.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, username=username, password=password)         #execute the specified command on the remote host via SSH and capture the standard output of the command execution. The result is then decoded from bytes to a UTF-8 string and stored in the result variable.
        _, stdout, stderr = ssh.exec_command(command)
        result = stdout.read().decode('utf-8').strip()

        remote_file_path = "/home/root/top_data.txt"                        #define the paths for the remote and local files. remote_file_path points to the location of the file on the remote host, while local_file_path points to the desired local destination for the downloaded file.
        local_file_path = r"top_data.txt"

        sftp_client = ssh.open_sftp()                                       #use SFTP (Secure File Transfer Protocol) to download the remote file specified by remote_file_path to the local path specified by local_file_path
        sftp_client.get(remote_file_path, local_file_path)
        sftp_client.close()

        with open(local_file_path, 'r') as file:
            content = file.read()

        chunks = content.split("top -")                         #to get the contents of the latest top command iteration, as that is pretty accurate
        last_iteration = chunks[-1]

        latest_file_path = r"top_data_latest.txt"           #define the path for the new file top_data_latest.txt where the extracted last iteration will be saved. It then opens the file in write mode and writes the extracted last iteration into it.
        with open(latest_file_path, 'w') as file:
            file.write("top -" + last_iteration)

        print("File 'top_data_latest.txt' created successfully.")
    except paramiko.AuthenticationException:                                        #handle potential exceptions that might occur during the execution of the code. They provide error messages for different types of exceptions that can be raised. The finally block ensures that the SSH connection is properly closed regardless of whether an exception occurred or not.
        print("Authentication failed. Please check your username and password.")
    except paramiko.SSHException as ssh_ex:
        print(f"SSH error occurred: {ssh_ex}")
    except Exception as ex:
        print(f"An error occurred: {ex}")
    finally:
        ssh.close()