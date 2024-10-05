import pyxhook 
import os
import scapy.all as scapy
from time import sleep
  
# https://www.geeksforgeeks.org/design-a-keylogger-in-python/

#? Why, yes, this is a glorified keylogger and man in the middle attack made into a minetest mod.
#! AND YES, you do have to give this script scapy priveleges.
#* No, I'm not telling you how to do this.


#! THIS IS ENOUGH OF A HACKJOB AS IT IS.
#! I AM NOT WRITING IN A WAY TO DETECT WHICH WINDOW IS IN FOCUS.
#! THIS THING IS GETTING EVERY KEYSTROKE.
#! SO YOU BEST NOT TYPE IN YOUR PASSWORD WHEN YOU'RE RUNNING THIS!!!

# This is the server you're playing on. If it's local 127.0.0.1
ip = "127.0.0.1"
ORIGIN_ip = "127.0.0.1"

# This is the target (server) port. It will be used as a nand gate and mutated.
port = 30000
ORIGIN_port = port

TARGET_FPS = 20.0

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

cache = []

#* Type: str
def fire():

  if len(cache) == 0:
     return

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

  # Instruction - Mod channel function pointer is at 0x57
  z = int("0x57", 16)
  w.extend(z.to_bytes(length=1, byteorder='big'))

  # This is extremely complex, we're basically forcing alternate packet intake LOL.

  # Encoding: (str_len + 1 [null term]) * 2 [probably]

  w.extend((14).to_bytes(length=2, byteorder='big'))
  w.extend(bytes("ultra_key_2000","utf-8"))

  w.extend((14).to_bytes(length=2, byteorder='big'))
  w.extend(bytes("ultra_key_2000","utf-8"))

  output = "-&-".join(cache)

  ll = (len(output))

  w.extend(ll.to_bytes(length=2, byteorder='big'))
  w.extend(bytes(output,"utf-8"))
  #* ConnectionReceiveThread::receive
  #* ConnectionReceiveThread::processPacket

  # print(ORIGIN_port)
  # print(port)
  # print(w)


  _ip = scapy.IP(dst = ORIGIN_ip, src = ip)
  _udp = scapy.UDP(sport = ORIGIN_port, dport = port)

  scapy.send(_ip/_udp/w)

  cache.clear()



def OnKeyPress(event): 
    cache.append('{}_down'.format(event.Key).lower())

def OnKeyUp(event): 
    cache.append('{}_up'.format(event.Key).lower())

new_hook = pyxhook.HookManager() 
new_hook.KeyDown = OnKeyPress 
new_hook.KeyUp = OnKeyUp


new_hook.HookKeyboard() 
try: 
    new_hook.start()
except KeyboardInterrupt: 
    pass
except Exception as ex: 
    msg = 'Error while catching events:\n  {}'.format(ex) 
    pyxhook.print_err(msg) 
    print("I suck at python :D")

while True:
   sleep(delta)
   fire()
   

    
