import pyxhook 
import os
import scapy.all as scapy
from time import sleep
  
# https://www.geeksforgeeks.org/design-a-keylogger-in-python/

#? Why, yes, this is a glorified keylogger and man in the middle attack made into a minetest mod.

# The EXTREMELY STUPID way to enable scapy:
# sudo setcap cap_net_raw=eip $(readlink -f $(which python))
#! THIS WILL ALLOW ANY PYTHON PROGRAM TO CREATE FAKE PACKETS ON YOUR SYSTEM !

ip = "127.0.0.1"
# This is the target (server) port. It will be used as a nand gate and mutated.
port = 30000
ORIGIN_port = port

TARGET_FPS = 60.0

delta = 1.0 / TARGET_FPS


# Get the port of the client. The client must be connected to the server for this to work.
# This only works for one client.
x = os.popen("netstat -n --udp --listen -p 2>/dev/null | grep min").read()
if (x == ""):
  print("ERROR! Could not detect minetest client!")
  exit()
x = x.splitlines()
for i in x:
  if "0.0.0.0:" + str(port) not in i:
    x = i
x = x.split()[3]
x = x.split(":")[1]
if not x.isnumeric():
  print("ERROR! Could not get minetest client port!")
  exit()
port = int(x)


# pid         peer  chan
#[0, 1, 2, 3][4, 5][6 ]

#! HEADER 7 bytes.

# protocol ID
t = int("0x4f457403", 16)
w = bytearray()
w.extend(t.to_bytes(length=4, byteorder='big'))

# peer (is server)
w.extend((1).to_bytes(length=2, byteorder='big'))

# channel
w.extend((2).to_bytes(length=1, byteorder='big'))

#! Packet type.

# type
w.extend((1).to_bytes(length=1, byteorder='big'))

# control type
w.extend((0).to_bytes(length=1, byteorder='big'))

# Instruction
z = int("0x2F", 16)
w.extend(z.to_bytes(length=1, byteorder='big'))

# Chat version
w.extend((1).to_bytes(length=1, byteorder='big'))

# Message type
w.extend((1).to_bytes(length=1, byteorder='big'))

# I honestly have no idea
w.extend((1).to_bytes(length=2, byteorder='big'))
w.extend((0).to_bytes(length=2, byteorder='big'))
w.extend((12).to_bytes(length=2, byteorder='big'))

# Pad this thing because it crashes for literally no reason
w.extend(bytes("things to do" + "aaaa","utf-16be"))



# w.extend(bytes("hi","utf-8"))
# w.extend(bytes("hi","utf-8"))

# w.extend(bytes("1234567","utf-8") + b'\x00')



# w.extend(bytes("hi\0","utf-8"))

# w.extend(bytes("hi\0","utf-8"))

# w.extend((0).to_bytes(length=1, byteorder='big'))





# w.extend(bytes("0","utf-8"))




#* ConnectionReceiveThread::receive

#* ConnectionReceiveThread::processPacket


# w.extend((0).to_bytes(length=1, byteorder='big'))

# w.extend((2).to_bytes(length=1, byteorder='big'))

# w.extend(bytes("\0\0\0\0","utf-8"))


print("sending")

# print(ORIGIN_port)
# print(port)
# print(w)

# conf.L3socket = L3RawSocket

_ip = scapy.IP(dst = "127.0.0.1", src = "127.0.0.1")
_udp = scapy.UDP(sport = ORIGIN_port, dport = port)

scapy.send(_ip/_udp/w)

# def OnKeyPress(event): 
#     print('{}_down'.format(event.Key))

# def OnKeyUp(event): 
#     print('{}_up'.format(event.Key))

# new_hook = pyxhook.HookManager() 
# new_hook.KeyDown = OnKeyPress 
# new_hook.KeyUp = OnKeyUp


# new_hook.HookKeyboard() 
# try: 
#     new_hook.start()
# except KeyboardInterrupt: 
#     pass
# except Exception as ex: 
#     msg = 'Error while catching events:\n  {}'.format(ex) 
#     pyxhook.print_err(msg) 
#     print("I suck at python :D")


    
