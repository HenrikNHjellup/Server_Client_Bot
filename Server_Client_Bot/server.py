import socket
import itertools
import random
import string
import time
import sys
import re

"""
CHEKCING INPUT VALIDITY
"""
n = len(sys.argv)
if n != 2:
    print("Cannot start client. Exactly one (1) parameter must be given.")
    print("To run, type: py server.py 'port', where 'port' is your desired IPv4 port.")
    print("You can use 1234 if nothing else comes to mind.")
    sys.exit()

PORT = sys.argv[1]

PORT_regex_test = '^()([1-9]|[1-5]?[0-9]{2,4}|6[1-4][0-9]{3}|65[1-4][0-9]{2}|655[1-2][0-9]|6553[1-5])$'
if not re.search(PORT_regex_test, PORT):
    print("Cannot start client. Port format not valid.")
    sys.exit()

PORT = int(PORT)

"""
PREPARING SERVER AND MAKING SOCKETS
"""

print("///////////////// SERVER /////////////////////\n")

host_name = input("What is your host name? ")

HEADER_LENGTH = 10

# Creating socket, binding "all IPs" to port, listening
server_socket = socket.socket()
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen()

# Creating lists and variables
sockets_list = [server_socket]
clients = []
address_list = []
bot_name_list = []

#Max amount of bots
num_of_bots = 4
#Bot counter
bot_nr = 0

print("The server will be accepting ", num_of_bots, " bots unless you write 'no' or 'n' on input.")
print("For simplicity, you can connect ", num_of_bots, " bots and then press enter ", num_of_bots, " times.")
time.sleep(0.5)

def loading_animation():
    n_points = 50
    points_l = [ '=' * i + ' ' * (n_points - i) + '\r' for i in range(n_points) ]
    cond = True
    dot_counter = 0
    for points in itertools.cycle(points_l):
        print(points, end='')
        time.sleep(0.01)
        dot_counter += 1
        if dot_counter == 251:
            cond = False
        if not cond:
            break

loading_animation()

print("Creating socket...\n")
time.sleep(float((random.randrange(0, 10))/10)*3)

print("""          .?7777777777$.            
          777..77777777$+           
         .77    777777$$$    """)
time.sleep(float((random.randrange(0, 10))/10))
print("""         .777 .777777$$$$           
         .777777777$$$$$$           
         --------:77$$$$$$   """)
time.sleep(float((random.randrange(0, 10))/10))
print("""  .7777777777777$$$$$$$.=======.  
 77777777777777$$$$$$$$.========  
777777777777$$$$$$$$$$$.========= """)
time.sleep(float((random.randrange(0, 10))/10))
print("""7777777777$$$[PYTHON]$$$.=========
777$$$$.~~===[SOCKET]=====++++++++: """)
time.sleep(float((random.randrange(0, 10))/10))
print(""" 7$$$$$.===============++++++++++. 
 .,$$$$.=============++++++++++~.            
         .=========------           """)
time.sleep(float((random.randrange(0, 10))/10))
print("""         .=======+++..+++           
         .=======++.  .++           """)
time.sleep(float((random.randrange(0, 10))/10))
print("""          ,======++++,,++,           
          ..====++++++=.            
            .......~+=.     
""")


print("ACCEPTING BOTS...")

"""
SENDING AND RECEIVING MESSAGES
"""

while bot_nr < num_of_bots:
    # Accepting connections and appending to lists
    connection, address = server_socket.accept()
    sockets_list.append(connection)
    clients.append(connection)
    address_list.append(address)

    # Receiving bot name
    bot_name = clients[bot_nr].recv(HEADER_LENGTH)
    bot_name_list.append(bot_name)
    print("\nConnection from: ", bot_name.decode())
    bot_nr += 1
    inpt = input("More bots? y/n ")
    if inpt.lower() == "n" or inpt.lower() == "no":
        break
print("NOT ACCEPTING MORE BOTS")

while True:
    msg = input(f"{host_name}: ")
    # Remove punctuation
    msg_str = msg.translate(str.maketrans('', '', string.punctuation))
    # Make list
    srv_msg_list = msg_str.split()
    for word in srv_msg_list:
        if word.lower() == "bye":
            server_socket.close()
            sys.exit()
    if len(msg) < 1:
        continue
    for client in clients:
        client.send(msg.encode())
    for i in range(len(clients)):
        rpl = clients[i].recv(1024)
        print(f"{bot_name_list[i].decode()}: {rpl.decode()}")
    print()

