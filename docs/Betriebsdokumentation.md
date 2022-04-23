# Betriebsdokumentation
[[_TOC_]]
## Einführungstext 

TODO: In 2-3 Sätzen beschreiben was die Skripte grundsaetzlich tun.

## Installationsanleitung für Administratoren

### Installation
TODO: Wie ist das skript zu installieren. (z.B. apt-get install ... oder tar xvf .... oder ...)

#### Requirements
Ubuntu Server installation (18.4 oder 20.4)
Überprüfen das Python 3 installiert ist.
```
python3 --version
```

#### Allgemeine Installation
Beide Skripts verwenden die Python Library gitpython. Sie kann mit dem folgenden Befehlen installiert werden:
```
sudo apt install python3-pip
pip3 install gitpython
```

Beide Skripts befinden sich in diesem Git Repository. Desswegen ist es Empfolen diese Repository zu klonen:
```
git clone https://github.com/Nightshade1925/m122_projektarbeit_albisetti_harlacher.git
```
Die beiden Skripts befinden sich im ordner bin (m122_projektarbeit_albisetti_harlacher/bin)

WICHTIG: Die erfolgreiche Ausführung der Skirpts erfordert den zugriff auf das Konfigurationsfile config.json mit dieser Referenz:
```
../etc/config.json
```
Ebenfalls muss das utils.py File im selben ordner sein wie die beiden Skripts.
Ansonstens spielt es keine Rolle wo die Skirpts installiert werden.

#### Skript 1
i think nothing (check this bob)

#### Skript 2 
i think nothing (check this one here pls Paul from futere)


### Konfiguration

TODO: Beschreibung der Konfigurationsfiles (Beispiel-Files erstellen im Repo)
Das Konfigurationsfile ist config.json und wird von beiden Skripts verwendet.\
Beispielkonfiguration:
```json
{
  "loglevel": "INFO",
  "logpath": "log_file.log"
}
```
Da keine spezielle Konfiguration notwendig ist für die Ausführung der Skripts wird nur das Logging zun Logfile konfiguriert.
Das Loglevel kann DEBUG, INFO, WARNING, ERROR oder CRITICAL sein. Es definiert welche wichtigkeit von Logs in das Logfile geloggt werden.
(Note: Wenn der Debug Flag bei der Ausführung des Skripts gesetzt ist, wird das Loglevel zu DEBUG überschrieben)

Logpath ist der Pfad zum Logfile. 

TODO: Wie ist ein allfaelliger Cronjob einzurichten TODO: Wie sind User-Home-Templates einzurichten
Abgesehne von der Installation und der Konfiguration des config.json File braucht es keine weitere Konfiguraitionene


## Bediensanleitung Benutzer

TODO: Erzeugen der Input-Files beschreiben, falls noetig
### Erzeugen von Input-Files
#### Skript 1
here you go bob

#### Skript 2
Das Skript 2 braucht zwar kein Input files, jedoch bracht es logischerweise Git Repos um Commits daraus zu extrahieren. Dazu können selber welche geklont werden mit:
```
git clone [url]
```
oder man verwendet das Skript 1 um die Git Repos zu klonen.

TODO: beschreiben des Scriptaufruf
### Skriptaufruf
Wie bereits in der Installation beschrieben spielt es keine Rolle von wo die Skripts ausgeführt werden oder wo sie installiert wurden, sollange das Konfigurationsfile (config.json) folgenderweise referenziert werden kann 
```
../etc/config.json
```
Ebenfalls muss das utils.py File im selben Ordner sein wie die Skripts.
\n
\n
Die Details zum Skriptaufruf können von beiden Skirpts mit folgendem Befehl eingesehen werden:
```
python3 pathToTheSkript.py -h
```

#### Skript 1
Script 1 Aufruf:  python git_clone_update_repos.py -b ~ -f m122_projektarbeit_albisetti_harlacher/etc/input_file.csv

#### Skript 2
Aufruf:
```
git_extract_commits.py [-d] -b BASE_DIR -o OUTPUT_FILE
```
Das BASE_DIR ist der Ordner welcher die Git Repos beinhaltet von welchen man die Git Commits ins Output File herausschreiben möchte.\
Das OUTPUT_FILE beschreibt der Pfad wohin das Output File geschrieben werden soll.\
Mit dem Flag -d kann der Debug Modus aktiviert werden. Damit werden Informationen auf dem DEBUG Level sowohl in die Konsole wie auch ins Logfile geschrieben.

TODO: beschreiben der erzeugt files (falls solche erzeugt werden)


TODO: Lokation von logfiles und bekannte Fehlermeldungen beschreiben.
Wo die Logs sich befinden muss man selber in der Konfiguration definieren.
