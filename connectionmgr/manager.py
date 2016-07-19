def recv(sock):
    sock.buffer= ""
    while not sock.buffer.endswith("\r\n"):
        sock.buffer += sock.sock.recv(2048).decode("utf-8", errors="replace")
    sock.buffer = sock.buffer.strip().split("\r\n")
    return sock.buffer

class ConnectionManager(object):
    def __init__(self):
        self.connections = {}
    def add(self,name,socket_class):
        self.connections[name] = socket_class
    def connect(self,name,host,port):
        if name in self.connections.keys():
            self.connections[name]((host, port))
        else:
            raise ValueError("{0} does not exist.".format(name))
    def recv_all(self):
        recv = {}
        for connection_name in self.connections.keys():
            recv[connection_name] = self.recv(connection_name)
        return recv
    def recv(self,name):
        if name in self.connections.keys():
            return {"socket": self.connections[name].sock, "received": recv(self.connections[name])}
        else:
            raise ValueError("{0} does not exist.".format(name))
