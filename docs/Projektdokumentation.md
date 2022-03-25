# Projekt Dokumentation

[[_TOC_]]

## Lösungsdesign
Anhand der Analyse wurde folgendes Lösungsdesign entworfen.

### Aufruf der Skripte

Die Skripts sind mit Python geschrieben und müssen desswegen auch mit Python ausgeführt werden.
Eine Debugging option ist für beide Skripts vorhanden. Diese verwendet man indem man den Flag "-d" verwendet.

Das Skript lauft nicht automatisch ab.

Beide Skripts verwenden die selbe globale Konfiguration.

Hier noch eion Beispielaufruf für die Skripts:

#### Script 1
python3 git_clone_update_repos.py -d -b Basedir -f PathToFileWithURL

#### Script 2
python3 git_extract_commits.py -d -b Basedir -o PathForOutputFile

### Ablauf der Automation

#### Script 1
![Activity Diagram Script 1](https://user-images.githubusercontent.com/71868338/160097514-774fc902-b344-4220-a1c2-5a5d7ec9400d.png)
#### Script 2
![M122_LB02_CreateOutputFile drawio](https://user-images.githubusercontent.com/69149487/160097776-1ce4bc69-e995-44b3-bbc2-e776018d5122.png)

### Konfigurationsdateien

Das Konfiguraiontsfile wird von beiden Skripts verwendet und wird nur für die Log Konfiguration verwendet
Die Konfiguration ist im JSON Format.

Folgende Parameter sind vorhanden:
loglevel  - DEBUG, INFO, WARNING, ERROR oder CRITICAL. Definiert das loglevel für die logs in das file 
logpath   - Definiert wo das Logfile gespeichert wird


## Abgrenzungen zum Lösungsdesign

TODO: Nachdem das Programm verwirklicht wurde hier die unterschiede von der Implemenatino zum Lösungsdesign beschreiben (was wurde anders gemacht, was wurde nicht gemacht, was wurde zusaetzlich gemacht)
