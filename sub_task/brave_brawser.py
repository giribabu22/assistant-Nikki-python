import os,time

os.system('sudo apt install pip')
os.system('sudo apt install curl')
os.system('sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg')
os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
os.system('sudo apt update')
time.sleep(1)
os.system('sudo apt install brave-browser=1.52.126')
time.sleep(1)
os.system('sudo apt install espeak')
os.system('sudo apt-get install portaudio19-dev')
