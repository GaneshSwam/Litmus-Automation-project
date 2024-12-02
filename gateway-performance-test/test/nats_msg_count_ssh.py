import paramiko

def run_ssh_nats_command(hostname, username, password, command):    #to run ssh nats tool commmand and download the file generated onto local device
    ssh = paramiko.SSHClient()      # Create an instance of the SSHClient class from the Paramiko library to establish an SSH connection.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # Set the host key policy to AutoAddPolicy, which automatically adds unknown SSH server keys to the client's known hosts.

    try:
        ssh.connect(hostname, username=username, password=password)
        _, stdout, stderr = ssh.exec_command(command)  # Using '_' to ignore stdin

        # After running the command on the remote server
        result = stdout.read().decode('utf-8').strip()

        # Downloading the file from the remote server
        
        remote_file_path = "/home/root/msg_data.txt"  # Adjusting the path to topp.txt on the remote server
        local_file_path = r"msg_data.txt"  # Local path to save the downloaded file

        sftp_client = ssh.open_sftp()       # Establish an SFTP (SSH File Transfer Protocol) client using the previously established SSH connection.
        sftp_client.get(remote_file_path, local_file_path)      # Download a file from the remote server using the SFTP client.
        sftp_client.close()                 # Close the SFTP client to release resources and end the SFTP session.

        print(f"File 'msg_data.txt' downloaded successfully.")
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your username and password.")
    except paramiko.SSHException as ssh_ex:
        print(f"SSH error occurred: {ssh_ex}")
    except Exception as ex:
        print(f"An error occurred: {ex}")
    finally:
        ssh.close()

