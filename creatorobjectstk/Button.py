import creatorobjectstk
from creatorobjectstk import MAIN_SETTINGS, ANCHOR, ON_WHAT
from .parselogic import parse_int, parse_srt, parse_float
from tkinter import Button, RAISED
from typing import Optional



class CreateButton(creatorobjectstk.CreateObject):
    def parse(self, pr:dict, ud:dict):
        self.colors: list = parse_srt(pr, ud, 'colors', 
                                      'red,green,yellow').split(',')
        self.interaction: str = parse_srt(pr, ud, 
                    'interaction', MAIN_SETTINGS.get('interaction', 'None')) 
        self.on_what: str = parse_srt(pr, ud, 'on_what', 'root')
        self.bg: str = parse_srt(pr, ud, 'bg', 
                                 MAIN_SETTINGS.get('bg', 'gray'))
        self.font: str = parse_srt(pr, ud, 'font', 
                                   MAIN_SETTINGS.get('font', 'Courier 9'))
        self.width: int = parse_int(pr, ud, 'width', 10)
        self.bd: int = parse_int(pr, ud, 'bd', MAIN_SETTINGS.get('bd', 4))
        self.relief: str = parse_srt(pr, ud, 'relief', 'raised')
        self.saved: str = parse_srt(pr, ud, 'saved', 'Name')
        self.text_switch: list = parse_srt(pr, ud, 'text_switch',
                                'STATUS OFF,STATUS ON,UNKNOWN').split(',')
        self.relx: float = parse_float(pr, ud, 'relx', 0.15)
        self.rely: float = parse_float(pr, ud, 'rely', 0.25)
        #command: str = parse_srt(pr, ud, 'command', 'change_color')
        self.command = None
        self.anchor: str = parse_srt(pr, ud, 'anchor', 
                                     MAIN_SETTINGS.get('anchor', 'CENTER'))
        self.active: int = parse_int(pr, ud, 'active', 2)
        self.button:Optional[Button] = None

    def create(self, **kwargs):
        if ON_WHAT.get(self.on_what) is not None:
            if self.button is None:
                active = self.active
                if self.active >= len(self.colors):
                    active = -1
                if kwargs.get('command') is not None:
                    self.command = kwargs.get('command')
                    self.button = Button(
                        ON_WHAT[self.on_what],
                        bg=self.colors[active],
                        text=self.text_switch[active],
                        font=self.font,
                        width=self.width,
                        bd=self.bd,
                        relief=RAISED,
                        command=self.command,
                    )
                    self.button.pack(pady=5)
                    self.button.place(relx=self.relx, rely=self.rely, 
                                      anchor=ANCHOR[self.anchor])
                    if creatorobjectstk.OBJECTS.get('BUTTON') is None:
                        creatorobjectstk.OBJECTS['BUTTON'] = {self.name: self}
                    else: 
                        creatorobjectstk.OBJECTS['BUTTON'][self.name] = self
                    return self.button

    
    def update(self):
        pass
    
    def delete(self):
        pass
