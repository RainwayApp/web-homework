# Take-home assignment: remote gamepad display

Thank you for your interest in a position at Rainway!

This assignment involves two things we love at Rainway: gamepads and streaming data.

In this assignment, you will create a small web applet that displays the state of a game controller, as streamed over a WebSocket connection.

## Specification

### User interface

The applet UI consists of only one view, containing: a URL input field, a "Connect" button, a "Disconnect" button, and a game controller display widget.

The **URL input field** specifies the WebSocket server URL to connect to. Its value defaults to `wss://homework.rain.gg:8765`, which is the URL to our gamepad data streaming server.

When the user clicks the **"Connect" button**, the app connects to the WebSocket server specified in the URL input field, and begins displaying the received gamepad data on the widget.

When the user clicks the **"Disconnect" button**, the app closes the connection and stops displaying gamepad data from the server.

The **game controller display widget** has an [Xbox-style](https://images-na.ssl-images-amazon.com/images/I/71WX6wVepIL._AC_SL1500_.jpg) shape and layout.
The only moving parts in this assignment are the _two thumbsticks_ and the _A, B, X, and Y buttons_.
In response to inputs, the thumbsticks should move around to reflect the coordinates received, and the buttons should light up whenever the incoming data says they are being pressed.
(You can display the other features of the gamepad at whichever level of detail you want. Feel free to grab free assets off the Internet to work with.)

**Tip:** For both thumbsticks, clearly display the circular "knob" of the stick moving around in its circular "slot", so that it's obvious where the neutral position is.

### The server

This repository includes the gamepad server, written in Python 3. To run it, use `pip3 install websockets` and then `python3 server.py [host] [port]`.

Our gamepad data server will immediately begin streaming 60 messages per second upon connection. Each message describes the current state of the gamepad.
Your application should capture these messages and visually reflect the described gamepad state in the _game controller display widget_.

Each message is a JSON-encoded object, shaped like this:

```
{
  "thumbsticks": {
    "left": {"x": 0.875, "y": 0.997},
    "right": {"x": 0.314, "y": -0.819}
  },
  "buttons": {
    "a": false,
    "b": true,
    "x": false,
    "y": false
  }
}
```

* For each thumbstick, `x` is the current horizontal position from -1.0 (left) to 1.0 (right), and `y` is the vertical position from -1.0 (up) to 1.0 (down).

* For each button, `true` indicates that it is currently being pressed, and `false` indicates that it is not currently being pressed.

**Note:** The server stops sending data after 60 seconds. You don't have to handle this gracefully.

## Rules

1. You can use third-party software, frameworks, templates, and free assets all you like, so long as your solution is your own work. **React and TypeScript** are a plus. Just make sure to properly credit what you use, and obey licenses.
2. The visuals are all up to you. If it looks pretty, that's a bonus! But functional is fine: we will mainly judge your code.
3. When you're done, push your solution to a repo under your personal github account and send us an email linking us to it.
4. Include instructions for how to build (if appropriate) and run your solution.
5. If you have any more questions before or while crafting your solution, don't hesitate to get in touch with us.
6. Have fun!

## Bonus

Try hooking up your display widget to _real_ gamepad data using the [Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API)!

See [gamepad-tester.com](https://gamepad-tester.com/) for inspiration.
