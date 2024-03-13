# client.py
import socket
import pickle


def send_data(sock, data):
    serialized_data = pickle.dumps(data)
    sock.send(serialized_data)


def receive_data(sock):
    serialized_data = sock.recv(1024)
    data = pickle.loads(serialized_data)
    return data


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(
        ("localhost", 12346)
    )  # Assurez-vous que le port correspond au serveur

    try:
        while True:
            # Collectez les données du jeu et envoyez-les au serveur
            player_input = input("Entrez une action (ou 'exit' pour quitter) : ")
            if player_input.lower() == "exit":
                break

            game_data = {"player_action": player_input}
            send_data(client_socket, game_data)

            # Recevez les données du serveur pour mettre à jour l'état du jeu
            server_data = receive_data(client_socket)
            print("Données du serveur reçues:", server_data)
            # Traitez les données reçues et mettez à jour l'état du jeu
            # ...

    finally:
        # Fermez la connexion du client lorsque la boucle se termine
        client_socket.close()


if __name__ == "__main__":
    start_client()
