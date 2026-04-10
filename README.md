# Overview

I programmed this chat room project to practice using one of many cool things that python can do. It allows users to chat between each other using the internet or any other connection type like bluetooth.

This program connects users through the internet and allows users to enter with a username and chat with others. There are functions that detect key words like time, weather, users, and help, so that when users ask for the time for example, the server responds with the time to their message. The chatroom is started when the server file is run in either the vscode or command line, and all users run the client file. I have omitted my ip address from the code and it relies on users to use the same ip network to connect because my computer had a firewall which would not allow connection from other ips like a server would.

This code was written so I could have a fun project that would allow me to write messages securely to others without going through a mainstream chatting software. 

[Software Demo Video](https://youtu.be/mso7g_B6UEY)

# Network Communication

This project connects user through the server that handles messages.

I used tcp for this chat project and the port was just a random number (20598).

Messages are sent as bytes and encoded and decoded using ascii.

# Development Environment

This project was created using python and tcp. It was coded and can be hosted from vscode.

I used python which is a simple and widely used language for all sorts of projects. I imported things like socket for tcp connections and threading for multiple users.

# Useful Websites

* [Youtube](https://www.youtube.com/watch?v=bwTAVGg_kVs)
* [Python Documents](https://docs.python.org/3/howto/sockets.html)

# Future Work

* GUI for ease of use outside of command line
* Dynamic server responses like real weather rather than prewritten ones
* Move it online for users to connect from any network