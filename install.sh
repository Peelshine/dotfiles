#!/usr/bin/bash

sudo pacman -Syu

# Dependencies
sudo pacman -S git stow

git clone https://github.com/Peelshine/dotfiles $HOME/dotfiles
cd $HOME/dotfiles

# See https://www.gnu.org/software/stow for details.
stow .