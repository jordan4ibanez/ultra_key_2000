# ultra_key_2000
 A MASSIVE hackjob.

-----

### What is this?

-----

For a long time I've seen people ask, "How do we bind any key to anything in minetest?!"

The answer was: No.

Well, I decided on October 5th 2024 that was probably not a very good answer.

So this absolute security monstrosity was fired into existence.

This thing, is a glorified keylogger and man in the middle attack, which injects your client with keystrokes as if the server is sending it over a mod channel.

This thing does not detect window focus. As long as it's running, it's detecting and sending your keystrokes to your client if it's connected to a server.

-----

### This is a test of: if we can

### This is not: a solution

-----

# **NEVER USE THIS. THIS IS A PROOF OF CONCEPT.**

-----

needs:

python 3.12+ (probably)

```
pip3 install python3-xlib scapy
```

Steps:

1.) Enable the client mod. I'm not telling you how to do this.

2.) Enable mod channels. I'm not telling you how to do this.

3.) Connect to your server, which must be running the server mod.

4.) Start the python script.

5.) If any of these steps confused you, stop what you're doing right now.

