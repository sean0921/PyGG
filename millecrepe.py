#!/usr/bin/env python3

import gi
from os.path import abspath, dirname, join
import webbrowser

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 

WHERE_AM_I = abspath(dirname(__file__))

######################################################################################

def main(argv=None):
    class Handler:
        def onDestroy(self, *args):
            print("main program is going to be destroyed!")
            Gtk.main_quit()

        def on_mcma_gmt_begin_clicked(self, *args):
            print("mcma_gmt_begin is clicked!")
            gmt_begin_dialog.run()
            gmt_begin_dialog.hide()

        def on_mcma_generate_ps_clicked(self, *args):
            print("mcma_generate_ps is clicked!")

        def on_mcma_remove_last_clicked(self, *args):
            print("mcma_remove_last is clicked!")

        def on_mcma_recover_last_clicked(self, *args):
            print("mcma_recover_last is clicked!")

        def on_mcma_activate_removal_clicked(self, *args):
            print("mcma_activate_removal is clicked!")

        def on_mcma_gmt_docs_clicked(self, *args):
            webbrowser.open("https://docs.generic-mapping-tools.org/index.html")

        def on_mcma_about_clicked(self, *args):
            about_dialog.run()
            about_dialog.hide()

#        def on_mcma_about_dialog_destroy(self, *args):
#            print("mcma_about_dialog is going to be destroyed!")
#            about_dialog.destroy()

        def on_mcma_gmt_commands_changed(self, combo):
            tree_iter = combo.get_active_iter()
            if tree_iter is not None:
                model = combo.get_model()
                name, row_id = model[tree_iter][:2]
                #print(model[tree_iter][:])
                print("Selected: name=%s, ID=%s" % (name, row_id))
            else:
                entry = combo.get_child()
                print("Entered: %s" % entry.get_text())

#        def on_mcma_gmt_gmtset_clicked(self, *args):
#            print("mcma_gmt_gmtset is clicked!")
#
#        def on_mcma_gmt_pscoast_clicked(self, *args):
#            print("mcma_gmt_pscoast is clicked!")
#
#        def on_mcma_gmt_psbasemap_clicked(self, *args):
#            print("mcma_gmt_psbasemap is clicked!")
#
#        def on_mcma_gmt_psxy_clicked(self, *args):
#            print("mcma_gmt_psxy is clicked!")
#
#        def on_mcma_gmt_pssac_clicked(self, *args):
#            print("mcma_gmt_pssac is clicked!")
#
#        def on_mcma_gmt_pstext_clicked(self, *args):
#            print("mcma_gmt_pstext is clicked!")
#
#        def on_mcma_gmtcustom_clicked(self, *args):
#            print("mcma_gmtcustom is clicked!")
#
#        def on_mcma_gmt_end_clicked(self, *args):
#            print("mcma_gmt_end is clicked!")

    ### Example
    #    def onButtonPressed(self, button):
    #        print("Hello World!")

    builder = Gtk.Builder()

    glade_file_mainwindow = join(WHERE_AM_I, 'mainwindow.glade')
    builder.add_from_file(glade_file_mainwindow)

    glade_file_about_dialog = join(WHERE_AM_I, 'about_dialog.glade')
    builder.add_from_file(glade_file_about_dialog)

    glade_file_gmt_begin_dialog = join(WHERE_AM_I, 'gmt_begin_dialog.glade')
    builder.add_from_file(glade_file_gmt_begin_dialog)

    window = builder.get_object("mcma_main")
    about_dialog = builder.get_object("mcma_about_dialog")
    gmt_begin_dialog = builder.get_object("mcma_gmt_begin_dialog")

    builder.connect_signals(Handler())
    
    window.show_all()
    Gtk.main()

######################################################################################

if __name__ == "__main__":
    main()
