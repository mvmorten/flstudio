# name=Axiom 49

import transport

stop_button = 0x17
play_button = 0x18
record_button = 0x19

def OnMidiMsg(event):
	event.handled = False
	if event.data2 > 0:	
		if event.data1 == stop_button:
			transport.stop()
			event.handled = True
		if event.data1 == rewind_button:
			event.handled = True
		if event.data1 == fastforward_button:
			event.handled = True
		if event.data1 == play_button:
			transport.start()
			event.handled = True
		if event.data1 == record_button:
			transport.record()
			event.handled = True            

