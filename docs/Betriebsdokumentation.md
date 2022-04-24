# Betriebsdokumentation
[[_TOC_]]
## Einführungstext 

TODO: In 2-3 Sätzen beschreiben was die Skripte grundsaetzlich tun.

Das  Skript 1 klont alle GIT-Repos mit GIT-Kommandos und speichert sie in einem Verzeichnis. Das Skript 2 liest von allen GIT-Repos in diesem Verzeichnis alle Commits aus und speichert diese in einem File mit einem bestimtmen Format.\
In einen nächsten Schritt wird das Output File mit einen zu Verfügung gestelltem Skript visualisert.

## Installationsanleitung für Administratoren
### Installation
#### Requirements
1. Ubuntu Server installation (18.4 oder 20.4).
2. Überprüfen das Python 3 installiert ist.
```
python3 --version
```

#### Allgemeine Installation
Beide Skripts verwenden die Python Library gitpython. Sie kann mit dem folgenden Befehlen installiert werden:
```
sudo apt install python3-pip
pip3 install gitpython
```

Beide Skripts befinden sich in diesem Git Repository. Desswegen ist es empfolen das gesamte Repository zu klonen:
```
git clone https://github.com/Nightshade1925/m122_projektarbeit_albisetti_harlacher.git
```
Die beiden Skripts befinden sich im Ordner bin (m122_projektarbeit_albisetti_harlacher/bin).

WICHTIG: Die erfolgreiche Ausführung der Skripts erfordert den Zugriff auf das Konfigurationsfile config.json mit dieser Referenz:
```
../etc/config.json
```
Ebenfalls muss das utils.py File im selben Ordner sein wie die beiden Skripts.
Ansonstens spielt es keine Rolle wo die Skirpts installiert werden.

Es gibt keine Skriptspezifische installationen. Beide Skripts funktionieren nach der oben beschriebenen Installation.

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
Da keine spezielle Konfiguration notwendig ist für die Ausführung der Skripts wird nur das Logging zum Logfile konfiguriert.\
Das Loglevel kann DEBUG, INFO, WARNING, ERROR oder CRITICAL sein. Es definiert welche wichtigkeit von Logs in das Logfile geloggt werden.\
(Note: Wenn der Debug Flag bei der Ausführung des Skripts gesetzt ist, wird das Loglevel zu DEBUG überschrieben)

Logpath ist der Pfad zum Logfile. 

TODO: Wie ist ein allfaelliger Cronjob einzurichten TODO: Wie sind User-Home-Templates einzurichten
Abgesehne von der Installation und der Konfiguration des config.json File muss man nichts weiteres einrichten.

## Bediensanleitung Benutzer
TODO: Erzeugen der Input-Files beschreiben, falls noetig
### Erzeugen von Input-Files
#### Skript 1
Skript 1 benötigt ein CSV Datei als Input file. Das CSV Dateil sollte folgedes Format haben:
![image](https://user-images.githubusercontent.com/71868338/164968295-378bc71b-f1f4-401e-96dc-90e211246eb4.png)

Spalte 1: GitUrl  
Spalte 2 SpeicherZiel

WICHTIG: Zwischen den beiden Spalten muss es ein Abstand haben als Spaltentrennung.

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
Aufruf:          
```
Bsp:              sudo python3 git_clone_update_repos.py -b /home/vagrant -f m122_projektarbeit_albisetti_harlacher/etc/input_file.csv
                  sudo python3 PfadZumScript -b PfadZumZielOrt -f PfadZumInputFile (CSV Datei)
```

Nachdem der Script aufgerufen wurde, werden alle erfolgreich clonnte Repos in der Base directory stehen. Ebenfalls wird ein log file erstellt, wo der Benutzer den Skript aufgerufen hat. Falls es im Base directory bereits Repositories hat und diese nicht im Input file stehen, gelten diese als nicht benutzt und werden beim Skriptaufruf gelöscht.

#### Skript 2
Aufruf:
```
git_extract_commits.py [-d] -b BASE_DIR -o OUTPUT_FILE
```
Das BASE_DIR ist der Ordner welcher die Git Repos beinhaltet von welchen man die Git Commits ins Output File herausschreiben möchte.\
Das OUTPUT_FILE beschreibt der Pfad wohin das Output File geschrieben werden soll.\
Mit dem Flag -d kann der Debug Modus aktiviert werden. Damit werden Informationen auf dem DEBUG Level sowohl in die Konsole wie auch ins Logfile geschrieben.

TODO: beschreiben der erzeugt files (falls solche erzeugt werden)
### Skript Output
#### Skript 1
Some folders (bob)      

#### Skript 2
Das Skript 2 produziert ein Output File (an einer bestimmten Position welche beim Aufruf vom Skript definiert wird). Dieses Output File wird in einen nächsten Schritt mit einem weiteren Skript grafisch dargestellt.\
Das Output File ist im CSV Syntax. Es beginnt immer mit dem Titel:
```
Zielverzeichnis,Datum,Commit-Hash,Author
```
Jede weitere Zeile im Output File ist ein Commit aus einem Repo. Die Zeilen haben folgenden Syntax:
```
Name des Verzeichnis,Datum im Format YYYYmmdd (wobei YYYY=Jahr, mm=Monat, dd=Tag), Commit-Hash , Name des Commiters
```
Hier ein Beispiel:\
![grafik](https://user-images.githubusercontent.com/69149487/164976802-057dedd5-4361-478f-96e8-b1c8fba623a7.png)

TODO: Lokation von logfiles und bekannte Fehlermeldungen beschreiben.
Wo die Logs sich befinden muss man selber in der Konfiguration definieren.
