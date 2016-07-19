# ConnectionMgr
Python class for handling multiple sockets.

```python
>>> from connectionmgr import ConnectionManager
>>> import zirc, ssl
>>> mgr = ConnectionManager()
>>> mgr.add("freenode", zirc.Socket())
>>> mgr.add("stuxnet", zirc.Socket(wrapper=ssl.wrap_socket))
>>> mgr.connect("freenode", "irc.freenode.net", 6667)
>>> mgr.connect("stuxnet", "irc.stuxnet.xyz", 6697)
>>> mgr.recv_all()
{
    'stuxnet': {
        'received': [
            u':gemini.stuxnet.xyz NOTICE * :*** Looking up your hostname...',
            u':gemini.stuxnet.xyz NOTICE * :*** Checking Ident'
        ], 
        'socket': <- object at - >
    },
    'freenode': {
        'received': [
            u':gemini.stuxnet.xyz NOTICE * :*** Looking up your hostname...',
            u':gemini.stuxnet.xyz NOTICE * :*** Checking Ident'
        ], 
        'socket': <- object at - >
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
