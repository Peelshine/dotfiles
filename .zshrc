# If you come from bash you might have to change your $PATH.
# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time Oh My Zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="flumber"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(rust)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='nvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch $(uname -m)"

# Set personal aliases, overriding those provided by Oh My Zsh libs,
# plugins, and themes. Aliases can be placed here, though Oh My Zsh
# users are encouraged to define aliases within a top-level file in
# the $ZSH_CUSTOM folder, with .zsh extension. Examples:
# - $ZSH_CUSTOM/aliases.zsh
# - $ZSH_CUSTOM/macos.zsh
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"



mkcd() {
    mkdir -p "${1}"
    cd "${1}"
}



alias g="git"

# alias vencord="sh -c "$(curl -sS https://raw.githubusercontent.com/Vendicated/VencordInstaller/main/install.sh)""

# alias fabric="deno run https://fabricmc.net/cli"

alias ezrc="micro ~/.zshrc"
alias ebrc="micro ~/.bashrc"
alias eqcf="micro ~/.config/qtile/config.py"

alias co="echo $PWD > ~/.cio"
alias ci="cio="$(cat ~/.cio)"; cd $cio"

alias py="python3"
alias pysv="py -m http.server"
alias godotserve="py serve.py -r ."
alias rp="py main.py"

alias vtop="vtop --theme nord"
alias ls="ls -a"

alias gpu="sudo nvidia-smi daemon & gpustat --no-processes -i"

alias warp="warp-terminal"
alias nv="nvim"
alias mc="micro"
alias cld="cloudflared"

alias tsv="bash /home/rio/.local/share/Steam/steamapps/common/tModLoader/start-tModLoaderServer.sh -steam -lobby friends -world /home/rio/.local/share/Terraria/tModLoader/Worlds/International_Baddies_HQ.wld"

alias acv="python3 $HOME/Projects/python/acvbot/main.py"
alias gip="python3 $HOME/Projects/python/get-ip/main.py"
alias gpip="ip a | grep "192""
alias curli="python3 $HOME/Projects/python/curli/main.py"

# alias idea="sh /home/rio/Applications/intellij/idea-IU-233.11799.300/bin/idea.sh"

# alias sober="flatpak run org.vinegarhq.Sober"
# alias vinegar="flatpak run org.vinegarhq.Vinegar"
# alias obs="flatpak run com.obsproject.Studio"
# alias flatseal="flatpak run com.github.tchx84.Flatseal"
# alias bottles="flatpak run com.usebottles.bottles"
alias apt="sudo apt"
alias apt-get="sudo apt-get"
alias dpkg="sudo dpkg"

alias u="cd .."
alias uu="cd ..;cd .."
alias uuu="cd ..;cd ..; cd .."
alias uuuu="cd ..;cd ..; cd ..; cd ..;"
alias uuuuu="cd ..; cd ..; cd ..; cd ..; cd ..;"

alias gdf='cd ~/dotfiles'
alias gfb="cd ~/fb"
alias gdl="cd ~/Downloads"
alias gdc="cd ~/Documents"
alias gpc="cd ~/Pictures"
alias gvd="cd ~/Videos"
alias gms="cd ~/Music"
alias gpj="cd ~/Projects"
alias gppj="cd ~/Projects/python"
alias ggpj="cd ~/Projects/godot"
alias grpj="cd ~/Projects/rust"
alias gjpj="cd ~/Projects/java"
alias gupj="cd ~/Projects/ursina"
alias ggm="cd ~/Games"
alias gap="cd ~/Applications"
alias gsv="cd ~/Servers"
alias gas="cd ~/Assignments"
alias gsd="cd ~/sd"
alias gsl="cd ~/silly"
alias gdk="cd ~/devkits"
alias ggh="cd ~/git"
alias gcf="cd ~/.config"
alias glc="cd ~/.local"
export QMK_HOME="~/qmk_firmware"
export DENO_INSTALL="/home/rio/.deno"

fpath+=~/.zfunc

export PATH=$PATH:$HOME/bin:$HOME/.local/bin:/usr/local/bin:/usr/bin:/usr/local/games
export PATH=$PATH:/usr/local/go/bin
export PATH=$PATH:/usr/games
export PATH=$PATH:/$DENO_INSTALL/bin
export PATH=$PATH:$HOME/Applications/helix
export PATH=$PATH:$HOME/.cargo/env
export PATH=$PATH:$HOME/.cargo/bin

eval $(thefuck --alias)
