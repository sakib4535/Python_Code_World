import time


class Packet:
    def __init__(self, data):
        self.data = data


class Alice:
    def __init__(self):
        self.packets = []

    def create_packet(self, data):
        self.packets.append(Packet(data))

    def has_packets(self):
        return len(self.packets) > 0

    def get_next_packet(self):
        return self.packets.pop(0)


class InternetProcess:
    def __init__(self, alice, bob):
        self.alice = alice
        self.bob = bob

    def check_alice(self):
        if self.alice.has_packets():
            packet = self.alice.get_next_packet()
            self.bob.receive_packet(packet)

    def check_bob(self):
        packet = self.bob.check_for_packet()
        if packet:
            print("Bob received packet:", packet.data)


class Bob:
    def __init__(self):
        self.packet = None

    def receive_packet(self, packet):
        self.packet = packet

    def check_for_packet(self):
        packet = self.packet
        self.packet = None
        return packet

with open("packets.txt", "r") as f:
    alice = Alice()
    for line in f:
        alice.create_packet(line.strip())

bob = Bob()
internet = InternetProcess(alice, bob)

while True:
    internet.check_alice()
    internet.check_bob()
    time.sleep(2)

