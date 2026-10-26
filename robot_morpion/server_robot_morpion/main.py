from cam_server import CamServer
import traceback
import sys

HOST = "0.0.0.0"
PORT = 2012
CAM_INDEX = 0

try:
    cam_server = CamServer(HOST, PORT, CAM_INDEX)
    print('serveur lancé')
    cam_server.run()

except Exception:
    traceback.print_exc()

finally:
    cam_server.close()
    sys.exit()