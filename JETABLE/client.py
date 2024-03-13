import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adresse_ip_serveur = "127.0.0.1"
port_serveur = 12345

try:
    client.connect((adresse_ip_serveur, port_serveur))

    # Demande au client de choisir un nom d'utilisateur
    username = input("Veuillez choisir un nom d'utilisateur : ")
    client.send(username.encode())

    # Attend la confirmation de l'acceptation du nom d'utilisateur
    confirmation = client.recv(1024).decode()
    print(confirmation)

    while True:
        # Envoie un message au serveur
        message = input(
            "Message au serveur (ou '/msg destinataire message' pour message privé, '/liste' pour afficher la liste des utilisateurs, '/salon nom_salon' pour créer ou rejoindre un salon, '/quitter' pour quitter un salon, '/listesalons' pour voir la liste des salons disponibles, '/membres' pour voir la liste des membres dans le salon, ou '/bye' pour se déconnecter) : "
        )
        client.send(message.encode())

        # Vérifie si le client souhaite se déconnecter
        if message.lower() == "/bye":
            break

        # Affiche la réponse du serveur
        reponse_serveur = client.recv(1024).decode()
        print(reponse_serveur)

except ConnectionRefusedError:
    print("La connexion au serveur a été refusée.")

except ConnectionResetError:
    print("La connexion avec le serveur a été interrompue.")

finally:
    # Ferme la connexion
    client.close()
