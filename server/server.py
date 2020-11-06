from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

# GLOBAL CONSTANTS
HOST = 'localhost'
PORT = 5500
BUFSIZ = 512
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10

# GLOBAL VARIABLES
persons = []

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def broadcast():



def wait_for_connection():
    """
    Wait for connection from new clients, start new thread once connected
    :param server: SOCKET
    :return: None
    """
    run = True
    while run:
        try:
            client, client_address = server.accept()
            person = Person(addr, client)
            persons.append(person)
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[FAILURE]", e)
            run = False
    print("SERVER CRASHED")


def client_communication(person):
    """
    Thread to handle all messages from client
    :param client: SOCKET
    :return: None
    """

    client = person.client
    addr = person.addr

    # Get persons name
    name = client.recv(BUFSIZ).decode("utf8")
    msg = f"{name} has joined the chat!"
    broadcast(msg)

    while True:
        msg = client.recv(BUFSIZ)
        if msg == bytes("{quit}", "utf8"):
            client.send(bytes("{quit}", "utf8"))
            client.close()
            person.remove(person)

        else:




if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS) # listen for connections
    print("[STARTED] Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
