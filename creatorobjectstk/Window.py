import creatorobjectstk
from creatorobjectstk import ON_WHAT
from .parselogic import parse_srt, parse_int
from tkinter import Tk
from typing import Optional



class CreateWindow(creatorobjectstk.CreateObject):
    def parse(self, pr:dict, ud:dict):
        self.interaction: str = parse_srt(pr, ud, 'interaction', 'None') 
        self.on_what: str = parse_srt(pr, ud, 'on_what', 'root')
        self.title: str = parse_srt(pr, ud, 'title', 'Empty')
        self.height: int = parse_int(pr, ud, 'height', 100)
        self.width: int = parse_int(pr, ud, 'width', 100)
        self.action: bool = bool(parse_int(pr, ud, 'action', False))
        self.x: int = parse_int(pr, ud, 'relx', 10)
        self.y: int = parse_int(pr, ud, 'rely', 10)
        self.bg: str = parse_srt(pr, ud, 'bg', 'gray')
        self.window:Optional[Tk] = Tk()
        self.window.title(self.title)
        self.window.geometry(f'{self.height}x{self.width}')
        self.window['bg'] = self.bg
        self.window.protocol('WM_DELETE_WINDOW', self._destroy)
        self.action = True
        ON_WHAT[self.name] = self.window
        if creatorobjectstk.OBJECTS.get('WINDOW') is None:
            creatorobjectstk.OBJECTS['WINDOW'] = {self.name: self}
        else:
            creatorobjectstk.OBJECTS['WINDOW'][self.name] = self

    def create(self):
        if not self.test:
            if self.window is not None:
                self.window.mainloop()
        return self.window

    def update(self, **kwargs):
        for parametr, change in kwargs.items():
            if change is not None:
                match parametr:
                    case 'title': 
                        self.title = change
                        if self.window is not None:
                            self.window.title(self.title)
                    case 'interaction':
                        self.interaction = change 
                    case 'on_what':
                        self.on_what = change
                    case 'height':
                        self.height = change
                        if self.window is not None:
                            self.window.geometry(f'{self.height}x{self.width}')
                    case 'width':
                        self.width = change
                        if self.window is not None:
                            self.window.geometry(f'{self.height}x{self.width}')
                    case 'action':
                        self.action = change
                    case 'x':
                        self.x = change 
                    case 'y':
                        self.y = change
                    case 'bg':
                        self.bg = change
                    case _:
                        raise ValueError

    def _destroy(self):
        if self.window is not None:
            ON_WHAT[self.name] = None
            self.window.destroy()
            self.window = None
        





        


