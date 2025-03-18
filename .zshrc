# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Set directory for zinit and plugins
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"

# Download zinit if it isn't already there
if [ ! -d "$ZINIT_HOME" ]; then
    mkdir -p "$(dirname $ZINIT_HOME)"
    git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi

# Load zinit
source "${ZINIT_HOME}/zinit.zsh"

# Load Powerlevel10k
zinit ice depth=1; zinit light romkatv/powerlevel10k

# Load zsh plugins
#zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light Aloxaf/fzf-tab
zinit light MichaelAquilina/zsh-autoswitch-virtualenv
zinit light zdharma-continuum/fast-syntax-highlighting

# Im gonna be so fr i have no idea what this does im just copying most of this
# line by line from the Dreams of Autonomy zsh config video
autoload -U compinit && compinit
zinit cdreplay -q

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# Keybindings
bindkey '^ ' autosuggest-accept
bindkey '^b' history-search-backward
bindkey '^n' history-search-forward

# Alacritty nav keys
bindkey '^[[H' beginning-of-line
bindkey '^[[F' end-of-line
bindkey '^[[3~' delete-char
bindkey '^[[1;3D' backward-word
bindkey '^[[1;3C' forward-word

# TTY nav keys
bindkey '^[[1~' beginning-of-line
bindkey '^[[4~' end-of-line
bindkey '^[[3' delete-char

# History
HISTSIZE=5000
HISTFILE=~/.zsh_history
SAVEHIST=$HISTSIZE
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_dups
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_find_no_dups

export FZF_DEFAULT_OPTS=" \
#--color=bg+:#ccd0da,bg:#eff1f5,spinner:#dc8a78,hl:#d20f39 \
--color=fg:#4c4f69,header:#d20f39,info:#8839ef,pointer:#dc8a78 \
--color=marker:#7287fd,fg+:#4c4f69,prompt:#8839ef,hl+:#d20f39 \
--color=selected-bg:#bcc0cc \
--color=border:#ccd0da,label:#4c4f69"

# Completion styling
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview #'ls --color $realpath'
zstyle ':fzf-tab:complete:__zoxide_z:*' fzf-preview #'ls --color $realpath'

# Aliases
alias hx='helix'

# Git aliases
alias g='git'
alias gs='git status'
alias gd='git diff'
alias gc='git commit'
alias gps='git push'
alias gpl='git pull'
alias ga='git add'
alias gaa='git add --all'

# Python aliases
alias py='python3'
alias pyserv='py -m http.server'

# Flag aliases
alias yt-dlp-music='yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0'
alias ls='ls -a --color'
alias slurp='slurp -b #00000050 -c #ffffff25 -s #ffffff00'

# Tool aliases
alias u='cd ..'
alias uu='cd ..;cd ..'
alias uuu='cd ..;cd ..; cd ..'
alias uuuu='cd ..;cd ..; cd ..; cd ..'
alias uuuuu='cd ..; cd ..; cd ..; cd ..; cd ..'

alias gpu="sudo nvidia-smi daemon & gpustat --no-processes -i"

# Functions
mkcd() {
    mkdir -p "${1}"
    cd "${1}"
}

gip() {
    echo Local:
    hostname -I | grep -Eo '([0-9]*\.){3}[0-9]*' | grep 192.168
    echo Public:
    curl https://api.ipify.org
    echo
    curl -s https://api.ipify.org | xclip -selection clipboard
}

# Path extensions
export PATH=$PATH:$HOME/.cargo/env
export PATH=$PATH:$HOME/.cargo/bin
export PATH=$PATH:$HOME/.bin
export PATH=$PATH:$HOME/.local/bin

# Shell integrations
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
eval "$(thefuck --alias)"
eval "$(zoxide init --cmd cd zsh)"
