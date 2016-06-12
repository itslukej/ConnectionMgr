# ConnectionMgr
Python class for handling multiple sockets.

```
>>> from connectionmgr import ConnectionManager
>>> mgr = ConnectionManager()
>>> mgr.add("freenode")
>>> mgr.add("stuxnet", ssl=True)
>>> mgr.connect("freenode", "irc.freenode.net", 6667)
>>> mgr.connect("stuxnet", "irc.stuxnet.xyz", 6697)
>>> mgr.recv_all()
{
    'stuxnet': {
        'received': [
            u':gemini.stuxnet.xyz NOTICE * :*** Looking up your hostname...',
            u':gemini.stuxnet.xyz NOTICE * :*** Checking Ident'
        ], 
        'socket': <connectionmgr.socket_handler.Socket object at - >
    },
    'freenode': {
        'received': [
            u':gemini.stuxnet.xyz NOTICE * :*** Looking up your hostname...',
            u':gemini.stuxnet.xyz NOTICE * :*** Checking Ident'
        ], 
        'socket': <connectionmgr.socket_handler.Socket object at - >
    }
}
```

##Use of the socket class

```
>>> socket.recv()
[u':gemini.stuxnet.xyz NOTICE * :*** Found your hostname']
>>> socket.socket
<ssl.SSLSocket object at 0x7fbd48631488>
>>> socket.send("Something")
>>> socket.recv()
[u':gemini.stuxnet.xyz NOTICE * :*** No Ident response']
```

socket.send automatically appends "\r\n" to the message being sent to the server.
socket.recv automatically splits the received message by "\r\n"
