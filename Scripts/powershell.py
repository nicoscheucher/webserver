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

    # Ausführen von ipconfig-Befehl
    stdin, stdout, stderr = ssh_client.exec_command('ipconfig')
    
    # Ausgabe lesen
    output = stdout.read().decode()
    
    print("Ausgabe von 'ipconfig' auf dem Server:")
    print(output)
    
except paramiko.AuthenticationException:
    print("Authentifizierung fehlgeschlagen. Überprüfen Sie Ihre Anmeldeinformationen.")
except paramiko.SSHException as ssh_err:
    print(f"Fehler beim Verbindungsaufbau: {ssh_err}")
finally:
    # SSH-Verbindung schließen
    ssh_client.close()
