import subprocess

# Definiere die PowerShell-Befehle, um eine Verbindung zum Server herzustellen und das whoami-Kommando auszuführen
powershell_commands = [
    "$Username = 'DEIN_USERNAME'",
    "$Password = ConvertTo-SecureString 'DEIN_PASSWORT' -AsPlainText -Force",
    "$Credential = New-Object System.Management.Automation.PSCredential($Username, $Password)",
    "$Session = New-PSSession -ComputerName SERVER_NAME -Credential $Credential",
    "Invoke-Command -Session $Session -ScriptBlock { whoami }",
    "Remove-PSSession $Session"
]

# Verbinde dich per PowerShell und führe das whoami-Kommando aus
output = subprocess.run(["powershell.exe", "-Command", ";".join(powershell_commands)], capture_output=True, text=True)

# Gib das Ergebnis aus
print("whoami output:", output.stdout)
