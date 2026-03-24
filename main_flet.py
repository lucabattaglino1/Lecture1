import flet as ft

from UI.controller import Controller
from UI.view import View

def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.set_controller(c) #qui si riconoscono view e controller
    v.carica_interfaccia() # carica gli oggetti grafici nella finestra

ft.app(target = main)