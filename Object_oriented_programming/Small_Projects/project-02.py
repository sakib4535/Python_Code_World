"""Write a set of Python classes that can simulate an Internet application in
which one party, Alice, is periodically creating a set of packets that she
wants to send to Bob. An Internet process is continually checking if Alice
has any packets to send, and if so, it delivers them to Bob's computer, and
Bob is periodically checking if his computer has a packet from Alice, and,
if so, he reads and deletes it.
"""

""" 
Solution: 
In summary, we have three entities: Alice, Bob, and an Internet process that acts as a mediator between the two. 
Alice creates packets, the Internet process delivers them to Bob, and Bob receives and deletes the packets. 
We need to create a set of Python classes to simulate this scenario.
"""

import time

class Packet:
    def __init__(self, data):
        self.data = data

class Alice:
    def __init__(self):
        self.packets_to_send = []

    def create_packet(self, data):
        packet = Packet(data)
        self.packets_to_send.append(packet)

    def has_packets(self):
        return len(self.packets_to_send) > 0

class InternetProcess:    # Its working like a mediator between two person
    def __init__(self, alice, bob):
        self.alice = alice
        self.bob = bob

    def check_packets(self):
        if self.alice.packets_to_send:
            for packet in self.alice.packets_to_send:
                self.bob.receive_packet(packet)
            self.alice.packets_to_send = []

class Bob:
    def __init__(self):
        self.received_packets = []

    def receive_packet(self, packet):
        self.received_packets.append(packet)

    def check_packets(self):
        if self.received_packets:
            for packet in self.received_packets:
                print(f"Received the Packet from Alice: {packet.data}")


alice = Alice()
bob = Bob()
interent_process = InternetProcess(alice, bob)


alice.create_packet("Packing the American Documents")
alice.create_packet("Packing the Danish Documents")
alice.create_packet("packing the French Documents")

while True:
    interent_process.check_packets()
    bob.check_packets()
    time.sleep(2)




