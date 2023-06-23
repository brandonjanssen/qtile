#!/bin/bash


/etc/xdg/autostart/lxpolkit.desktop &
#/usr/bin/lxpolkit &
dunst &
xdg-user-dirs-update &
#/etc/xdg/autostart/polkit-gnome-authentication-agent-1.desktop &
#lxsession &
feh --randomize --bg-fill /home/dmne/Pictures/background &
#nitrogen --restore &
#picom -f &
picom &
#picom --experimental-backend &
#blueberry-tray &
#blueman-applet &
#pasystray --notify=all instead &
#pasystray &
#nm-applet &
#gammy &
# syncthing &
# mpd &
#volumeicon &
xmodmap  -e 'clear lock'
#cbatticon &
variety &
xbindkeys -f ~/.xbindkeysrc &
#cbatticon -u 20 -i notification -c "poweroff" -l 15 -r 10 &
# cbatticon  -i notification /sys/class/power_supply/BAT0 &
#xrandr --output HDMI-A-0 --mode 1366x768 --rate 59.79 --output eDP --off &
#/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 & 

