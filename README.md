Problem description:
Live chat application. Please create a simple application "Text chat" using Python as primary development tool 
(without an additional packages, only common pack). Requirements: should work on Windows without an additional configuration; 
chat should have at least two active members; GUI not required. Input data: user name or ID. Output data: chat console.
Desirable to provide your results (code base) using Git.

Solution:
Python 3.6. Since GUI is not required, we'll be using terminal(command prompt/power shell on Windows) for the chat app.
There are 2 programs. First we neet to start server on localhost and random port number(5000 will be free). For this task
we'll be using UDP. Then in another terminal window we will start client. It will connect to the server and allow us to join chat 
providing our nickname. Then we can write messages, until we will write "q", it will break the connection and we'll live the chat. 
We can add numerous of users, but in order to get all the messages we have to refresh(I didn't make "realtime" solution, 
'cos it seems to be platform dependent). 
