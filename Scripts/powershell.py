import paramiko

# SSH-Verbindungsinformationen
hostname = '10.3.14.121'
port = 22  # Standard-SSH-Port ist 22
username = 'Administrator'
password = 'Start123$'

# Erstellen einer SSH-Verbindung
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(hostname, port, username, password)
    print("Erfolgreich mit dem Server verbunden.")

    # PowerShell-Befehl zum Erstellen eines Benutzers im Active Directory
    powershell_command = '''New-ADUser -Name "Jack Robinson" -GivenName "Jack" -Surname "Robinson" -SamAccountName "J.Robinson" -UserPrincipalName "J.Robinson@nifede.pri" -Path "OU=Importuser,DC=nifede,DC=pri" -AccountPassword (ConvertTo-SecureString "Start123$" -AsPlainText -Force) -Enabled $true'''

    # Ausführen des PowerShell-Befehls
    stdin, stdout, stderr = ssh_client.exec_command('powershell.exe -Command "{}"'.format(powershell_command))
    
    # Ausgabe lesen
    output = stdout.read().decode()
    
    print("Ausgabe des PowerShell-Befehls:")
    print(output)
    
except paramiko.AuthenticationException:
    print("Authentifizierung fehlgeschlagen. Überprüfen Sie Ihre Anmeldeinformationen.")
except paramiko.SSHException as ssh_err:
    print(f"Fehler beim Verbindungsaufbau: {ssh_err}")
finally:
    # SSH-Verbindung schließen
    ssh_client.close()
