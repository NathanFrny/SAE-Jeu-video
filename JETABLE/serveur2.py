# server.py
import socket
import threading
import pickle
import signal
import sys


def handle_client(client_socket, client_id):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            # Traitez les données reçues et mettez à jour l'état du jeu
            print(f"Données brutes reçues du client {client_id}: {data}")

            # Désérialisez les données
            decoded_data = pickle.loads(data)
            print(f"Données désérialisées du client {client_id}: {decoded_data}")

            # Simulez une réponse du serveur au client
            response_data = {"server_response": "Action réussie !"}
            send_data(client_socket, response_data)

        except Exception as e:
            print(f"Erreur de réception pour le client {client_id}: {e}")
            break


def send_data(sock, data):
    serialized_data = pickle.dumps(data)
    sock.send(serialized_data)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12346))  # Changez le port si nécessaire
    server.listen(4)

    # Ajoutez la gestion de signal pour intercepter Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    client_id = 1
    while True:
        try:
            client_socket, addr = server.accept()
            print(f"Nouveau joueur connecté : {addr}")
            threading.Thread(
                target=handle_client, args=(client_socket, client_id)
            ).start()
            client_id += 1
        except KeyboardInterrupt:
            # Si Ctrl+C est détecté, fermez le serveur correctement
            print("Arrêt du serveur.")
            break


def signal_handler(sig, frame):
    # Cette fonction sera appelée lorsqu'un signal (comme Ctrl+C) est détecté
    print("Signal détecté, fermeture du serveur.")
    sys.exit(0)


if __name__ == "__main__":
    start_server()
