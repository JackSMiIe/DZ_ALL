import socket
import threading

# Настройки клиента
HOST = '127.0.0.1'
PORT = 12345

# Функция для получения сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            continue

# Основная функция клиента
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
