'''
Created on Oct 10, 2010

@author: Mark V Systems Limited
(c) Copyright 2010 Mark V Systems Limited, All rights reserved.
'''
from tkinter import *
from tkinter.ttk import *
from arelle.CntlrWinTooltip import ToolTip
import re

'''
caller checks accepted, if True, caller retrieves url
'''
def askURL(parent, url=None):
    dialog = DialogURL(parent, url)
    if dialog.accepted:
        return dialog.url
    return None


class DialogURL(Toplevel):
    def __init__(self, parent, url=None):
        super().__init__(parent)
        self.parent = parent
        parentGeometry = re.match("(\d+)x(\d+)[+]?([-]?\d+)[+]?([-]?\d+)", parent.geometry())
        dialogX = int(parentGeometry.group(3))
        dialogY = int(parentGeometry.group(4))
        self.accepted = False
        self.url = None
        self.transient(self.parent)
        self.title("Enter URL")
        self.urlVar = StringVar()
        self.urlVar.set(url if url is not None else "http://")
        
        frame = Frame(self)
        urlLabel = Label(frame, text=_("URL:"), underline=0)
        urlEntry = Entry(frame, textvariable=self.urlVar, width=60)
        urlEntry.focus_set()
        okButton = Button(frame, text=_("OK"), command=self.ok)
        cancelButton = Button(frame, text=_("Cancel"), command=self.close)
        usSecButton = Button(frame, text=_("SEC search"), command=self.usSec)
        rssButton = Button(frame, text=_("SEC RSS"), command=self.rssFeed)
        urlLabel.grid(row=0, column=0, sticky=W, pady=3, padx=3)
        urlEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
        okButton.grid(row=1, column=2, sticky=E, pady=3)
        ToolTip(okButton, text=_("Opens above URL from web cache, downloading to cache if necessary"), wraplength=240)
        cancelButton.grid(row=1, column=3, sticky=EW, pady=3, padx=3)
        ToolTip(cancelButton, text=_("Cancel operation"))
        usSecButton.grid(row=1, column=1, sticky=W, pady=3)
        rssButton.grid(row=1, column=1, pady=3)
        ToolTip(usSecButton, text=_("Opens US SEC Edgar Company Search (in web browser)\n\n"
                                 "(1) Find the company in web browser,\n"
                                 "(2) Click 'documents' button for desired filing,\n"
                                 "(3) Find 'data files' panel, instance document row, 'document' column,\n"
                                 "(4) On instance document file name, right-click browser menu: 'copy shortcut',\n"
                                 "(5) Come back to this dialog window,\n"
                                 "(6) Ctrl-v (paste) shortcut into above URL text box,\n"
                                 "(7) Click ok button to load instance document"),
                                 wraplength=480)
        ToolTip(rssButton, text=_("Opens current US SEC Edgar RSS feed"),
                                 wraplength=480)
                
        frame.grid(row=0, column=0, sticky=(N,S,E,W))
        frame.columnconfigure(1, weight=1)
        window = self.winfo_toplevel()
        window.columnconfigure(0, weight=1)
        self.geometry("+{0}+{1}".format(dialogX+50,dialogY+100))
        
        self.bind("<Alt-u>", lambda *ignore: urlEntry.focus_set())
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.close)
        
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.grab_set()
        self.wait_window(self)
        
    def ok(self, event=None):
        self.url = self.urlVar.get()
        self.accepted = True
        self.close()
        
    def close(self, event=None):
        self.parent.focus_set()
        self.destroy()
        
    def usSec(self, event=None):
        import webbrowser
        webbrowser.open("http://www.sec.gov/edgar/searchedgar/companysearch.html")

    def rssFeed(self, event=None):
        self.url = "http://www.sec.gov/Archives/edgar/usgaap.rss.xml"
        self.accepted = True
        self.close()
