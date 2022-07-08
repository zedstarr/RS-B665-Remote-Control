# RS-B665-Remote-Control

### Browser-based remote control of a Technics RS-B665 Cassette Tape Deck using a Raspberry Pi/Node-RED/relays.

Requires hardware hacking of the cassette deck - soldering a lead onto the control panel's main board connector and replicating the internal resistor chain to create appropraite REW/PLAY/FF/STOP signals to the deck.

See https://bit.ly/RS-B665 for full details.
<br/><br/>  

I appreciate the Pi is overkill to control a few relays but it's also streaming USB audio from a couple of other audio components too.
( https://zedstarr.com/2021/01/11/streaming-vinyl-audio-around-the-house-with-raspberry-pi-and-icecast-darkice/ )  
<br/><br/>  

Also contained in the OPL directory is some Psion Series 3a OPL to connect wirelessly to the Raspberry Pi and send R,P,F or S to REW/PLAY/FF or STOP the tape deck.

Requires 3Link RS-232, 232/TTL converter and NodeMCU as AT-command/WiFi bridge to allow the 3a to talk to the Pi over the network.

See https://bit.ly/3aRSB665 for full details.
