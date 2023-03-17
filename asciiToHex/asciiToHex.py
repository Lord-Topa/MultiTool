import socket

HOST =  "127.0.0.1"
PORT = 6374

# This function takes in a socket as a parameter it then 
# uses a loop to continously get data from that socket in 
# the form of 1024 'chunks'. Stops retreiving data when
# a chunk comes in with a size below 1024. It then uses
# the chunks to reconstruct all of the data and returns it.
def recvall(sock):
    BUFFER_SIZE = 1024
    data = b''
    while True:
        chunk = sock.recv(BUFFER_SIZE)
        data += chunk
        if len(chunk) < BUFFER_SIZE:
            break
    return data

# Create socket and bind it, then accept connection when it comes in.
# Receive the message to be translated, translate it. Create a new 
# message for returning that has the length of the translated 
# message followed by a delimiter and then the translated message, 
# send it.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = recvall(conn)
            translatedData  = data.hex()
            translationLength = len(translatedData)
            fullMessage = str(translationLength) + "!0!" + translatedData
            print("\ndata recv: \n" + data.decode('utf-8') + " \nsending back: " + translatedData)
            if not data:
                break
            conn.sendall(fullMessage.encode())

print('PROGRAM CLOSING')


