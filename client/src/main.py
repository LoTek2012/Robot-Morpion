from client import Client
from camera_preview import CameraPreview
from config import *
import sys
import traceback
import threading

try :
    client = Client(HOST, PORT)
    preview = CameraPreview(WINDOW_PREVIEW_NAME, client)
    print('Connecté au serveur')

    while True :
        picture = client.get_picture()
        preview.update_window(picture)
        preview.window.update()
        #preview.run()
    #client.run()

except Exception :
    traceback.print_exc()

finally:
    client.close()
    sys.exit()
