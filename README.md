# DDOS ATTACK SCRIPT

#### Script Start Command
```
    app.py [-h]
        [--ip [*IP adresi] ]
        [--port [Port numarası] ]

Available Arguments:
  -h, --help   show this help message and exit
  --ip IP      Determines the ip address to attack.
  --port PORT  Specifies the port number to use, but if not entered, all ports are attacked.
```

##### Script initialization examples
```
# Only 192.168.1.1. Attacks 80 ports of the IP address.
python app.py --ip 192.168.1.1 --port 80

# Attacks all ports of 192.168.1.1 ip address.
python app.py --ip 192.168.1.1

```
