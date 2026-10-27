# client/src/config.py

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / '.env'

load_dotenv(ENV_FILE)

HOST = os.getenv('HOST', 'localhost')
PORT = int(os.getenv('PORT', 2012))

WINDOW_PREVIEW_NAME = "Preview"

# Grille
GRID_SIZE = 3
SYMBOL = {
    'P1' : 'X',
    'P2' : 'O',
    'empty' : ' ',
    'unknow' : '?'
}
