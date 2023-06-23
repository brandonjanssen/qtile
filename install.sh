#!/bin/bash

# Default packages are for the configuration and corresponding .config folders
# Install packages after installing base Debian with no GUI

# xorg display server installation
sudo apt install -y xserver-xorg xinit xbacklight xbindkeys xvkbd xinput light

# INCLUDES make,etc.
sudo apt install -y python3-pip 

# Qtile requirements
sudo apt install -y libpangocairo-1.0-0
sudo apt install -y python3-xcffib python3-cairocffi

# Install qtile
pip3 install qtile
pip3 install psutil

# Microcode for Intel/AMD 
sudo apt install -y amd64-microcode
#sudo apt install -y intel-microcode 

# Network Manager
sudo apt install -y network-manager network-manager-gnome

# Installation for Appearance management
sudo apt install -y lxappearance lxpolkit lxsession-logout

# File Manager (eg. pcmanfm,krusader,thunar)
sudo apt install -y thunar thunar-volman thunar-media-tags-plugin thunar-archive-plugin 

sudo apt install -y xfce4-places-plugin tumbler tumbler-plugins-extra file-roller

# Network File Tools/System Events
sudo apt install -y dialog mtools dosfstools avahi-daemon acpi acpid gvfs-backends #xfce4-power-manager

sudo systemctl enable avahi-daemon
sudo systemctl enable acpid

# Terminal (eg. terminator,kitty)
#sudo apt install -y xfce4-terminal
sudo apt install -y kitty

# Sound packages
sudo apt install -y pipewire pipewire-bin pipewire-pulse pipewire-jack pipewire-audio pipewire-alsa libwireplumber wireplumber-doc wireplumber
#sudo apt install -y pulseaudio alsa-utils pavucontrol volumeicon-alsa

# Neofetch/HTOP /// TERMINAL GODDIES 
sudo apt install -y lsd fd silversearcher-ag ripgrep lolcat zoxide ytfzf fzf bat fish duf du-dust fastfetch mlocate cpu-x pulsemixer pamixer 

# EXA installation
# replace ls command in .bashrc file with line below
# alias ls='exa -al --long --header --color=always --group-directories-first' 
#sudo apt install -y exa

# Printing and bluetooth (if needed)
#sudo apt install -y cups
# sudo apt install -y bluez blueman

# sudo systemctl enable bluetooth
sudo systemctl enable cups

# Browser Installation (eg. chromium)
#sudo apt install -y firefox-esr 

# Desktop background browser/handler 
# feh --bg-fill /path/to/directory 
# example if you want to use in autostart located in ~/.local/share/dwm/autostart.sh
sudo apt install -y feh
# sudo apt install -y nitrogen 

# Packages needed qtile after installation
sudo apt install -y picom dunst notification-daemon rofi libnotify-bin unzip p7zip

# Command line text editor -- nano preinstalled  -- I like micro but vim is great
sudo apt install -y micro xclip
# sudo apt install -y neovim

# Install fonts and papirus icon theme and arc-theme
sudo apt install -y fonts-font-awesome fonts-ubuntu fonts-liberation2 fonts-liberation fonts-terminus

# MY STUFF 
sudo apt install -y nala
sudo nala install -y  flameshot psmisc mangohud bibata-cursor-theme big-cursor 
sudo nala install -y lm-sensors fancontrol fonts-noto-color-emoji  htop btop caprine
sudo nala install -y mpv yt-dlp moc ffmpegthumbnailer python3-pil l3afpad galculator 

git clone https://github.com/alvatip/Nordzy-cursors
cd Nordzy-cursors
./install.sh
cd $builddir
rm -rf Nordzy-cursors

# DEB_GET WIMPYSWORLD
sudo nala install curl lsb-release wget
curl -sL https://raw.githubusercontent.com/wimpysworld/deb-get/main/deb-get | sudo -E bash -s install deb-get

deb-get install brave-browser code 

### KERNAL XANMOD 
wget -qO - https://dl.xanmod.org/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/xanmod-archive-keyring.gpg

echo 'deb [signed-by=/usr/share/keyrings/xanmod-archive-keyring.gpg] http://deb.xanmod.org releases main' | sudo tee /etc/apt/sources.list.d/xanmod-release.list

# Create folders in user directory (eg. Documents,Downloads,etc.)
xdg-user-dirs-update

# Installing Lightdm
sudo apt install lightdm lightdm-gtk-greeter-settings -y
sudo systemctl enable lightdm

# Adding qtile.desktop to Lightdm xsessions directory
cat > ./temp << "EOF"
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Type=Application
Keywords=wm;tiling
EOF
sudo cp ./temp /usr/share/xsessions/qtile.desktop;rm ./temp
u=$USER
sudo echo "Exec=/home/$u/.local/bin/qtile start" | sudo tee -a /usr/share/xsessions/qtile.desktop



sudo nala autoremove

printf "\e[1;32mDone! you can now reboot.\e[0m\n"
