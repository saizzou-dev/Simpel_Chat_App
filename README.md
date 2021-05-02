# Chat App mit GUI

Der Chat App besteht aus einer Server Datei die ausgeführt werden muss damit die Clients sich mit dem Server Verbinden kann. Der Host und Port kann geändert werden. Ein DynDNS Service (wie zb. No-IP) kann benutzt werden um ein fern Server zu benutzen.  

## Installation

Startet dei Server.py datei auf ihren Server.
```bash
python server.py
```
Der Server kann bis zu 10 Client verbindungen erhalten. Dies kann geändert werden indem man die Server.py ```SERVER.listen(10)``` zeile ändert.

## Usage

```CMD
python Client.py
```
Im Linux Terminal oder über der Command Zeile im Windows startet dem Client und tipt in die Box dem Nutzer Name hinein. Danach seit ihr zum Chat bereit. 



## Contributing
Fühlt euch frei dem Code zu nutzen oder zu verbessern. Pull Requeste werden auch akzeptiert.
