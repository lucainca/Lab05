from msilib.schema import ListView

import flet as ft
import model.corso
import model.modello

from UI.controller import Controller
from model import modello


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_name = ft.TextField(
            label="name",
            width=200,
            hint_text="Insert a your name"
        )



        self._txtCorso = ft.Dropdown(label= "corso",
                                     options = [ft.dropdown.Option(key=corso.codins, text= corso.__str__())
                                                for corso in self._controller.getCorsi() ],
                                     width=500 )

        self._txtMatricola= ft.TextField(
            label="Matricola",
            width=200
        )

        self._txtNome= ft.TextField(
            label="Nome",
            read_only=True,
            width=400
        )

        self._txtCognome= ft.TextField(
            label="Cognome",
            read_only=True,
            width=400
        )

        self.btnCercaIscr = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_cercaIscritti)

        self.btnCercaSt = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_cercaStudenti)

        self.btnCercaC = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_cercaCorsi )

        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi")

        #self._lv= ListView(expand=True)

        row1 = ft.Row([self._txtCorso, self.btnCercaIscr],
                      alignment=ft.MainAxisAlignment.CENTER)

        row2= ft.Row([self._txtMatricola, self._txtNome,self._txtCognome],
                     alignment=ft.MainAxisAlignment.CENTER)

        row3= ft.Row([self.btnCercaSt, self.btnCercaC, self.btnIscrivi],alignment=ft.MainAxisAlignment.CENTER)

       # row4= ft.Row(self._lv)

        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)
       # self._page.controls.append(row4)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()


    #def fillDropDown(self):

      #  for c in provaMod.getCorsi():

