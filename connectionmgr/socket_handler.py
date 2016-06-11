import socks, ssl as _ssl, socket 
class Socket(object):
    '''Handles receiving and sending data'''
    def __init__(self, ipv6=False, ssl=False, proxy=False, proxy_host=None, proxy_port=None, proxy_type=None):
        self.attachments = []

        if proxy:
            self.socket = socks.socksocket()
            self.socket.set_proxy(proxy_type, proxy_host, proxy_port)
        elif ipv6:
            self.socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        else:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if ssl and not proxy:
            self.socket = _ssl.wrap_socket(self.socket)
        self.connect = self.socket.connect
        self.close = self.socket.close
    def recv(self):
        self.part = ""
        self.data = ""
        while not self.part.endswith("\r\n"):
            self.part = self.socket.recv(2048)
            self.part = self.part.decode("UTF-8", "ignore")
            self.data += self.part
        self.data = self.data.splitlines()
        return self.data
    def printrecv(self):
        self.received_message = self.recv()
        for msg in self.received_message:
            print("[RECV] {0}".format(msg))
        return self.received_message
    def send(self, data):
        if type(data) is not str:
            data = data.decode("UTF-8")
        self.socket.send("{0}\r\n".format(data).encode("UTF-8"))
