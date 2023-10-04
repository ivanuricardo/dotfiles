from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#2f343f", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"), 
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96",
                                other_current_screen_border="#74438f",
                                other_screen_border="#74438f",
                                background="#2f343f"),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ),    
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#99c0de',fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                    background="#2f343f"),
                widget.Systray(icon_size = 20),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ), 
                widget.Sep(padding=8, linewidth=0, background="#2f343f"), 
                widget.Wttr(
   		       location={"Maastricht": "MAAS"}
		       ),
                widget.Sep(padding=8, linewidth=0,), 
                widget.Battery(format="{percent:2.0%}"),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"), 
                volume,
                widget.Sep(padding=4, linewidth=0, background="#2f343f"), 
                widget.TextBox(                                                
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f',
                       ),   
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ),    
                widget.Clock(format='󰥔 %Y-%m-%d %a %H:%M',
                             background="#2f343f",
                             foreground='#9bd689'),
                                                widget.TextBox(                                                
                                                
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f',
                       ),   
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378'
                ),
                widget.Sep(padding=10, linewidth=0, background="#404552")
                
            ],
            30,  # height in px
            background="#404552"  # background color
        ), ),
]
