import socket

HOST =  "127.0.0.1"
PORT = 6374

def recvall(sock):
    BUFF_SIZE = 1024
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            #either 0 or end of data
            break
    return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            #data = conn.recv(10)
            data = recvall(conn)
            #print(data)
            #newData = "123"
            newData  = data.hex()
            dataLength = len(newData)
            fullMsg = str(dataLength) + "!0!" + newData
            #newData = "4C 6F 72 65 6D 20 69 70 73 75 6D 20 64 6F 6C 6F 72 20 73 69 74 20 61 6D 65 74 2C 20 63 6F 6E 73 65 63 74 65 74 75 72 20 61 64 69 70 69 73 63 69 6E 67 20 65 6C 69 74 2C 20 73 65 64 20 64 6F 20 65 69 75 73 6D 6F 64 20 74 65 6D 70 6F 72 20 69 6E 63 69 64 69 64 75 6E 74 20 75 74 20 6C 61 62 6F 72 65 20 65 74 20 64 6F 6C 6F 72 65 20 6D 61 67 6E 61 20 61 6C 69 71 75 61 2E 20 55 74 20 65 6E 69 6D 20 61 64 20 6D 69 6E 69 6D 20 76 65 6E 69 61 6D 2C 20 71 75 69 73 20 6E 6F 73 74 72 75 64 20 65 78 65 72 63 69 74 61 74 69 6F 6E 20 75 6C 6C 61 6D 63 6F 20 6C 61 62 6F 72 69 73 20 6E 69 73 69 20 75 74 20 61 6C 69 71 75 69 70 20 65 78 20 65 61 20 63 6F 6D 6D 6F 64 6F 20 63 6F 6E 73 65 71 75 61 74 2E 20 44 75 69 73 20 61 75 74 65 20 69 72 75 72 65 20 64 6F 6C 6F 72 20 69 6E 20 72 65 70 72 65 68 65 6E 64 65 72 69 74 20 69 6E 20 76 6F 6C 75 70 74 61 74 65 20 76 65 6C 69 74 20 65 73 73 65 20 63 69 6C 6C 75 6D 20 64 6F 6C 6F 72 65 20 65 75 20 66 75 67 69 61 74 20 6E 75 6C 6C 61 20 70 61 72 69 61 74 75 72 2E 20 45 78 63 65 70 74 65 75 72 20 73 69 6E 74 20 6F 63 63 61 65 63 61 74 20 63 75 70 69 64 61 74 61 74 20 6E 6F 6E 20 70 72 6F 69 64 65 6E 74 2C 20 73 75 6E 74 20 69 6E 20 63 75 6C 70 61 20 71 75 69 20 6F 66 66 69 63 69 61 20 64 65 73 65 72 75 6E 74 20 6D 6F 6C 6C 69 74 20 61 6E 69 6D 20 69 64 20 65 73 74 20 6C 61 62 6F 72 75 6D";
            print("data recv: " + data.decode('utf-8') + " sending back: " + newData)
            if not data:
                break
            conn.sendall(fullMsg.encode())


