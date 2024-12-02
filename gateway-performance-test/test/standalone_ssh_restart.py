#optional standalone python file to perform ssh restart if needed

import paramiko
import os

def run_ssh_restart_command(hostname, username, password, command): #to execute a series of command which restart loopedge-dh and restore the cmd prompt
    ssh = paramiko.SSHClient()      # Create an instance of the SSHClient class from the Paramiko library to establish an SSH connection.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # Set the host key policy to AutoAddPolicy, which automatically adds unknown SSH server keys to the client's known hosts.

    try:
        ssh.connect(hostname, username=username, password=password)
        _, stdout, stderr = ssh.exec_command(command)  # Using '_' to ignore stdin

        # Reading and decoding the output
        result = stdout.read().decode('utf-8').strip()
        error = stderr.read().decode('utf-8').strip()

        print("Restart command executed successfully:")
        #print(result)

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


if __name__ == "__main__":

    #get the values from environment variables
    host_ip=os.environ.get("LE_HOST_IP_ADDRESS")
    ssh_username = os.environ.get("LE_SSH_USERNAME")
    ssh_password = os.environ.get("LE_SSH_PASSWORD")

 # Commands to execute on the remote server
    commands_to_run = [
        'cd /var/lib/loopedge-dh',
        'rm -r db',
        'systemctl restart loopedge-dh',
        'cd ~'
    ]
    # Combining commands using '&&'
    combined_command = ' && '.join(commands_to_run)     

    run_ssh_restart_command(host_ip, ssh_username, ssh_password, combined_command)  