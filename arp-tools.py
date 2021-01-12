import socket as socket

class ARP:
    def __init__(self):
        pass

    def send(self, packet):
        try:
            s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0, None)
            s.bind(('wlan0', 0))
            s.send(packet.to_bytes())
            s.close()
        except Exception as e:
            print(f'{e}')


class ARPPacket():
    def __init__(self, destination_address, source_address, operation, sender_hardware_address, sender_protocol_address, target_hardware_address, target_protocol_address):
        ''' Ethernet Frame '''
        ''' user defined '''
        self.destination_address = destination_address
        self.source_address = source_address
        ''' static '''
        self.type = format(2054, '04x')

        ''' ARP Protocol '''
        ''' user defined '''
        self.operation = operation
        self.sender_hardware_address = sender_hardware_address
        self.sender_protocol_address = sender_protocol_address
        self.target_hardware_address = target_hardware_address
        self.target_protocol_address = target_protocol_address
        ''' static '''
        self.hardware_type = format(1, '04x')
        self.protocol_type = format(2048, '04x')
        self.hardware_address_length = format(6, '02x')
        self.protocol_address_length = format(4, '02x')

    def to_bytes(self):
        return bytes.fromhex(self.destination_address + self.source_address + self.type + self.hardware_type + self.protocol_type + self.hardware_address_length + self.protocol_address_length + self.operation + self.sender_hardware_address + self.sender_protocol_address + self.target_hardware_address + self.target_protocol_address)



class Client:
    def __init__(self):
        arp = ARP()
        destination_address = '1a1a1a1a1a1a'
        source_address = '1b1b1b1b1b1b'
        operation = format(2, '04x')
        sender_hardware_address = 'ffffffffffff'
        sender_protocol_address = format(192, '02x') + format(168, '02x') + format(178, '02x') + format(1, '02x')
        target_hardware_address = 'ffffffffffff'
        target_protocol_address = format(192, '02x') + format(168, '02x') + format(178, '02x') + format(2, '02x')
        pck = ARPPacket(destination_address, source_address, operation, sender_hardware_address, sender_protocol_address, target_hardware_address, target_protocol_address)

        arp.send(pck)


if __name__ == '__main__':
    Client()
