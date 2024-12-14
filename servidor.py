import socket

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 65432        # Puerto del servidor

# Crear un socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor escuchando en {HOST}:{PORT}")

# Aceptar conexión de un cliente
conn, addr = server_socket.accept()
print(f"Conexión establecida con {addr}")

while True:
    # Recibir datos del cliente
    data = conn.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Cliente: {data}")

    # Enviar respuesta al cliente
    respuesta = input("Servidor (escribe tu mensaje): ")
    conn.sendall(respuesta.encode('utf-8'))

conn.close()
