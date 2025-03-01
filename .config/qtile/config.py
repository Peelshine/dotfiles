# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.widget import base
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import psutil
from subprocess import run, Popen
from os import system, path
import pyautogui as pag

Nord = {
    "Polar-1":   "#2e3440",
    "Polar-2":   "#3b4252",
    "Polar-3":   "#434c5e",
    "Polar-4":   "#4c566a",

    "Snow-1":    "#d8dee9",
    "Snow-2":    "#e5e9f0",
    "Snow-3":    "#eceff4",

    "Frost-1":   "#8fbcbb",
    "Frost-2":   "#88c0d0",
    "Frost-3":   "#81a1c1",
    "Frost-4":   "#5e81ac",

    "Aurora-1":  "#bf616a", # Red
    "Aurora-2":  "#d08770", # Orange
    "Aurora-3":  "#ebcb8b", # Yellow
    "Aurora-4":  "#a3be8c", # Green
    "Aurora-5":  "#b48ead" # Purple
}

mod = "mod4"
alt = "mod1"
meta = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "a", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "control"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, alt], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, alt], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, alt], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, alt], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # Monitor controls
    Key([mod], "s", lazy.to_screen(0), desc="Go to screen 0"),
    Key([mod], "d", lazy.to_screen(1), desc="Go to screen 1"),
    # Command shortcuts
    Key([mod], "Space", lazy.spawn("rofi -show run"), desc="Show the rofi run dialog"),
    Key([mod, alt], "Space", lazy.spawn("rofi -show window"), desc="Show the rofi window dialog"),
    Key([mod], "w", lazy.spawn("librewolf"), desc="Open librewolf"),
    Key([mod], "e", lazy.spawn("Thunar"), desc="Open thunar"),
    Key([mod, alt], "w", lazy.spawn("flameshot gui"), desc="Take a GUI Screenshot"),
    Key([mod], "v", lazy.spawn('flatpak run it.mijorus.smile'), desc='Open emoji picker'),
    
    # Some other stuff idfk bro
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    #Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

# groups = [Group(i) for i in "123456789"]
groups = [
    Group("1", matches=[Match(wm_class="Sober")]),
    Group("2", matches=[Match(wm_class="LibreWolf")]),
    Group("3", matches=[Match(wm_class="discord")]),
    Group("4", matches=[Match(wm_class="steam")]),
    Group("5", matches=[Match(wm_class="Quodlibet")]),
    Group("6", matches=[Match(wm_class="obs")]),
    Group("7"),
    Group("8"),
    Group("9"),
]

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
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


def init_layout_theme():
    return {"border_on_single":True,
            "margin":3,
            "border_width":4,

            "border_focus": Nord["Aurora-1"],

            "border_normal": Nord["Polar-4"],
           }


layout_theme = init_layout_theme()

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraMono Nerd Font",
    fontsize=14,
    padding=3,
    border=Nord["Aurora-1"],
    foreground=Nord["Snow-3"]
)
extension_defaults = widget_defaults.copy()

class button_that_does_thing(base._TextBox):

    def left_clicK_method():
        print('balls')

    def __init__(self, **config):
        super().__init__("", **kwargs)
        self.add_callbacks(
            {
                "Button1": self.left_clicK_method
            }
        )

    

screens = [
    Screen(
        top=bar.Bar(
            [
            #widget.TextBox("reload_test", name="reload_test"),

            widget.GroupBox(
		    this_current_screen_border=Nord["Frost-2"],
		    this_screen_border=Nord["Frost-4"],
            other_current_screen_border=Nord["Frost-2"],
		    other_screen_border=Nord["Frost-4"],
		    highlight_method="line",
		    highlight_color=Nord["Polar-1"],
		    inactive=Nord["Polar-2"],
		    urgent_border=Nord["Aurora-1"],
		    margin_x=0,
		    disable_drag=True,
		    toggle=False,
		    markup=True,
		    fmt="{}"
		),

        widget.NvidiaSensors(
            format="{perf}{}test",
            threshold=0,
            
        ),

        widget.CPUGraph(
            border_color=Nord["Polar-4"],
            graph_color=Nord["Frost-3"],
            fill_color=Nord["Frost-4"],
            # type="line",
		),

		# widget.TextBox(f"{str(psutil.cpu_percent()).ljust(5)}  ", foreground=Nord["Frost-3"]),
		# UpdatingTextBox(),

		widget.MemoryGraph(
            border_color=Nord["Polar-4"],
            graph_color=Nord["Frost-3"],
            fill_color=Nord["Frost-4"],
            # type="line",
		),

        widget.HDDBusyGraph(
            border_color=Nord["Polar-4"],
            graph_color=Nord["Frost-3"],
            fill_color=Nord["Frost-4"],
            # type="line",
            device="nvme0n1"
        ),

		widget.NetGraph(
            border_color=Nord["Polar-4"],
            graph_color=Nord["Frost-3"],
            fill_color=Nord["Frost-4"],
            # type="line",
            interface="enp5s0"
        ),
        
		# widget.WindowName(
  #           foreground=Nord["Frost-1"]
		# ),
		
        widget.Net(
            format="{up} {up_suffix}",
            foreground=Nord["Frost-3"]
            
        ),

        widget.TextBox("", foreground=Nord["Frost-2"]),

        widget.Net(
            format="{down} {down_suffix} ".ljust(15),
            foreground=Nord["Frost-3"]
        ),

        widget.Spacer(
		    length=bar.STRETCH
		),
		
		widget.Clipboard(
		    fmt="[ {} ]",
		    max_width=50,
            foreground=Nord["Frost-1"]
		),



		widget.Spacer(
		    length=bar.STRETCH
		),

  #               widget.Pomodoro(
		#     color_inactive=Nord["Frost-3"],
		#     color_active=Nord["Aurora-3"],
		#     color_break=Nord["Aurora-1"],
		#     length_pomodori=25,
		#     length_long_break=15,
		#     length_short_break=5,
		#     prefix_inactive="Pomodoro",
 	#         prefix_active="",
		#     prefix_break="",
		#     prefix_long_break="",
		#     prefix_paused="Paused",
		# ),

                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),

        widget.Clock(
		    format="%Y-%m-%d    %a    %I:%M:%S %p   ",
		    foreground=Nord["Frost-3"]
		),

        widget.QuickExit(
            default_text="[x]  ",
            countdown_format="[{}]  ",
            foreground=Nord["Frost-1"]
        ),
        
            ],
            30,
            background = Nord["Polar-1"],
            margin = 0,
            border_width=[4, 4, 4, 4],  # up right down left
            border_color=[Nord["Polar-4"], Nord["Polar-4"], Nord["Polar-4"], Nord["Polar-4"]],
            
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
        wallpaper='/home/rio/pictures/Wallpapers/56.png'
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


@hook.subscribe.startup_once
def autostart():
    home = path.expanduser('~/.config/qtile/autoshart.sh')
    Popen([home])


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="Tk"),
        Match(wm_class="2d_bullethell"),
        Match(wm_class="flumberboozle"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "Qtile"
