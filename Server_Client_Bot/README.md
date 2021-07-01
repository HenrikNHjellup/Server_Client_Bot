# README

How to use the server and client:

1. All files must be in the same directory on your computer!

2. You start server.py by navigating to the directory on your computer using a CLI such as cmd.exe on Windows or
terminal on your Linux or OSX machine (The program has mainly been tested on Windows, so that is recommended).

3. Type "py server.py {PORT}" without the braces, where {PORT} is your desired port (You can use 1234 if nothing else comes to mind).

4. The server program opens, and you are met with an input asking for a host name.
   Write your desired host name, such as "Host", "HOST", "John", "Beth" or anything else.

5. Open another a CLI on another window and type "py client.py {IP} {PORT} {BOT}" without the braces,
   where {IP} is your desired IPv4 address (Use 127.0.0.1 or localhost if connected locally),
   {PORT} is your desired IPv4 port (Must be same as server.py port),
   {BOT} is your desired client BOT (Must be one of the available bots. Type "py client.py --bots" for available bots).

6. You are now ready to send messages to the bots, and receive their replies.

7. When you are done with the conversation, simply type "bye" somewhere, and all

Settings:

Change num_of_bots in server.py for your desired max amount of bots.
