# ServerMonitoring
Send report from server to email every 8 hours
Installing the code on the server
Method 1: Using SSH

Connecting to the server: Connect to your server via SSH.
Cloning the repository: Run the git clone command using the repository URL.
Installing dependencies: If your script requires specific libraries, install them using pip.
Executing the script: Run your Python script.
Method 2: Using package management tools

For Debian/Ubuntu-based systems:
‌
Bash

sudo apt update
sudo apt install git

git clone https://github.com/javadubu/ServerMonitoring.git

cd ServerMonitoring

pip install -r requirements.txt

python monitor.py

