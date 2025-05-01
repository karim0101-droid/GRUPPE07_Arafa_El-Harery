# ROD_Project

Dieses Repository enthält die Beschreibungspakete für das ROD-Projekt. Es ist für die Verwendung in einer ROS-Umgebung (z. B. mit ROS Noetic) ausgelegt.

---

## 🔑 SSH-Zugang einrichten (empfohlen)

Falls du das Repository via SSH klonen möchtest (anstatt per HTTPS), richte zunächst einen SSH-Key ein:

### 1. SSH-Key generieren (falls nicht vorhanden)

```bash
ssh-keygen -t ed25519 -C "deine.email@example.com"
```

2. Public Key anzeigen und kopieren

cat ~/.ssh/id_ed25519.pub

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
📥 Repository klonen

```bash
git clone git@github.com:karim0101-droid/ROD_Project.git
```
  Hinweis: Stelle sicher, dass du SSH-Zugriff hast – siehe oben.

🛠️ Workspace einrichten und builden

Wechsle in den Workspace (z. B. GRUPPE07_Arafa_El-Harery) und führe den Build aus:
```bash
cd ~/GRUPPE07_Arafa_El-Harery
catkin build
```


📡 Workspace automatisch sourcen

Damit dein Workspace bei jedem Terminalstart verfügbar ist, füge Folgendes zu deiner ~/.bashrc hinzu:
```bash
source ~/GRUPPE07_Arafa_El-Harery/devel/setup.bash
```
Danach einmal neu laden oder Terminal neustarten:
```bash
source ~/.bashrc
```

---
