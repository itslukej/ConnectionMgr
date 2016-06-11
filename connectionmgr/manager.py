from .socket_handler import Socket

class ConnectionManager(object):
    def __init__(self):
        self.connections = {}
    def add(self,name,ssl=False, ipv6=False, proxy=False, proxy_host=None, proxy_port=None, proxy_type=None):
        self.connections[name] = Socket(ipv6,ssl,proxy,proxy_host,proxy_port,proxy_type)
    def connect(self,name,host,port):
        if name in self.connections.keys():
            self.connections[name].connect((host, port))
        else:
            raise ValueError("{0} does not exist.".format(name))
    def recv_all(self):
        recv = {}
        for connection_name, connection in self.connections.items():
            recv[connection_name] = {"socket": connection, "received": connection.recv()}
        return recv
    def recv(self,name):
        if name in self.connections.keys():
            return {"socket": self.connections[name], "received": self.connections[name].recv()}
        else:
            raise ValueError("{0} does not exist.".format(name))
