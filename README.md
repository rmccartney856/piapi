# piapi

![pyapi logo](https://github.com/rmccartney856/pyapi/blob/master/media/logo.jpg)

Simple API with web interface using AJAX and direct HTTP commands to allow remote control of any Arduino or other serial device via a Raspberry Pi.

## Requirements

* `pip3 install cherrypy`
* `pip3 install pyserial`

## Installation and Run

1. `git clone https://github.com/rmccartney856/pyapi`
2. `cd PATH//pyapi`
3. `sudo python3 install.py`
4. `sudo reboot`

## Raspberry Pi Usage

1. Clone Repository to any directory on your Raspberry Pi.
2. Install utility as described above.
3. Navigate to `http://PI_IP_ADDRESS:8080` or `http://pyapi.local:8080`.

## Windows Usage

1. Clone Repository to any directory.
2. Install Anaconda and import the enviroment `enviroments/pyapi.yml`.
3. Run `main.py` in the newly imported enviroment.
3. Navigate to `http://PI_IP_ADDRESS:8080` or `http://pyapi.local:8080`.

## Commands to use with Requests Libary

* Send data to the arduino as follows `http://PI_IP_ADDRESS:8080/send?command=ARDUINO_COMMAND_HERE`
* Clear log files on server device `http://PI_IP_ADDRESS:8080/clearLogs`
* Acquire Receive log `http://PI_IP_ADDRESS:8080/public/receiveLog.csv`
* Acquire Transmit log `http://PI_IP_ADDRESS:8080/public/transmitLog.csv`
* Connect or Reconnect Serial `http://PI_IP_ADDRESS:8080/connect`
* Get latest serial monitor data in table form `http://PI_IP_ADDRESS:8080/serialMonitor`
* Get latest serial monitor line as string `http://PI_IP_ADDRESS:8080/getLine`

## Future Work (In Progress)

* Use `glob` to detect and connect to devices automatically.
* Responsive web design.
* Clean table display in webpage.
* Add the use of `setting.json` for easier configuration.

Note: The serial port is automatically connected when using the `send?command=ARDUINO_COMMAND_HERE` function. The connect command is best used to manage disconnect errors. 

## Screenshots

![Screenshot 1](https://github.com/rmccartney856/pyapi/blob/master/media/logo.jpg)

![Screenshot 2](https://github.com/rmccartney856/pyapi/blob/master/media/logo.jpg)

