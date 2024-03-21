import paramiko

# SSH-Verbindungsinformationen
hostname = '10.3.14.121'
port = 22  # Standard-SSH-Port ist 22
username = 'Administrator'
password = 'Start123$'

def establish_ssh_connection(hostname, port, username, password):
    """Stellt eine SSH-Verbindung her."""
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh_client.connect(hostname, port, username, password)
        print("Erfolgreich mit dem Server verbunden.")
        return ssh_client
    except paramiko.AuthenticationException:
        print("Authentifizierung fehlgeschlagen. Überprüfen Sie Ihre Anmeldeinformationen.")
    except paramiko.SSHException as ssh_err:
        print(f"Fehler beim Verbindungsaufbau: {ssh_err}")
    return None

def execute_powershell_command(ssh_client, command):
    """Führt einen PowerShell-Befehl aus."""
    stdin, stdout, stderr = ssh_client.exec_command(f'powershell.exe -Command "{command}"')
    output = stdout.read().decode()
    print("Ausgabe des PowerShell-Befehls:")
    print(output)

def main():
    ssh_client = establish_ssh_connection(hostname, port, username, password)
    if ssh_client:
        # PowerShell-Befehl zum Erstellen eines Benutzers im Active Directory
        powershell_command = '''
        New-ADUser -Name "Jack Robinson" -GivenName "Jack" -Surname "Robinson" 
        -SamAccountName "J.Robinson" -UserPrincipalName "J.Robinson@nifede.pri" 
        -Path "OU=Users,DC=nifede,DC=pri" -AccountPassword (ConvertTo-SecureString "Start123$" -AsPlainText -Force) 
        -Enabled $true
        '''
        execute_powershell_command(ssh_client, powershell_command)
        ssh_client.close()

if __name__ == "__main__":
    main()
