import socket
import random
import string
import itertools
import time
import sys
from bot import available_bots, interpret_msg, long_verb_list

"""
CHECKING INPUT VALIDITY
"""

n = len(sys.argv)
if n == 2 and sys.argv[1] == "--bots":
    print("Available bots: ", available_bots)

elif n != 4:
    print("Cannot start client. Exactly three (3) parameters must be passed.")
    print("To run, type: py clientFinal.py 'ip' 'port' 'bot'")
    print("Where 'ip' is your desired IPv4 address, 'port' is IPv4 port, and 'bot' is your desired bot.")
    print("For available bots, run script again like so: py client.py --bots")
    print("Exiting...")
    sys.exit()


"""
LOADING ANIMATIONS
"""

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



"""
PREPARING CLIENT AND MAKING SOCKETS
"""


print("///////////////// CLIENT /////////////////////")

IP = sys.argv[1]
PORT = int(sys.argv[2])
BOT = str(sys.argv[3])

HEADER_LENGTH = 10

if BOT not in available_bots:
    print("Could not find bot. Connect again...")
    sys.exit(-1)

client_socket = socket.socket()
client_socket.connect(("localhost", 1234))
client_socket.send(BOT.encode())


"""
SENDING AND RECEIVING MESSAGES
"""

round_counter = 0
suggestion_list = []

while True:
    # Decoding message
    msg = client_socket.recv(1024).decode()
    # Removing punctuation
    msg = msg.translate(str.maketrans('', '', string.punctuation))
    # Making message list
    msg_list = msg.split()

    # Appending verbs found in the message to the suggestion list
    for word in msg_list:
        if word.lower() == "bye":
            client_socket.close()
            sys.exit()
        print(word)
        for verb in long_verb_list:
            if word == verb or word == verb + "ing" or word == verb + "ning":
                suggestion_list.append(word)

    # If suggestion list is less than the number of rounds, append an "err" string
    if len(suggestion_list) <= round_counter:
        suggestion_list.append("err")

    # Making the reply
    print(suggestion_list)
    if round_counter == 0:
        reply = interpret_msg(suggestion_list[round_counter], None, BOT)
    else:
        reply = interpret_msg(suggestion_list[round_counter], suggestion_list[round_counter-1], BOT)


    print(msg)

    client_socket.send(reply.encode())
    print("Sending \"{}\"".format(reply))

    round_counter += 1
