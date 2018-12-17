#!/usr/bin/env python3
import subprocess
import gi.repository
gi.require_version('Budgie', '1.0')
from gi.repository import Budgie, GObject, Gtk

class RunScriptsAndCommands(GObject.GObject, Budgie.Plugin):

    __gtype_name__ = "RunScriptsAndCommands"

    def __int__(self):
        GObject.Object.__init__(self)

    def do_get_panel_widget(self, uuid):
        return RunScriptsAndCommandsApplet(uuid)


class RunScriptsAndCommandsApplet(Budgie.Applet):

    manager = None

    def __init__(self, uuid):

        Budgie.Applet.__init__(self)

        self.box = Gtk.EventBox()
        self.add(self.box)
        img = Gtk.Image.new_from_icon_name("xterm-color", Gtk.IconSize.MENU)
        self.box.add(img)
        self.menu = Gtk.Menu()
        self.create_menu()
        self.box.show_all()
        self.show_all()

    def funct1(self, menuitem):
        print(menuitem)
        subprocess.call("nautilus", Shell=True)

    def funct2(self, menuitem):
        print(menuitem)
        subprocess.call("sh /path/to/your/script.sh", Shell=True)

    def create_menu(self):
        item1 = Gtk.MenuItem('Nautilus')
        item1.connect("activate", self.funct1)
        item2 = Gtk.MenuItem('Your script')
        item2.connect("activate", self.funct2)
        for item in [item1, item2]:
            self.menu.append(item)
        self.menu.show_all()
        self.box.connect("button-press-event", self.popup_menu)

    def popup_menu(self, *args):
        self.menu.popup(
            None, None, None, None, 0, Gtk.get_current_event_time()
        )
