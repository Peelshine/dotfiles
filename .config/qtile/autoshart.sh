#!/bin/sh

picom -b &
echo picom done

pulseaudio --start
echo pulse done

sh $HOME/.xrandr-setup.sh
echo xrandr done

sh $HOME/.fehbg
echo fehbg done
