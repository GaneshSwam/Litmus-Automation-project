import paramiko

def run_ssh_restart_command(hostname, username, password, command): #to execute a series of command which restart loopedge-dh and restore the cmd prompt

    ssh = paramiko.SSHClient()      # Create an instance of the SSHClient class from the Paramiko library to establish an SSH connection.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # Set the host key policy to AutoAddPolicy, which automatically adds unknown SSH server keys to the client's known hosts.

    try:
        ssh.connect(hostname, username=username, password=password)     # Establish an SSH connection to the remote server
        # Execute the specified command on the remote server
        _, stdout, stderr = ssh.exec_command(command)  # Using '_' to ignore stdin

        # Reading and decoding the output
        result = stdout.read().decode('utf-8').strip()
        error = stderr.read().decode('utf-8').strip()

        print("Restart command executed successfully: \n")
        # Print any error messages from the executed command
        if error:
            print("Error occurred:")
            print(error)
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your username and password.")
    except paramiko.SSHException as ssh_ex:
        print(f"SSH error occurred: {ssh_ex}")
    except Exception as ex:
        print(f"An error occurred: {ex}")
    finally:
        ssh.close()     # Close the SSH connection, regardless of success or failure

