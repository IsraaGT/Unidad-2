import socket

# Configuración del cliente
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 65432        # Puerto del servidor

# Crear un socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"Conectado al servidor en {HOST}:{PORT}")

while True:
    # Enviar mensaje al servidor
    mensaje = input("Cliente (escribe tu mensaje): ")
    client_socket.sendall(mensaje.encode('utf-8'))

    # Recibir respuesta del servidor
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Servidor: {data}")

    if mensaje.lower() == "salir" or data.lower() == "salir":
        print("Cerrando conexión...")
        break

client_socket.close()
