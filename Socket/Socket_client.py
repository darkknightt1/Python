import socket
import os
import subprocess
import time
s = socket.socket()
host = '192.168.1.7'
port = 9999
while True:
    try:
        s.connect((host, port))
        print("Connected successfully!")
        break  # Break out of the loop if connection is successful
    except ConnectionRefusedError:
        print("Connection refused. Retrying in 5 seconds...")
        time.sleep(1)  # Wait for 5 seconds before retrying
    except Exception as e:
        print(f"An error occurred: {e}")
        break  # Exit the loop if an unexpected error occurs

while True:
    s.send(str.encode("2"))
    data = s.recv(1024)
    
    if len(data) > 0:
        received = data.decode("utf-8")

        s.send(str.encode("No obstacle"))
        print(received)
        
        '''
import socket
import sys


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end = "")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
'''





from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow, QApplication, QComboBox, QSlider
from PySide6.QtCore import Qt, QTimer, QElapsedTimer, QThread, Signal
import sys
import socket
import threading
import time
import cv2
import numpy as np
import struct
from flask import Flask, Response, render_template_string

global counter 
counter = 0
conn = None
# Flask app to serve the video stream
app = Flask(__name__)

data_dict = {}

def receive_frames(sock):
    while True:
        packet, addr = sock.recvfrom(65535)
        
        if len(packet) < 6:
            continue

        # Unpack the header
        frame_id, chunk_id, num_chunks = struct.unpack('!HHH', packet[:6])
        chunk_data = packet[6:]

        if frame_id not in data_dict:
            data_dict[frame_id] = [None] * num_chunks
        
        data_dict[frame_id][chunk_id] = chunk_data

        if all(data_dict[frame_id]):
            # All chunks received, reassemble
            buffer = b''.join(data_dict[frame_id])
            frame = np.frombuffer(buffer, dtype=np.uint8)
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

            if frame is not None:
                # Display frame using OpenCV
                cv2.imshow('TUTOBOT Stream', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                # Encode frame as JPEG for streaming
                _, jpeg = cv2.imencode('.jpg', frame)
                frame = jpeg.tobytes()
                
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            
            # Remove the frame from the dictionary
            del data_dict[frame_id]

    cv2.destroyAllWindows()
    sock.close()





def gen(sock):
    for frame in receive_frames(sock):
        yield frame

@app.route('/video_feed')
def video_feed():
    return Response(gen(sock), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TUTOBOT</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background: url('YOUR_BACKGROUND_IMAGE_URL') no-repeat center center fixed;
                background-size: cover;
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                text-align: center;
            }
            .content {
                max-width: 80%;
                background-color: rgba(0, 0, 0, 0.5);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            }
            .video-stream {
                width: 100%;
                height: auto;
                border: 2px solid white;
                border-radius: 10px;
                margin-bottom: 20px;
            }
            .description {
                text-align: left;
            }
            h1 {
                margin-bottom: 10px;
            }
            p {
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <img class="video-stream" src="/video_feed" alt="Video Stream">
            <div class="description">
                <h1>Welcome to TUTOBOT</h1>
                <p>TUTOBOT is an advanced robot designed to revolutionize the experience of visiting museums and art galleries. Acting as a knowledgeable and engaging tour guide, TUTOBOT provides visitors with detailed information about exhibits, art pieces, and historical artifacts. It ensures that every visitor, regardless of their background or prior knowledge, leaves with a deeper understanding and appreciation of the displayed items.</p>
                <p>TUTOBOT is equipped with advanced AI technology, allowing it to interact with visitors in a natural and intuitive manner. It can answer questions, provide additional context, and even offer personalized recommendations based on the visitor's interests. This makes each tour unique and tailored to the individual.</p>
                <p>TUTOBOT can work in any museum or art gallery and interact with any visitor, thanks to its ability to speak multiple languages. Its computer vision capabilities enable it to identify exhibits and provide relevant information accordingly. Additionally, TUTOBOT is equipped with video streaming capabilities, allowing for real-time monitoring and ensuring smooth operation throughout the tour.</p>
                <p>Whether you are a history buff, an art lover, or just a curious visitor, TUTOBOT is here to guide you through a journey of discovery and learning. Join TUTOBOT on an unforgettable tour and see the museum in a whole new light.</p>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

class FlaskThread(QThread):
    def run(self):
        app.run(host='0.0.0.0', port=8000)



def start_streaming():
    # Initialize and bind the socket only when starting streaming
    global sock
    host='0.0.0.0'
    port=8844
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    for _ in receive_frames(sock):
        pass
 
def button4_clicked():# streaming button
    print("Awwww4   !")
    global counter
    counter+=1
    button_4.setEnabled(False)
    if counter == 1: #only the first time
        #flask_thread = FlaskThread()
        #flask_thread.start()
        pass

    streaming_thread = threading.Thread(target=start_streaming)
    streaming_thread.start()

app = QApplication(sys.argv)
window = QMainWindow()

button_4 = QPushButton("VIDSTREAM")
button_4.setFont(QFont("Helvetica Neue", 16, QFont.Bold))
button_4.setFixedSize(140, 60)
button_4.setStyleSheet("""
    QPushButton {
        background-color: blue;
        color: white;
        border-radius: 15px;
        padding: 10px;
    }
    QPushButton:disabled {
        background-color: #9E9E9E;
        color: #E0E0E0;
    }
""")
button_4.clicked.connect(button4_clicked)



window.setCentralWidget(mainWidget)
window.show()

# Run the application event loop
sys.exit(app.exec())