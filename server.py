import asyncio
import json
import websockets
import sys
from math import hypot, sin

# Buttons: spell out "RAINWAY" in Morse code, then do a little dance.
pattern = 'x xxx x   y yyy   b b   aaa a   x xxx xxx   y yyy   bbb b bbb bbb   axybaxyb       '

# Send 60 seconds of synthetic gamepad data.  
async def send_gamepad_data(ws, path):
    t = 0.0
    def f(x): return 0.707 * sin(x)
    for i in range(60 * 60):
        await asyncio.sleep(1/60)
        t += 1/60
        b = pattern[int(7*t) % len(pattern)]
        x1, y1 = f(+1.0*t), f(-1.4*t)
        x2, y2 = f(-1.3*t), f(+0.6*t)
        json_string = json.dumps({ 
          'thumbsticks': {
            'left':  {'x': x1, 'y': y1},
            'right': {'x': x2, 'y': y2},
          },
          'buttons': {k: b == k for k in 'abxy'}
        })
        await ws.send(json_string)

if len(sys.argv) <= 2:
  sys.exit('usage: python3 server.py [host] [port]')

host = sys.argv[1]
port = int(sys.argv[2])
start_server = websockets.serve(send_gamepad_data, host, port)
print("Started server at '%s', port %d." % (host, port))
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

