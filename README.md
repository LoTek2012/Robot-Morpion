# Robot-Morpion

A LEGO Mindstorms NXT robot that uses a camera to analyze a tic-tac-toe board, determine the best move, and play autonomously.

## Overview

Robot-Morpion is split into two components running on separate computers:

- **Server:** captures images from the camera and sends them to the client over a network socket.
- **Client:** analyzes the images with OpenCV, determines the game state and best move, and controls the NXT motors using `nxt-python`.

> [!IMPORTANT]
> **Legacy environment:** The server was originally designed for Windows XP and Python 3.4.4. Running it on a modern operating system may require compatible versions of Python and its dependencies.

## Hardware

- Many LEGO building parts
- A compatible camera (I recommend the *LEGO MovieMaker USB Camera*/*RCX Digital Colour Camera*)
- Two computers: one for the server and one for the client
- A network connection between the two computers

## Project resources

### Building instructions

See [`docs/building-instructions.pdf`](docs/building-instructions.pdf).

### Parts list

See [`docs/parts-list.csv`](docs/parts-list.csv).

### CAD model

The LEGO model was created with BrickLink Studio. The project file is [`Robot-Morpion.io`](model/Robot-Morpion.io).

## Software requirements

The client and server have separate dependency lists:

- **Client:** `client/requirements.txt`
- **Server:** `server/requirements.txt`

Use the dependency file appropriate to the component and Python environment you are setting up. The server's legacy Windows XP environment uses Python 3.4.4; if you use a newer system, check that the Python version and library versions are compatible.

> [!NOTE]
> The version of ``opencv-python`` for ``Python 3.4.4`` (the last version for XP) no longer exist on PyPi. You can download it [here](https://dashboard.stablebuild.com/pypi-deleted-packages/pkg/opencv-python/3.2.0.8)

## Configuration

Configure the environment files before starting either component:

1. Copy `client/.env.exemple` to `client/.env`.
2. Copy `server/.env.exemple` to `server/.env`.
3. Set the values required by each component in its `.env` file.

The exact variable names and required values are defined by the corresponding `.env.exemple` files.

## Running the program

Start the **server first**, then start the client. The client needs the server to be running in order to connect and receive images.

### Server

The server is located in `server/` and should run on a computer different from the client computer.

Its responsibilities are to:

1. Capture images using the connected camera.
2. Send the images to the client through a network socket.

### Client

The client is located in `client/`. Its responsibilities are to:

1. Request and receive camera images from the server through a network socket.
2. Analyze the images with OpenCV to determine the current board state.
3. Determine the best move.
4. Control the NXT motors using `nxt-python` to execute the move.

## License

This project is released under the MIT License. See [`LICENSE`](LICENSE) for more informations.
