import socket as socket


class RAW:
    def __init__(self, interface):
        self.interface = interface

    def send(self, packets):
        sock = None
        try:
            with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0, None) as sock:
                try:
                    sock.bind((self.interface, 0))
                    for p in packets:
                        sock.send(p)
                except Exception as e:
                    print(f'Error using socket: {e}')
                finally:
                    sock.close()
        except Exception as e:
            print(f'Error creating socket: {e}')