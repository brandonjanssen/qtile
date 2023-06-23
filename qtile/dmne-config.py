import os
import subprocess
from typing import List  # noqa: F401

from libqtile import hook

from libqtile.bar import Bar

from libqtile.widget.window_count import WindowCount
from libqtile.widget.prompt import Prompt
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.windowname import WindowName
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.generic_poll_text import GenPollUrl

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal



@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh') # path to my script, under my user directory
    subprocess.call([home])
    
    
# mod = "mod4"
# terminal = guess_terminal()
#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    # Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    # Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    # Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    # Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod], "l", lazy.layout.grow()),
    Key([mod], "h", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "a", lazy.layout.flip()),
    # Key([mod,"control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    # Key([mod,"control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    # Key([mod,"control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod,"control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "f",
            lazy.window.toggle_floating(),
            desc='toggle floating'
            ),

    ### Switch focus to specific monitor (out of three)
    # Key([mod], "o",
    #     lazy.to_screen(0),
    #     desc='Keyboard focus to monitor 1'
    #     ),
    # Key([mod], "s",
    #     lazy.to_screen(1),
    #     desc='Keyboard focus to monitor 2'
    #     ),
    # Key([mod], "d",
    #     lazy.to_screen(2),
    #     desc='Keyboard focus to monitor 3'
    #     ),
    # ### Switch focus of monitors
    # Key([mod], "period",
    #     lazy.next_screen(),
    #     desc='Move focus to next monitor'
    #     ),
    # Key([mod], "comma",
    #     lazy.prev_screen(),
    #     desc='Move focus to prev monitor'
    #     ),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    #Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    ##################################################################
    ######### START OF MY APPS #######################################
    ##################################################################

    ### BROWSER ##############
    Key([mod], "w", lazy.spawn("google-chrome-stable")),

    ### TERMINAL APPS  ########
    Key([mod], "Return", lazy.spawn("xfce4-terminal -e fish")),
    Key([mod], "m", lazy.spawn("xfce4-terminal -e mocp")),
    Key([mod], "v", lazy.spawn("xfce4-terminal -e vim")),
    Key([mod,"shift"], "v", lazy.spawn("xfce4-terminal -e vim .config/qtile/config.py")),
    Key([mod,"control"], "t", lazy.spawn("xfce4-terminal -e nnn")),
    Key([mod,"shift"], "t", lazy.spawn("xfce4-terminal -e ranger")),

    ###  SEARCH  ######################
    Key([mod], "space", lazy.spawn("rofi -show drun -show-icons -modi drun,run")),
    Key([mod2], "space", lazy.spawn("rofi -show calc")),

    ###  EDITOR  #############
    Key([mod], "e", lazy.spawn("lapce")),

    ###  WRITING  ############
    Key([mod], "o", lazy.spawn("obsidian")),
    Key([mod,"shift"], "o", lazy.spawn("libreoffice")),

    ### FILE-MANAGERS  ########
    Key([mod], "t", lazy.spawn("thunar")),

    ### SOCIAL APPS  ##########
    Key([mod], "s", lazy.spawn("/home/dmne/Downloads/session-desktop-linux-x86_64-1.8.6.AppImage ")),
    Key([mod,"shift"], "s", lazy.spawn("skypeforlinux ")),
    Key([mod,"control"], "s", lazy.spawn("telegram-desktop ")),
    Key([mod], "d", lazy.spawn("discord")),

    ### COLOR-PICKER  #########
    Key([mod], "g", lazy.spawn("gpick")),

    ### CALCULATOR  ##################
     Key([mod,"shift"], "g", lazy.spawn("galculator")),

    ### MEDIA  ###############
    Key([mod], "r", lazy.spawn("feh --randomize --bg-fill /home/dmne/Pictures/background")),

    ###  LOGOUT  ##############
    Key([mod], "x", lazy.spawn("/usr/bin/clearine ")),

# Emacs programs launched using the key chord CTRL+e followed by 'key'                       
        KeyChord([mod],"i", [
            Key([], "e",
                lazy.spawn("lapce"),
                desc='lapce'
                ),
            Key([], "s",
                lazy.spawn("/home/dmne/Applications/session-desktop-linux-x86_64-1.10.1.AppImage"),
                desc='Sessions'
                )
        ]),
    
    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10")),

# INCREASE/DECREASE/MUTE VOLUME
    # Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    # Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 3%-")),
    # Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 3%+")),
    
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -3%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +3%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

#=-/ Multimedia keys /-=#
    # Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -10%")),
    # Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +10%")),
    # Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),    

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),



]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(margin=13, border_width=2, border_focus="#3f92f7", border_normal="#a17a06"),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.MonadThreeCol(
    margin=13,
    border_width=3,
    border_focus="#3f92f7",
    border_normal="#fdb302"   
    ),
    # layout.Matrix(),
    #layout.MonadTall(
     #margin=13,
     #border_width=3,
    # border_focus="#3f92f7",
     #border_normal="#fdb302"),
    # layout.MonadWide(),
    # layout.RatioTile(
    #  margin=13,
    #  border_width=3,
    #  border_focus="#3f92f7",
    #  border_normal="#fdb302"),   
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(
    #   margin=13,
    #  border_width=3,
    #  border_focus="#3f92f7",
    #  border_normal="#fdb302"),  
    
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraCode Bold",
    # font="sans",
    fontsize=11,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(
                    # disable_drag=True,
                    active='#05ff00',
                    inactive='#3f92f788',
                    rounded=True,
                    highlight_method='line',
                    # block_highlight_text_color='red',
                    borderwidth=3,
                    highlight_color='#383838',
                    background='#3B426188',
                    # background_inactive='#1f2335',
                    # background_active='#ffffff',
                ),
                widget.Prompt(),
                widget.WindowName(
                    foreground="#ffffff",
                    font='FiraCode Italic',
                    # font='FiraCode Bold Italic',
                    fontsize=8,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Moc(
                    # background=
                    foreground="#ffffff",
                    font='FiraCode Bold Italic',
                    fontsize=8,
                    update_interval=1
                ),
                widget.Sep(
                #    background="",
                    foreground="#3B4261",
               #    linewidth="0",
                    padding=10,
                ),
                widget.CryptoTicker(
                    crypto='BTC',
                    foreground="#ffffff",
                    # foreground="#c1c1c1",
                    currency = 'USD',
                    symbol = '$',
                    font = 'FiraCode',
                    fontsize ='9',
                ),
                widget.Sep(
                #    background="",
                foreground="#3B4261",
               #    linewidth="0",
                padding=2,
                ),
                 widget.Net(
                    font="FiraCode Bold",
                   #fontsize=12,
                    interface="wlan0",
                    format = '{down} ↓↑ {up}',
                    foreground="#11eeca",
                    # foreground="#ff0011",
                    # background= "#006bff",
                    padding = 0,
                ),
               #  widget.Sep(
               #  #    background="",
               #      foreground="#1f2335",
               # #    linewidth="0",
               #      padding=2,
               #  ),
                # widget.Battery(
                #     foreground="#3F92F7"
                # ),

                widget.Sep(
                    # background="#ffffff80",
                    foreground="#3B4261",
                    # foreground="#1F2335",
                    #    linewidth="0",
                    padding=10,
                ),

                widget.CPU(
                   # format="CPU {freq_current}GHz {load_percent}%"
                    foreground="#eedf17",
                    # foreground="#ff00b3",
                    # background="#ff0055",
                    threshold = 90,
                    padding = 5,
                ),

                widget.Sep(
               #    background="",
                    foreground="#3B4261",
               #    linewidth="0",
                    padding=10,
                ),

                widget.Memory(
                    # background="#fdb302",
                    foreground="#4dee17",
                   # font=
                  # fontsize=9,
                ),

                widget.Sep(
                    #    background="",
                    foreground="#3B4261",
                    #    linewidth="0",
                    padding=10,
                ),
                widget.DF(


                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # widget.Thermal_zone(),
                widget.ThermalSensor(
                        foreground = "#a550d7",
                        # foreground = "#f3f50c",
                        foreground_alert = "#FF0000",
                        # background = "#7f88ae",
                        metric = True,
                        padding = 3,
                        threshold = 80
                        ),
                widget.Sep(
                        # background="#ffffffff",
                        foreground="#3B4261",
                    #    linewidth="0",
                        padding=10,
                ),        
                widget.Clock(
                    format="%a %b %d  %H:%M",
                    foreground="#c1c1c1",
                    # background="#ab00fa",
                ),
                widget.Sep(
                    #    background="",
                    foreground="#3B4261",
                    #    linewidth="0",
                    padding=10,
                ),    
                widget.Systray(
                    background="#3B4261",
                    # background="#7f88ae",
                    # background="#1f233580",
                ),
                # widget.Sep(
                #     # background="#9BA5D3",
                #     foreground="#1F2335",
                #     #    linewidth="0",
                #     padding=10,
                # ),
                # widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                # widget.QuickExit(),
            ],
            margin=[0, 0, 0, 0],
            #margin=[26, 26, 5, 10], ### good for laptop
            background='#3B4261',
            # background='#3B426188',
            # background='#1f2335',
            opacity=1,
            size=16,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="blueman-manager"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="Gpick"),  # ssh-askpass
        Match(wm_class="galculator"),  # ssh-askpass
        #Match(wm_class="Kazam"),  # ssh-askpass
        #Match(wm_class="kazam"),  # ssh-askpass
        Match(wm_class="pavucontrol"),  # ssh-askpass
        Match(wm_class="Imager"),  # ssh-askpass
        Match(wm_class="NoiseTorch-ng"),  # ssh-askpass
        Match(wm_class="SpeedCrunch"),  # ssh-askpass
        Match(wm_class="system-config-printer"),  # ssh-askpass
        Match(wm_class="crx_dmkamcknogkgcdfhhbddcghachkejeap"),  # ssh-askpass
        Match(wm_class="crx_nkbihfbeogaeaoehlefnkodbefgpgknn"),  # ssh-askpass
        Match(wm_class="crx_jiidiaalihmmhddjgbnbgdfflelocpak"),  # ssh-askpass
        Match(wm_class="crx_mfgccjchihfkkindfppnaooecgfneiii"),
        Match(wm_class="Scanner"),  # ssh-askpass
        Match(wm_class="InfinityWallet"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# @hook.subscribe.startup_once
# def autostart():
#     home = os.path.expanduser('~/.config/qtile/autostart.sh')
#      subprocess.Popen([home])

# @hook.subscribe.startup_once
# def autostart():
#     home = os.path.expanduser('~')
#     subprocess.call([home + '.config/qtile/autostart.sh'])
    
