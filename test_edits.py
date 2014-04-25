import os
import tempfile
import difflib
from gi.repository import Gtk

from WordAgent import *

print("Begin editing testing suite")

init_msg = "Initialized "

edits = ["I'm a different starting buffer",
"I've changed the buffer",
"I'm going to write a story",
"Once upon a time...",
"Once upone a time, in a land far far away...",
"Macabre murder mysteries make more money.",
"Macabre murder mysteries make much more money!",
"Macabre murder mysteries make much more money!"]

seg_bfr = SegmentBuffer()
print(init_msg, seg_bfr)

diff = SequenceDiffer()
print(init_msg, diff)

clerk = FileClerk()
print(init_msg, clerk)

signal = SignalHandler(seg_bfr, diff, clerk)
print(init_msg, signal)

print("Starting to loop through edits, no undo or redos here")
edits = enumerate(edits)
for e in edits:
    num, txt = e
    print("Loop #", num, "-----")
    print("Current edit: ", txt)
    print("seg_bfr.copy is ", seg_bfr.copy)
    print("seg_bfr.undos is ", seg_bfr.undos)
    diff.set_seqs(txt, seg_bfr.copy)
    ratio = diff.quick_ratio()
    print("diff.quick_ratio between txt and seg_bfr.copy: ", ratio)
    print("Setting seg_bfr.copy to text of edit")
    seg_bfr.copy = txt

    print("seg_bfr.copy is now", seg_bfr.copy)
    print("seg_bfr.undos is now", seg_bfr.undos)
