from machine import Pin, PWM
import socket
import time
import network
import dht
import _thread

ssid = 'Erichussy'
password = 'lmao1234'

led_B = PWM(Pin(18))
led_B.freq(1000)

led_G = PWM(Pin(19))
led_G.freq(1000)

led_R = PWM(Pin(20))
led_R.freq(1000)

sensor = dht.DHT22(Pin(22))

port = 2121


class Haina:
    def __init__(self, _gen="", _ocazie="", _categorie="", _nume="", _tip=""):
        self.gen = _gen  # M/F/Ambele
        self.ocazie = _ocazie  # Casual/Formal/Ambele
        self.categorie = _categorie  # Pantof/Pantalon/Tricou/Bluza/Accesoriu
        self.nume = _nume  # cum se cheama haina efectiv
        self.tip = _tip  # haina pt vreme calda/rece/racoare


class Vreme:
    def __init__(self, _tip="", _temperatura=0, _umiditatea=0):
        self.tip = _tip  # rece/racoare/cald
        self.temperatura = _temperatura
        self.umiditatea = _umiditatea

    def getTip(self):
        return self.tip

    def getTemperatura(self):
        return self.temperatura

    def setTip(self, _tip):
        self.tip = _tip

    def setTemperatura(self, _temperatura):
        self.temperatura = _temperatura

    def setUmiditate(self, _umiditate):
        self.umiditatea = _umiditate

    def getUmiditate(self):
        return self.umiditatea


class CurrentUser:
    def __init__(self, _nume="Nume", _gen="M"):
        self.nume = _nume
        self.gen = _gen
        self.haine = []

    def getNume(self):
        return self.nume

    def setNume(self, _nume):
        self.nume = _nume

    def getGen(self):
        return self.gen

    def setHaine(self, _haine):
        self.haine = _haine

    def setGen(self, _gen):
        self.gen = _gen

    def getHaine(self):
        return self.haine

    def addHaine(self, _haina):
        self.haine.append(_haina)


userM = CurrentUser("Erich", "M")
userF = CurrentUser("Sabina", "F")
currentVreme = Vreme()

# rece
userM.addHaine(Haina("M", "casual", "pantof", "Botine", "rece"))
userM.addHaine(Haina("M", "casual", "pantalon", "Pantaloni", "rece"))
userM.addHaine(Haina("M", "casual", "tricou", "Pulover", "rece"))
userM.addHaine(Haina("M", "casual", "bluza", "Palton", "rece"))

userM.addHaine(Haina("M", "casual", "pantof", "Cizme", "rece"))
userM.addHaine(Haina("M", "casual", "tricou", "Helanca", "rece"))
userM.addHaine(Haina("M", "casual", "accesoriu", "Fular", "rece"))
userM.addHaine(Haina("M", "casual", "accesoriu", "Caciula", "rece"))

userF.addHaine(Haina("F", "casual", "pantof", "Botine", "rece"))
userF.addHaine(Haina("F", "casual", "pantalon", "Pantaloni", "rece"))
userF.addHaine(Haina("F", "casual", "tricou", "Pulover", "rece"))
userF.addHaine(Haina("F", "casual", "bluza", "Palton", "rece"))

userF.addHaine(Haina("F", "casual", "pantof", "Cizme", "rece"))
userF.addHaine(Haina("F", "casual", "tricou", "Helanca", "rece"))
userF.addHaine(Haina("F", "casual", "accesoriu", "Fular", "rece"))
userF.addHaine(Haina("F", "casual", "accesoriu", "Caciula", "rece"))

# racoare
userM.addHaine(Haina("M", "casual", "pantof", "Adidasi", "racoare"))
userM.addHaine(Haina("M", "casual", "pantalon", "Pantaloni trening", "racoare"))
userM.addHaine(Haina("M", "casual", "bluza", "Hanorac", "racoare"))

userF.addHaine(Haina("F", "casual", "pantof", "Balerini", "racoare"))
userF.addHaine(Haina("F", "casual", "pantalon", "Blugi", "racoare"))
userF.addHaine(Haina("F", "casual", "tricou", "Bluza", "racoare"))
userF.addHaine(Haina("F", "casual", "bluza", "Vesta", "racoare"))

userF.addHaine(Haina("F", "casual", "pantof", "Adidasi", "racoare"))
userF.addHaine(Haina("F", "casual", "pantalon", "Pantaloni trening", "racoare"))
userF.addHaine(Haina("F", "casual", "bluza", "Hanorac", "racoare"))

# cald
userM.addHaine(Haina("M", "casual", "pantof", "Adidasi", "cald"))
userM.addHaine(Haina("M", "casual", "pantalon", "Pantaloni scurti", "cald"))
userM.addHaine(Haina("M", "casual", "tricou", "Tricou", "cald"))
userM.addHaine(Haina("M", "casual", "accesoriu", "Sapca", "cald"))

userM.addHaine(Haina("M", "casual", "pantof", "Sandale", "cald"))
userM.addHaine(Haina("M", "casual", "tricou", "Salopeta", "cald"))

userF.addHaine(Haina("F", "casual", "pantof", "Adidasi", "cald"))
userF.addHaine(Haina("F", "casual", "pantalon", "Pantaloni scurti", "cald"))
userF.addHaine(Haina("F", "casual", "tricou", "Tricou", "cald"))
userF.addHaine(Haina("F", "casual", "accesoriu", "Sapca", "cald"))

userF.addHaine(Haina("F", "casual", "pantof", "Sandale", "cald"))
userF.addHaine(Haina("F", "casual", "tricou", "Salopeta", "cald"))

userM.getHaine().sort(key=lambda x: x.nume)
userF.getHaine().sort(key=lambda x: x.nume)


def R_on():
    led_R.duty_u16(1500)


def R_off():
    led_R.duty_u16(0)


def G_on():
    led_G.duty_u16(1500)


def G_off():
    led_G.duty_u16(0)


def B_on():
    led_B.duty_u16(1500)


def B_off():
    led_B.duty_u16(0)


def setVremeFromSenzor():
    time.sleep(1)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    _tip = ""
    if temp < 10:
        B_on()
        R_off()
        G_off()
        _tip = "rece"
    elif 11 <= temp < 17:
        B_off()
        R_off()
        G_on()
        _tip = "racoare"
    elif temp >= 18:
        B_off()
        R_on()
        G_off()
        _tip = "cald"
    currentVreme.setTip(_tip)
    currentVreme.setUmiditate(hum)
    currentVreme.setTemperatura(temp)


_thread.start_new_thread(setVremeFromSenzor, ())


def recomanda_haine(_tip):
    listaCurenta = []
    arePantof = False
    arePantalon = False
    areTricou = False
    areBluza = False
    areAccesoriu = False
    for haina in userM.getHaine():
        if _tip in haina.tip:
            if "casual" in haina.ocazie:
                if "pantof" in haina.categorie:
                    if arePantof is False:
                        arePantof = True
                        listaCurenta.append(haina)
                if "pantalon" in haina.categorie:
                    if arePantalon is False:
                        arePantalon = True
                        listaCurenta.append(haina)
                if "tricou" in haina.categorie:
                    if areTricou is False:
                        areTricou = True
                        listaCurenta.append(haina)
                if "bluza" in haina.categorie:
                    if areBluza is False:
                        areBluza = True
                        listaCurenta.append(haina)
                if "accesoriu" in haina.categorie:
                    if areAccesoriu is False:
                        areAccesoriu = True
                        listaCurenta.append(haina)
    reccString = "Vremea curenta este " + _tip + ", recomand urmatoarea tinuta:"
    if listaCurenta is []:
        return "Nu ai destule haine pentru acest tip de vreme/ocazie"
    for haina in listaCurenta:
        reccString = reccString + haina.nume + ", "
    return reccString


def recomanda_locuri(tip):
    if "rece" in tip:
        return "Este frig afara, stam acasa sau la un local pentru cafeluta calda"
    elif "racoare" in tip:
        return "Este racoare afara, mergem la terasa sau in natura"
    elif "cald" in tip:
        return "Este cald afara, hai la gratar sau la strand"


def handle_request(conn):
    # Receive data from the connection
    data = conn.recv(1024).decode()
    print(f"Received data: {data}")
    setVremeFromSenzor()
    # Check for commands in the data
    if "GET / HTTP/1.1" in data:
        response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><form><label 
        for=\"cmd\">Comanda:</label><input type=\"text\" id=\"cmd\" name=\"cmd\" /><input type=\"submit\" 
        value=\"Trimite\" /></form></body></html>"""
    elif "cmd=haine" in data:
        response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n <html><body><form><label 
        for=\"cmd\">Comanda:</label><input type=\"text\" id=\"cmd\" name=\"cmd\" /><input type=\"submit\" 
        value=\"Trimite\" /></form><p>""" + recomanda_haine(currentVreme.getTip()) + """</p></body></html>"""
    elif "cmd=loc" in data:
        response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><form><label 
        for=\"cmd\">Comanda:</label><input type=\"text\" id=\"cmd\" name=\"cmd\" /><input type=\"submit\" 
        value=\"Trimite\" /></form><p>""" + recomanda_locuri(currentVreme.getTip()) + """</p></body></html>"""
    elif "cmd=vreme" in data:
        response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><form><label 
        for=\"cmd\">Comanda:</label><input type=\"text\" id=\"cmd\" name=\"cmd\" /><input type=\"submit\" 
        value=\"Trimite\" /></form><p>Vremea: """ + currentVreme.getTip() + """<br>Temperatura: """ + str(
            currentVreme.getTemperatura()) + """*C
        <br>Umiditatea: """ + str(currentVreme.getUmiditate()) + """ %</p></body></html>"""
    else:
        response = """HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<html><body><form><label 
        for=\"cmd\">Comanda:</label><input type=\"text\" id=\"cmd\" name=\"cmd\" /><input type=\"submit\" 
        value=\"Trimite\" /></form><p>Unknown command\n</p></body></html>"""

    conn.sendall(response.encode())
    conn.close()


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print(f"Connecting to WiFi: {ssid}")
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print(f"Connected to WiFi, IP address: {wlan.ifconfig()[0]}")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('', port)
s.bind(address)

s.listen(1)
print(f"Listening on port {port}")

while True:
    conn, addr = s.accept()
    print(f"Connected by {addr}")

    handle_request(conn)
