import winrm

# Erstelle eine Verbindung zum Windows-Server
session = winrm.Session('10.3.14.121', auth=('NIFEDE\Administrator', ''))

# Führe das whoami-Kommando auf dem Server aus
result = session.run_cmd('whoami')

# Gib das Ergebnis aus
print("whoami output:", result.std_out.decode())
