# name=Axiom 49

import transport

loop_button = 0x14
rewind_button = 0x15
fastforward_button = 0x16
stop_button = 0x17
play_button = 0x18
record_button = 0x19

def OnControlChange(event):
	event.handled = False
	if event.data2 > 0:	
		if event.data1 == loop_button:
			transport.globalTransport(113, 1)
			event.handled = True
		if event.data1 == stop_button:
			transport.stop()
			event.handled = True
		if event.data1 == rewind_button:
			transport.setSongPos(0)
			event.handled = True
		if event.data1 == fastforward_button:
			transport.setSongPos(1)
			event.handled = True
		if event.data1 == play_button:
			transport.start()
			event.handled = True
		if event.data1 == record_button:
			transport.record()
			event.handled = True			

