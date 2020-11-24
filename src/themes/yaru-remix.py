# Yaru-remix theme setup
# v20.10.1

import os

# Download theme files
os.system("wget https://github.com/Muqtxdir/yaru-remix/archive/v20.10.1.tar.gz -P $HOME/Downloads")
os.system("tar -xf $HOME/Downloads/v20.10.1.tar.gz -C $HOME/Downloads && rm $HOME/Downloads/v20.10.1.tar.gz")
os.system("mkdir $HOME/.themes && mkdir $HOME/.icons")

# Gtk themes setup
os.system('echo -e "\nStart setup Gtk themes..."')
os.system("cp -r $HOME/Downloads/yaru-remix-20.10.1/gtk/Yaru-remix $HOME/.themes/ && cp -r $HOME/Downloads/yaru-remix-20.10.1/gtk/Yaru-remix-dark $HOME/.themes/")
os.system("cp -r $HOME/Downloads/yaru-remix-20.10.1/gnome-shell/Yaru-remix/gnome-shell $HOME/.themes/Yaru-remix/ && cp -r $HOME/Downloads/yaru-remix-20.10.1/gnome-shell/Yaru-remix-dark/gnome-shell $HOME/.themes/Yaru-remix-dark/")
os.system('gsettings set org.gnome.desktop.interface gtk-theme "Yaru-remix" && gsettings set org.gnome.shell.extensions.user-theme name "Yaru-remix"')

# Icon theme setup
os.system('echo -e "\nStart setup Icon themes..."')
os.system("cp -r $HOME/Downloads/yaru-remix-20.10.1/icons/Yaru-remix $HOME/.icons/ && cp -r $HOME/Downloads/yaru-remix-20.10.1/icons/Yaru-remix-dark $HOME/.icons/")
os.system('gsettings set org.gnome.desktop.interface icon-theme "Yaru-remix"')

# Clear downloaded theme files
os.system('echo -e "\nClearing downloaded files..."')
os.system("rm -R $HOME/Downloads/yaru-remix-20.10.1")