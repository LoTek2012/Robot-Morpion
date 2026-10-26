# Robot-Morpion
Un robot LEGO Mindstorms NXT qui annalyse un plateau de morpion et joue le meilleur coup possible

## Préparation

### Materiel
* Beaucoup de pieces LEGO
* La LEGO Cam (C'est pour cette raison que le server est sous Windows XP et qu'il y a un serveur en fait 😉.)
* 2 PCs (Pour le [Client](#client) et le [Serveur](#server))

### Instructions de montage
Les instruction de montages se trouvent dans le dossier ``lego/`` au format PDF avec le fichier pour Bricklink Studio.

### Environement Python
* Pour le [Client](#client), utiliser le ``requirement.txt``.
* Pour le [Serveur](#), utiliser ``robot_morpion/server_robot_morpion/server_requirement.txt`` avec ``Python 2.4.4``. Respecter les versions des bibliotheques et de Python du Serveur **uniquement si le Serveur est sous Windows XP**. La version de ``opencv-python`` pour ``Python 3.4.4`` n'existe plus sur PyPi, vous la trouverai [ici](https://dashboard.stablebuild.com/pypi-deleted-packages/pkg/opencv-python/3.2.0.8)

## Lancement du robot
Il faut d'abord commencer par lancer le [Serveur](#server) car sinon le [Client](#client) renvera une erreur de connexion

### Server
Les fichiers du Serveur se situe dans ``robot_morpion/server_robot_morpion/``.
Le dossier du server doit être placé sur un ordinateur different du Client et connecté au même reseau local.

Le server a été concu et optimiser pour fonctionner sur Windows XP avec Python 3.4.4 mais il peut fonctionner sur un environement plus recent avec les bonne versions de Python et des bibliotheques.

Sa fonction est simplement de prendre des photos avec la camera et de les envoyer au [Client](#client) via ``socket``.

### Client
Le Client s'occupe de :
1. Demander et recevoire les images de la camera du [Serveur](#server) via ``socket``
2. Annalizer les images et l'avancement du jeu avec la bibliotheque ``opencv-python``
3. Jouer le meilleur coup possible en utilisant les moteurs de la brique NXT via ``nxt-python``

## License
**MIT License**
