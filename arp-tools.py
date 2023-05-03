import socket as socket


class ARP:
    def __init__(self, interface):
        self.interface = interface

    def send(self, packets):
        sock = None
        try:
            with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0, None) as sock:
                try:
                    sock.bind((self.interface, 0))
                    for p in packets:
                        sock.send(p.to_bytes())
                except Exception as e:
                    print(f'Error using socket: {e}')
                finally:
                    sock.close()
        except Exception as e:
            print(f'Error creating socket: {e}')


class ARPPacket():
    def __init__(self, destination_address, source_address, operation, sender_hardware_address, sender_protocol_address, target_hardware_address, target_protocol_address):
        ''' Ethernet Frame '''
        ''' user defined '''
        self.destination_address = destination_address.replace(':', '')
        self.source_address = source_address.replace(':', '')
        ''' static '''
        self.type = format(2054, '04x')

        ''' ARP Protocol '''
        ''' user defined '''
        self.operation = format(operation, '04x')
        self.sender_hardware_address = sender_hardware_address.replace(':', '')
        self.sender_protocol_address = self._ip_str_to_hex(sender_protocol_address)
        self.target_hardware_address = target_hardware_address.replace(':', '')
        self.target_protocol_address = self._ip_str_to_hex(target_protocol_address)
        ''' static '''
        self.hardware_type = format(1, '04x')
        self.protocol_type = format(2048, '04x')
        self.hardware_address_length = format(6, '02x')
        self.protocol_address_length = format(4, '02x')

    def to_bytes(self):
        return bytes.fromhex(self.destination_address + self.source_address + self.type + self.hardware_type + self.protocol_type + self.hardware_address_length + self.protocol_address_length + self.operation + self.sender_hardware_address + self.sender_protocol_address + self.target_hardware_address + self.target_protocol_address)

    def _ip_str_to_hex(self, ip_address):
        ip = ''
        for chunk in ip_address.split('.'):
            ip += str(format(int(chunk), '02x'))
        return ip


class Client:
    def __init__(self):
        iface = 'wlx246511c68c84'
        arp = ARP(iface)

        destination_address = '1a:1a:1a:1a:1a:1a'
        source_address = '1b:1b:1b:1b:1b:1b'
        operation = 2
        sender_hardware_address = 'ff:ff:ff:ff:ff:ff'
        sender_protocol_address = '192.168.178.111'
        target_hardware_address = 'ff:ff:ff:ff:ff:ff'
        target_protocol_address = '192.168.178.112'
        pck_1 = ARPPacket(destination_address, source_address, operation, sender_hardware_address, sender_protocol_address, target_hardware_address, target_protocol_address)

        target_protocol_address = '192.168.178.113'
        pck_2 = ARPPacket(destination_address, source_address, operation, sender_hardware_address, sender_protocol_address, target_hardware_address, target_protocol_address)

        arp.send([pck_1, pck_2])


if __name__ == '__main__':
    Client()
