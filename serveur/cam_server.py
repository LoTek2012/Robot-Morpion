import socket
import cv2

class CamServer :

    def __init__(self, host, port, cam_index):
        self.host, self.port = host, port
        self.cam_index = cam_index

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("serveur créé")
        
        self.socket.bind((self.host, self.port))
        self.socket.listen(1) # Ecoute une seul fois
        self.client, address = self.socket.accept() # accept la connexion

        self.cam = cv2.VideoCapture(self.cam_index) # Ouvre la webcam specifié (par defaut : index=0)

        if self.cam.isOpened() == False :
            raise Exception("Impossible d'accéder à la webcam")


    def receive(self, size):
            data = b""
            while len(data) < size:
                packet = self.client.recv(size - len(data)) # attent de recevoir quelque chose, renvoi b"" si connexion fermé
                if packet == b"":
                    raise Exception("Connexion au client interompu")
                data = data + packet
            return data

    def take_picture(self) :
        ret, frame = self.cam.read()
        if not ret or frame is None :
            print("Erreur : Impossible de capturer l'image")
            return None
        return frame

    def send_picture(self, img):

        success, jpeg = cv2.imencode(".jpg", img) # Convertire image NumPy en JPEG (success est une variable booleen)
        if success == False :
            print("Erreur : Echec de la conversion en JPEG à partir de l'image NumPy")
            return False

        data2 = jpeg.tobytes() # Convertire JPEG en octets (methode des tableau NumPy)
        img_size = len(data2) # Obtenire le nombre d'octet de l'image convertit en octets
        data1 = img_size.to_bytes(4, "big") # Convertire la taille de l'image (int) en octets (4 est le nombre d'octets utiliser : 1 octet = 1 -> 255) (methode de int)

        self.send(data1)
        self.send(data2)

        return True

    def send(self, data):
        self.client.sendall(data)

    def run(self):
        while True:
            request = self.receive(7)
            
            if request == b'picture':
                img = self.take_picture()
                if img is None :
                    continue
                success = self.send_picture(img)
            else :
                print('Erreur : Requette incorrecte')

    def close(self):
        self.socket.close()
        self.cam.release()
