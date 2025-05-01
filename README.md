# ROD_Project SETUP

Dieses Repository enthält die Beschreibungspakete für das ROD-Projekt. Es ist für die Verwendung in einer ROS-Umgebung (z. B. mit ROS Noetic) ausgelegt.
Hinweis: Wenn etwas im README nicht angeführt wird, bitte hinzufügen @Sameh!

---

## 🔑 SSH-Zugang einrichten (empfohlen)

Falls du das Repository via SSH klonen möchtest (anstatt per HTTPS), richte zunächst einen SSH-Key ein:

### 1. SSH-Key generieren (falls nicht vorhanden)

```bash
ssh-keygen -t ed25519 -C "deine.email@example.com"
```

### 2. Public Key anzeigen und kopieren

```bash
cat ~/.ssh/id_ed25519.pub
```
### 3. SSH-Key zu GitHub hinzufügen

  Öffne 
  ```bash 
  https://github.com/settings/keys
  ```

  Klicke auf "New SSH Key"

  Füge den kopierten Key in das Textfeld ein und gib ihm einen Namen

4. SSH-Verbindung testen

```bash
ssh -T git@github.com
```
## 📥 Repository klonen

```bash
git clone git@github.com:karim0101-droid/ROD_Project.git
```
  Hinweis: Stelle sicher, dass du SSH-Zugriff hast – siehe oben.


## 🌿 Im jeweiligen Branch arbeiten

Wechsle in deinen Branch und ändere dabei "branch-name" zu deinem jeweiligen Branch:
```bash
git checkout branch-name
```
Wenn du noch keinen Branch erstellt hast, erstelle einen und ändere "new-branch-name" zu deinem jeweiligen Branch:
```bash
git checkout -b new-branch-name
```

## 5. Dependecies herunterladen

1. Installiere fehlende ROS-Controller

Stelle sicher, dass du folgendes Paket installiert hast:
```bash
sudo apt install ros-noetic-ros-controllers
```

Dieses Paket enthält JointTrajectoryController und weitere wichtige Controller-Plugins.

2. Kontrolliere die Controller-Plugins im System

Du kannst prüfen, welche Controller verfügbar sind mit:
```bash
rosservice call /controller_manager/list_controller_types
```

Stelle außerdem sicher, dass du alles rund um MoveIt heruntergeladen hast:
```bash
sudo apt install ros-noetic-moveit*
```

## 6. Workspace einrichten und builden


Wechsle in den Workspace und führe den Build aus:
```bash
cd ~/GRUPPE07_Arafa_El-Harery
catkin init
catkin build
```


### 📡 Workspace automatisch sourcen

Öffne ".bashrc" mit:
```bash
nano ~/.bashrc
```

Damit dein Workspace bei jedem Terminalstart verfügbar ist, füge Folgendes zu deiner ~/.bashrc hinzu:
```bash
source ~/GRUPPE07_Arafa_El-Harery/devel/setup.bash
```
,falls dies nicht funktioniert, bitte den gesamten Pfad angeben und zum Speichern STRG+X -> J -> Enter drücken!

Danach einmal neu laden oder Terminal neustarten:
```bash
source ~/.bashrc
```

---
