# Budgie-RunScriptsAndCommandsApplet
An applet for the Budgie Desktop to run scripts and commands

*******Currently broken*******

It is based on: https://github.com/phil-hur/budgietestapplet

Thanks a lot to Phil Hur


Installation:

        git clone https://github.com/Liemaeu/Budgie-RunScriptsAndCommandsApplet.git

        sudo mv Budgie-RunScriptsAndCommandsApplet* /usr/lib/budgie-desktop/plugins/Budgie-RunScriptsAndCommandsApplet

        You need to logout and login again

To add a command/a script:

        sudo nano /usr/lib/budgie-desktop/plugins/Budgie-RunScriptsAndCommandsApplet/someapp.py

First you have to define a new function like this:

        def functionname(self, menuitem):

        print(menuitem)
        
        subprocess.call("command", Shell=True)

change functionname and command in what ever you want (for a script the command is: sh /path/to/the/script.sh).

After that, you have to create a new item in the create_menu function, like this:

        itemname = Gtk.MenuItem('name')

        itemname.connect("activate", self.functionname)

change itemname and name in whatever you want, functionname must be the name of the function you defined earlier.

The last step is to change this part of the create_menu function:

        for item in [item1, item2]:

        self.menu.append(item)

In the [ ]  you have to write the names of all your items in, seperated by an ,

        You have to logout and login again to make your changes work 
