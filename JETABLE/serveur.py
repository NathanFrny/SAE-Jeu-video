import socket
import threading

# Dictionnaire pour stocker les connexions des clients avec leurs noms d'utilisateur et les salons auxquels ils sont connectés
clients = {}
salons = {}


def broadcast(message, client_exclu=None, salon=None):
    """Diffuse un message à tous les clients d'un salon."""
    if salon:
        for username, client in clients.items():
            if username in salons.get(salon, set()) and client != client_exclu:
                try:
                    client.send(message)
                except:
                    # En cas d'erreur de connexion, retire le client de la liste
                    supprimer_client(username)
    else:
        for username, client in clients.items():
            if client != client_exclu:
                try:
                    client.send(message)
                except:
                    # En cas d'erreur de connexion, retire le client de la liste
                    supprimer_client(username)


def gerer_client(client, adresse):
    try:
        # Demande au client de choisir un nom d'utilisateur
        client.send("Veuillez choisir un nom d'utilisateur : ".encode())
        username = client.recv(1024).decode()

        # Vérifie si le nom d'utilisateur est déjà pris
        while username in clients:
            client.send(
                "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre : ".encode()
            )
            username = client.recv(1024).decode()

        # Confirme l'acceptation du nom d'utilisateur
        client.send("Nom d'utilisateur accepté. Bienvenue!".encode())

        # Ajoute le client à la liste avec son nom d'utilisateur
        clients[username] = client

        # Informe tous les clients du nouveau client connecté
        message_connexion = f"{username} a rejoint le chat."
        broadcast(message_connexion.encode())

        # Message de bienvenue dans le salon principal
        message_bienvenue = f"Bienvenue sur le serveur principal, {username}!"
        clients[username].send(message_bienvenue.encode())

        while True:
            # Reçoit les données du client
            donnees = client.recv(1024)
            if not donnees:
                break

            # Convertit les données en chaîne
            message = donnees.decode()

            # Vérifie si le client souhaite se déconnecter
            if message.lower() == "/bye":
                break

            # Vérifie si le message est une commande de message privé
            elif message.startswith("/msg "):
                destinataire, contenu_msg = message[5:].split(" ", 1)
                destinataire = destinataire.lower()

                # Vérifie si le destinataire existe
                if destinataire in clients:
                    message_prive = f"Message privé de {username}: {contenu_msg}"
                    clients[destinataire].send(message_prive.encode())
                else:
                    message_destinataire_inexistant = (
                        f"Le destinataire {destinataire} n'existe pas."
                    )
                    clients[username].send(message_destinataire_inexistant.encode())

            # Vérifie si le message est une commande pour lister les utilisateurs
            elif message.lower() == "/liste":
                liste_utilisateurs = "Utilisateurs connectés : " + ", ".join(
                    clients.keys()
                )
                client.send(liste_utilisateurs.encode())

            # Vérifie si le message est une commande pour créer ou rejoindre un salon
            elif message.startswith("/salon "):
                if trouver_salon_utilisateur(username):
                    # Empêche l'utilisateur de rejoindre un salon s'il est déjà dans un salon
                    message_salon_existant = "Vous êtes déjà dans un salon. Veuillez quitter le salon actuel avant de rejoindre un nouveau salon."
                    clients[username].send(message_salon_existant.encode())
                else:
                    salon_demande = message[7:]
                    creer_ou_rejoindre_salon(username, salon_demande)

            # Vérifie si le message est une commande pour quitter un salon
            elif message.lower() == "/quitter":
                quitter_salon(username)

            # Vérifie si le message est une commande pour voir la liste des salons disponibles
            elif message.lower() == "/listesalons":
                liste_salons = "Salons disponibles : " + ", ".join(salons.keys())
                client.send(liste_salons.encode())

            # Vérifie si le message est une commande pour voir la liste des membres dans le salon
            elif message.lower() == "/membres":
                salon_client = trouver_salon_utilisateur(username)
                if salon_client:
                    membres_salon = "Membres du salon : " + ", ".join(
                        salons.get(salon_client, set())
                    )
                    client.send(membres_salon.encode())
                else:
                    message_pas_dans_salon = (
                        "Vous n'êtes actuellement dans aucun salon."
                    )
                    clients[username].send(message_pas_dans_salon.encode())

            else:
                # Affiche le message du client
                message = f"{username}: {message}"
                print(message)

                # Envoie le message à tous les clients du même salon
                salon_client = trouver_salon_utilisateur(username)
                broadcast(message.encode(), client, salon_client)

    except ConnectionResetError:
        print(f"La connexion avec {adresse} a été interrompue.")

    finally:
        # Ferme la connexion et retire le client de la liste
        supprimer_client(username)
        client.close()
        print(f"Connexion avec {adresse} fermée.")


def creer_ou_rejoindre_salon(username, salon_demande):
    """Crée ou rejoint un salon."""
    if salon_demande not in salons:
        # Crée un nouveau salon s'il n'existe pas
        salons[salon_demande] = set([username])
        message_bienvenue = f"Bienvenue dans le salon {salon_demande}, {username}!"
        clients[username].send(message_bienvenue.encode())
    else:
        # Rejoint le salon s'il existe
        salons[salon_demande].add(username)
        message_bienvenue = f"Bienvenue dans le salon {salon_demande}, {username}!"
        clients[username].send(message_bienvenue.encode())

    # Informe le client de son salon actuel
    message_salon = f"Vous êtes dans le salon : {salon_demande}"
    clients[username].send(message_salon.encode())

    # Informe tous les clients du salon de l'arrivée du nouveau client
    message_nouveau_client = f"{username} a rejoint le salon."
    broadcast(message_nouveau_client.encode(), salon=salon_demande)


def quitter_salon(username):
    """Quitte un salon."""
    salon_client = trouver_salon_utilisateur(username)

    if salon_client:
        # Retire le client du salon
        salons[salon_client].remove(username)

        # Informe le client qu'il a quitté le salon
        message_quitte_salon = f"Vous avez quitté le salon : {salon_client}"
        clients[username].send(message_quitte_salon.encode())

        # Informe les autres clients du salon du départ du client
        message_depart_client = f"{username} a quitté le salon."
        broadcast(message_depart_client.encode(), salon=salon_client)
    else:
        # Informe le client s'il n'est pas dans un salon
        message_pas_dans_salon = "Vous n'êtes actuellement dans aucun salon."
        clients[username].send(message_pas_dans_salon.encode())


def trouver_salon_utilisateur(username):
    """Trouve le salon auquel un utilisateur est connecté."""
    for salon, utilisateurs in salons.items():
        if username in utilisateurs:
            return salon
    return None


def supprimer_client(username):
    """Supprime un client de la liste."""
    if username in clients:
        # Informe tous les clients de la déconnexion du client
        message_deconnexion = f"{username} a quitté le chat."
        broadcast(message_deconnexion.encode())

        # Retire le client de tous les salons
        for salon in salons.values():
            if username in salon:
                salon.remove(username)

        del clients[username]


# Configuration du serveur
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adresse_ip = "127.0.0.1"
port = 12345
serveur.bind((adresse_ip, port))
serveur.listen(5)
print(f"Le serveur écoute sur {adresse_ip}:{port}")

try:
    while True:
        # Accepte une nouvelle connexion
        client, adresse = serveur.accept()
        print(f"Connexion établie avec {adresse}")

        # Crée un thread pour gérer le client
        thread_client = threading.Thread(target=gerer_client, args=(client, adresse))
        thread_client.start()

except KeyboardInterrupt:
    print("Arrêt du serveur.")
    fermer_connexions()

finally:
    # Ferme la connexion du serveur
    serveur.close()
