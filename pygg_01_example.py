import sys
import subprocess
import gi
import pygmt

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

fig  = pygmt.Figure()
fig2 = pygmt.Figure()

class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Map Generator")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Philippines Map")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Leyte")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Close")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print('"Philippines Map" will be generated')
        fig.basemap(region=[116.0,128.0,4.0,22.0], projection='M16c', frame='a2f0.5',X='4c')
        fig.coast(W='0.1p,black',S='0/0/255',G='#73bf00',D='f',frame='WSne+t"Philippines\' Map"')
        fig.savefig("phip_test.png")
        print('"Philippines Map" is generated')
        if sys.platform == "linux":
            subprocess.run(["xdg-open","phip_test.png"], capture_output=True)
        Gtk.main_quit()

    def on_open_clicked(self, button):
        print('"Leyte Map" will be generated')
        fig2.basemap(region=[124.0,125.5,9.75,11.75], projection='M16c', frame='a2f0.5',X='4c')
        fig2.coast(W='0.1p,black',S='0/0/255',G='#73bf00',D='f',frame='WSne+t"Leyte\'s Map"')
        fig2.savefig("Leyte_test.png")
        print('"Leyte Map" is generated')
        if sys.platform == "linux":
            subprocess.run(["xdg-open","Leyte_test.png"], capture_output=True)
        Gtk.main_quit()

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
