# Simple port scanner

## Description
**simple-port-scanner** is a basic TCP port scanner written in Python.  
It scans ports from **1 to 1024** on a given IP address and reports which ports are open along with their well-known service names.

## Project structure
simple-port-scanner/ <br>
├── PortScanner.py <br>
└── Ports.py <br>

## Files Overview

### Ports.py
Contains a dictionary named `WELL_KNOW_PORTS` that maps common port numbers to their standard service names (e.g. `80 → HTTP`, `22 → SSH`).  
This file is used to identify services running on open ports.

### PortScanner.py
Main scanning script that:
- Asks the user for a target IP address
- Iterates through ports **1–1024**
- Creates a TCP socket for each port
- Uses a short timeout (0.125s) for faster scanning
- Checks if a port is open using `connect_ex`
- Displays open ports with their service names
- Prints a message when scanning is complete

## Requirements
- Python 3.x
- No external libraries required (uses built-in `socket` module)

## Usage
```md
python PortScanner.py
```
You need to select a target, For example we will be scanning localhost
```md
127.0.0.1
```
Example output:
```md
Port 80 HTTP jest otwarty
```

## Notes
- Scans **TCP ports only**
- **No error handling at the moment for ports missing in `WELL_KNOW_PORTS`**
- Intended for educational purposes and testing in authorized environments only

## Planned Features
- UDP port scanning
- Custom port range
- Multithreaded scanning
- Service banner grabbing
- Export results to file
- Translation to English

## License
Educational / personal use




