import gi
import webbrowser

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def on_mcma_gmt_begin_clicked(self, *args):
        print("mcma_gmt_begin is clicked!")

    def on_mcma_generate_ps_clicked(self, *args):
        print("mcma_generate_ps is clicked!")

    def on_mcma_remove_last_clicked(self, *args):
        print("mcma_remove_last is clicked!")

    def on_mcma_recover_last_clicked(self, *args):
        print("mcma_recover_last is clicked!")

    def on_mcma_activate_removal_clicked(self, *args):
        print("mcma_activate_removal is clicked!")

    def on_mcma_gmt_docs_clicked(self, *args):
        print("mcma_gmt_docs is clicked!")
        webbrowser.open("https://docs.generic-mapping-tools.org/6.0/index.html")

    def on_mcma_gmt_gmtset_clicked(self, *args):
        print("mcma_gmt_gmtset is clicked!")

    def on_mcma_gmt_pscoast_clicked(self, *args):
        print("mcma_gmt_pscoast is clicked!")

    def on_mcma_gmt_psbasemap_clicked(self, *args):
        print("mcma_gmt_psbasemap is clicked!")

    def on_mcma_gmt_psxy_clicked(self, *args):
        print("mcma_gmt_psxy is clicked!")

    def on_mcma_gmt_pssac_clicked(self, *args):
        print("mcma_gmt_pssac is clicked!")

    def on_mcma_gmt_pstext_clicked(self, *args):
        print("mcma_gmt_pstext is clicked!")

    def on_mcma_gmtcustom_clicked(self, *args):
        print("mcma_gmtcustom is clicked!")

    def on_mcma_gmt_end_clicked(self, *args):
        print("mcma_gmt_end is clicked!")

### Example
#    def onButtonPressed(self, button):
#        print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("mainwindow.glade")
builder.connect_signals(Handler())

window = builder.get_object("mcma_main")
window.show_all()

Gtk.main()
