from abc import abstractmethod
from tkinter import CENTER, BOTH
#from .classes import (
#    _Checkbutton, 
#    _Combobox,
#    _Entry,
#    _ImgButton,
#    _Label,
#    _LabelFrame,
#    _Notebook,
#    _Window,
#    _Device,
#    )

#from . import (
#    Window,
#    Button,
#)


def check_object(type_, object_) -> bool:
    if not type_ == object_:
        return False
    return True

MAIN_SETTINGS = dict()

ANCHOR = {
    'CENTER': CENTER,
}

FILL = {
    'BOTH': BOTH,
}

STATE = {
    'DISABLED': 'readonly',
    'NORMAL': 'normal',
    'READONLY': 'readonly',
}

ON_WHAT = dict()


OBJECTS = {
    'BUTTONS': {},
}

class CreateObject:
    def __init__(self, name:str, **kwargs) -> None:
        self.name = name
        match kwargs.get('test'):
            case True: self.test = True
            case _: self.test = False
    
    @abstractmethod
    def parse(self):
        pass
    
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass
