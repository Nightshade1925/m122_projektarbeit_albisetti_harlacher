# Skript 1

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Erstmaliger Aufruf | Das Skript soll mit einem input file aufgerufen werden, in welchem nur verfügbare Git-URLs sind. Diese sollen in ein noch nicht existierendes Verzeichnis geklont werden:<pre>sudo python3 git_clone_update_repos.py -b /home/vagrant -f m122_projektarbeit_albisetti_harlacher/etc/input_file.csv</pre> | Benutze das Inputfile.csv das im m122_projektarbeit_albisetti_harlacher/etc/ liegt| Verzeichnis wird erstellt und alle Repos werden darin geklont | | | |

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
|Nicht gebrauchte Repos löschen | Das Script soll mit einem input file aufgerufen werden. Anschliessen soll beim existierten Test Repo überprüft werden, ob es im input file aufgelistet ist. Ist dies nicht der Fall, soll dieses Test Repo gelöscht werden | Zuerst soll noch ein Test Repo geklont werden im gleichen Zielverzeichniss. <pre>git clone https://github.com/Nightshade1925/TicketSystem.git</pre> Benutze das Inputfile.csv das im <pre>m122_projektarbeit_albisetti_harlacher/etc/ </pre> liegt| Verzeichnis wird erstellt, alle Repos werden darin geklont und das zuerst geklonte Repo wird gelöscht.| | | |

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Nicht existierende Repo clonen | Das Skript soll mit einem input file aufgerufen werden, in welchem nur ungültige Git-URLs sind. Diese sollen geklont werden:<pre>>sudo python3 git_clone_update_repos.py -b /home/vagrant -f m122_projektarbeit_albisetti_harlacher/etc/NotExistingRepo.csv</pre> | Benutze das NotExistingRepo.csv das im <pre>m122_projektarbeit_albisetti_harlacher/etc/ </pre> liegt | Nichts wurde geklonnt. Im log file sollte die Fehlermeldung stehen, "couldn't clone repo name".| | | |

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Überprüfung ob das directory im Zielverzeichnis ein Repo ist. | Das Script soll mit einem input file aufgerufen werden. Anschliessend soll es im Zielverzeichnis überprüfen ob alle directories ein repo ist falls es kein Repo ist, nichts machen.<pre>sudo python3 git_clone_update_repos.py -b /home/vagrant -f m122_projektarbeit_albisetti_harlacher/etc/input_file.csv</pre> | Zuerst soll ein neues directory im Zielverzeichnis erstellt werden. Benutze das Inputfile.csv das im <pre>m122_projektarbeit_albisetti_harlacher/etc/ </pre> liegt | Verzeichnis wird erstellt und alle Repos werden darin geklont. Das erstellte directory ist immer noch vorhanden.| | | |

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Überprüfe ob das existierende Repo nur ein pull command macht und kein clone command | Das Skript soll mit einem input file aufgerufen werden. Diese sollen in ein noch nicht existierendes Verzeichnis geklont werden:<pre>>sudo python3 git_clone_update_repos.py -b /home/vagrant -f m122_projektarbeit_albisetti_harlacher/etc/input_file.csv</pre> | Zuerst muss das folgende Repository im Zielverzeichnis geklont werden <pre>https://github.com/Nightshade1925/m122_projektarbeit_albisetti_harlacher.git</pre>| Verzeichnis wird erstellt und alle Repos werden darin geklont | | | |

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Installation nach Dokumentation | Installation des Skripts Schritt für Schritt nach Dokumentation | Geklontest git Repo mit Dokumentation | Ein funktionierendes Skript | | | |


# Skript 2

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Erstmaliger Aufruf | Das Skript soll mit einem Verzeichnis als parameter augerufen werden in welchem 2 Repos sind:<pre> sudo python3 git_extract_commits.py -b / -f /tmp/commits.csv</pre> | Verzeichnis mit den GIT-Repos die mit dem Skript 1 geklont wurden:<pre>/tmp/myrepos</pre> | Alle Repos aus /tmp/myrepos werden gelesen und ein File /tmp/commits.csv erstellt mit allen Commits beider Repos | | | |

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Paramter fehlen | Das Skript soll aufgerufen werden ohne den paramter für das Outputfile:<pre> python3 git_extract_commits.py -b /tmp/myrepos</pre> | Verzeichnis mit den GIT-Repos die mit dem Skript 1 geklont wurden:<pre>/tmp/myrepos</pre> | Eine Warnung wird ausgegeben welche sagt, dass ein Input Paramter fehlt  | | | |

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Verzeichnis leer | Das Skript soll mit einem Verzeichnis als parameter augerufen werden in welchem nichts ist:<pre> python3 git_extract_commits.py -b /tmp/myrepos -f /tmp/commits.csv</pre> | Ein leeres Verzeichniss | Eine Warnung wird ausgegeben welche sagt, dass kein Repository im Verzeichnis gefunden wrude  | | | |

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Verzeichnis ohne Repo | Das Skript soll mit einem Verzeichnis als parameter augerufen werden in welchem kein Repo ist:<pre> python3 git_extract_commits.py -b /tmp/myrepos -f /tmp/commits.csv</pre> | Ein verzeichnis welches kein Repo entält | Eine Warnung wird ausgegeben welche sagt, dass kein Repository im Verzeichnis gefunden wrude  | | | |

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Output File ohne Permission | Das Skript soll mit einem Output File als parameter augerufen werden auf welches der momentane user keien berechtigungen hat:<pre> python3 git_extract_commits.py -b /tmp/myrepos -f /var/commits.csv</pre> | Ein Output File Path auf welcher der user kein Zugriff hat | Eine Warnung wird ausgegeben welche sagt, dass Berechtigungen fehlen um das Output File zu erstellen | | | |

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Installation nach Dokumentation | Installation des Skripts Schritt für Schritt nach Dokumentation | Geklontest git Repo mit Dokumentation | Ein funktionierends Skript | | | |

