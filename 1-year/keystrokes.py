#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class LetterGame:
    keyval_name_to_unicode = {'Right': '→',
                              'Up': '↑',
                              'Left': '←',
                              'Down': '↓'
                              }

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def key_press(self, widget, event, data):
        keyname = gtk.gdk.keyval_name(event.keyval)
        codepoint = gtk.gdk.keyval_to_unicode(event.keyval)
        keyval_name = gtk.gdk.keyval_name(event.keyval)
        to_display = unichr(codepoint) \
            if codepoint != 0 \
            else self.keyval_name_to_unicode.get(keyval_name, keyval_name)
        data.set_markup('<span size="100000">' + to_display + '</span>')

    def __init__(self):
        self.window = gtk.Window()
        self.window.connect("destroy", self.destroy)
        self.letter_label = gtk.Label("Appuie sur une touche")
        self.letter_label.set_use_markup(True)
        self.window.connect("key_press_event", self.key_press, self.letter_label)
        self.window.add(self.letter_label)
        self.window.fullscreen()
        self.window.set_keep_above(True)
        self.letter_label.show()
        self.window.show()
        self.window.activate_focus()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    LetterGame().main()
