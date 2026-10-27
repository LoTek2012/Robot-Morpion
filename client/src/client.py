# client/src/client.py

import socket
import numpy
import cv2

class Client :
    """Represente le client Socket."""

    def __init__(self, adress: str, port: int):
        """Initialise le client avec Socket.

            Args:
                - adress (str): L'adresse ID du serveur
                - port (int): Le port sur lequelle se connecter au serveur (doit être le même coté serveur)
        """
        self.adress, self.port = adress, port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.adress, self.port))

    def receive(self, size: int): # Fonction permettant de s'assurer de recevoir tout les octets (socker.Socket.sendall envoi tout mais peut les diviser en plusieurs paquets)
        """Recevoir TOUS les octets envoyer par le serveur.

        Args:
            - size (int): Le nombre d'octet a recevoire

        Returns:
            - data (bytes): Les octets recus depuis le serveur
        """
        data = b""
        while len(data) < size:
            packet = self.socket.recv(size - len(data))
            if packet == None:
                print("Erreur : Connexion interompu")
                return None
            data = data + packet
        return data

    def get_picture(self):
        """Recevoire une image depuis le serveur.

        Returns:
            - img (MatLike | None) : Image JPEG recu convertit en tableau NumPY aannalysable par OpenCV
        """

        self.socket.sendall(b'picture') # b'' signifi que la suite de carractère est en faite des octets/bytes

        picture_size = int.from_bytes(self.receive(4), "big")
        data = self.receive(picture_size)

        print(f"image recu : {picture_size} octets")

        jpeg = numpy.frombuffer(data, dtype=numpy.uint8) # Reconvertit les octets en JPEG (info : jpeg = octet)
        img = cv2.imdecode(jpeg, cv2.IMREAD_COLOR) # Convertit image JPEG en tableu NumPy annalysable par OpenCV !!!!

        return img

    def send(self, data: bytes):
        """Envoi des données au serveur.
        
        Args:
            - data (bytes): Les données à envoyer
        """
        self.socket.sendall(data)

    def close(self):
        """Ferme la connexion avec le serveur."""
        self.socket.close()

    def run(self):
        """Demare """
        while True :
            self.frame = self.get_picture()