# serveur/main.py

import traceback
import sys
import os
from dotenv import load_dotenv
from cam_server import CamServer

load_dotenv()

HOST = os.getenv('HOST', 'localhost')
PORT = int(os.getenv('PORT', 2012))
CAM_INDEX = int(os.getenv('CAM_INDEX', 0))

try:
    cam_server = CamServer(HOST, PORT, CAM_INDEX)
    print('serveur lancé')
    cam_server.run()

except Exception:
    traceback.print_exc()

finally:
    cam_server.close()
    sys.exit()