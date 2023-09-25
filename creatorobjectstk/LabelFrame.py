import creatorobjectstk
from creatorobjectstk import ON_WHAT
from .parselogic import parse_int, parse_srt, parse_float
from tkinter import LabelFrame
from typing import Optional


class CreateLabelFrame(creatorobjectstk.CreateObject):
    def parse(self, pr:dict, ud:dict):
        self.on_what = parse_srt(pr, ud, 'on_what', 'root')
        self.interaction: str = parse_srt(pr, ud, 'interaction', 'None') 
        self.text = parse_srt(pr, ud, 'text', 'Empty')
        self.height: int = parse_int(pr, ud, 'height', 10)
        self.width: int = parse_int(pr, ud, 'width', 10)
        self.relx: float = parse_float(pr, ud, 'relx', 0.10)
        self.rely: float = parse_float(pr, ud, 'rely', 0.10)
        self.bg: str = parse_srt(pr, ud, 'bg', 'gray')
        self.labelframe:Optional[LabelFrame] = None

    def create(self):
        if ON_WHAT.get(self.on_what) is not None:
            if self.labelframe is None:
                self.labelframe = LabelFrame(
                                            ON_WHAT[self.on_what],
                                            text=self.text,
                                            height=self.height,
                                            width=self.width,
                                            bg=self.bg
                                        )
                ON_WHAT[self.name] = self.labelframe
                self.labelframe.pack(fill='both', expand=1)
                self.labelframe.place(relx=self.relx, rely=self.rely)

    def update(self):
        pass

    def delete(self):
        pass
