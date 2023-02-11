# MiTMattack
Man in the middle attack, using two Raspberry Pi 0 w's. One which connects to a keyboard, logs the input and then passes the keypress via serial connection to the second Pi, which is connected to the target computer, simulating a keyboard.

This attack renders most anti-virus useless as the data and malicious program would never interact directly with the client computer. However, this does mean that physical access to the target maschine in it's place of use. This project has been written completely as a Proof of Concept and in no way do I take responsiblity for people using the code maliciously.
