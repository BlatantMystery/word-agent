import os
import io
from collections import deque
from difflib import SequenceMatcher, ndiff, restore
from gi.repository import Gtk

from WordAgent import *

welcome_message = """
    Welcome to the Word Agent, the novel project management app!

    Features currently in development:
        Undo/Redo
        File IO

    Next Feature in the works:
        Project management
        "Post Production" formatting (Scribus integration?)

    Future Features:
        Version Control System integration
        Cloud Collaboration with WebRTC
"""

bob = Gtk.Builder()
bob.add_from_file("WordAgentApp.glade")

seg_bfr = SegmentBuffer(welcome_message)
txt_box = bob.get_object("editView")
txt_box.set_buffer(seg_bfr)

os.chdir("/home/sam/Documents/testing")
project_name = "default.wa.txt"

win = bob.get_object("mainWindow")

bob.connect_signals(SignalHandler(seg_bfr, project_name))

win.show_all()
Gtk.main()
