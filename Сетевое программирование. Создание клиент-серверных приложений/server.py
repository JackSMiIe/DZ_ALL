import socket
import threading
import sqlite3

# Настройки сервера
HOST = '127.0.0.1'
PORT = 12345

# Подключение к базе данных SQLite
conn = sqlite3.connect('chat_users.db', check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы пользователей
cursor.execute('''CREATE TABLE IF NOT EXISTS users
              (username TEXT PRIMARY KEY, password TEXT)''')

# Функция для регистрации нового пользователя
def register_user(username, password):
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# Функция для проверки логина пользователя
def authenticate_user(username, password):
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    return cursor.fetchone() is not None

# Словарь для хранения подключенных клиентов
clients = {}

# Функция для рассылки сообщений всем клиентам
def broadcast(message, _client_socket):
    for client_socket in clients:
        if client_socket != _client_socket:
            try:
                client_socket.send(message)
            except:
                client_socket.close()
                remove_client(client_socket)

# Функция для обработки сообщений от клиента
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"{clients[client_socket]}: {message.decode('utf-8')}")
                broadcast(message, client_socket)
            else:
                remove_client(client_socket)
        except:
            continue

# Функция для удаления клиента из списка
def remove_client(client_socket):
    if client_socket in clients:
        client_socket.close()
        del clients[client_socket]

# Функция для обработки каждого клиента в отдельном потоке
def client_thread(client_socket):
    client_socket.send(b'Welcome to the chat server.\nRegister or login with your username and password.')

    while True:
        try:
            client_socket.send(b'Enter "register" to sign up or "login" to sign in: ')
            choice = client_socket.recv(1024).decode('utf-8').strip().lower()

            client_socket.send(b'Username: ')
            username = client_socket.recv(1024).decode('utf-8').strip()

            client_socket.send(b'Password: ')
            password = client_socket.recv(1024).decode('utf-8').strip()

            if choice == 'register':
                if register_user(username, password):
                    client_socket.send(b'Registration successful. You are now logged in.\n')
                    clients[client_socket] = username
                    break
                else:
                    client_socket.send(b'Username already taken. Please try again.\n')
            elif choice == 'login':
                if authenticate_user(username, password):
                    client_socket.send(b'Login successful. Welcome back!\n')
                    clients[client_socket] = username
                    break
                else:
                    client_socket.send(b'Invalid credentials. Please try again.\n')
        except:
            continue

    while True:
        handle_client(client_socket)

# Запуск сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server started and listening...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    threading.Thread(target=client_thread, args=(client_socket,)).start()
