import unittest
import os
import sys
sys.path.append(os.getcwd())
from creatorobjectstk.Window import CreateWindow
from creatorobjectstk.Button import CreateButton
from tkinter import Tk


class TestObjects(unittest.TestCase):
    def setUp(self):
        self.pr= {
                "WINDOW" : { "WIN_1": {
                    'title': 'New Window',
                    'height': 150},
                    },
                "BUTTON" : {"BUT_1": {
                    'interaction': 'WIN_1',
                    'name': 'Press',
                    },
                            }
                }
        self.ud = {}
        self.window = self.pr.get('WINDOW')
        self.name_window = 'WIN_1'
        if self.window is None:
            return
        self.pr_window = self.window.get(self.name_window)
        self.button = self.pr.get('BUTTON')
        self.name_button = 'BUT_1'
        if self.button is None:
            return
        self.pr_button = self.button.get(self.name_button)

    def test_created_window(self):
        self.created_window = CreateWindow(name=self.name_window, test=True) 
        if self.pr_window is None:
            return
        self.created_window.parse(self.pr_window, self.ud)
        self.created_window.update(title='None')
        self.assertEqual(self.created_window.title, 'None')
        self.created_window.title='New title'
        self.assertEqual(self.created_window.title, 'New title')
        sl = self.created_window.create()
        self.assertTrue(self.created_window.action)
        self.assertEqual(type(sl), Tk)

    def test_created_button(self):
        self.created_window.create()
        self.created_button = CreateButton(self.name_button)
        if self.pr_button is None:
            return
        self.created_button.parse(self.pr_button, self.ud)





if __name__ == '__main__':
    unittest.main()
