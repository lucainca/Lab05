import flet as ft

from model import modello
from model.modello import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_cercaIscritti(self, e):

        corso = self._view._txtCorso.value
        if corso is None or corso == "":
            self._view.create_alert("Selezionare un corso!")
            return
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Codice insegnamento: {corso}"))
        self._view.update_page()


        self._view.txt_result.controls.append(ft.Text(f"Gli iscritti sono: {len(self.getIscritti(corso))}\n "))
        for i in self.getIscritti(corso):
            self._view.txt_result.controls.append(ft.Text(f" {i}" ))

        self._view.txt_result.controls.append(ft.Text(f"--------------"))
        self._view.update_page()


    def handle_cercaStudenti(self,e):

        matricola = self._view._txtMatricola.value

        if matricola is None or matricola == "":
            self._view.create_alert("Selezionare una matricola!")
            return

        corso = self._view._txtCorso.value

        find =0
        for iscr in self.getIscritti(corso):
            if iscr.matricola==int(matricola):
                self._view._txtNome.value = iscr.nome
                self._view._txtCognome.value = iscr.cognome
                find+=1

        if find==0:
            self._view._txtNome.value = ""
            self._view._txtCognome.value = ""
            self._view.create_alert("Matricola non trovata!")
        self._view.update_page()



    def handle_cercaCorsi(self,e):
        matricola = self._view._txtMatricola.value
        cnt=0

        if matricola is None or matricola == "":
            self._view.create_alert("Selezionare una matricola!")
            return
        self._view.txt_result.controls.clear()

        for iscr in self.getStudenti():
            if iscr.matricola == int(matricola):
                self._view._txtNome.value = iscr.nome
                self._view._txtCognome.value = iscr.cognome
                cnt+=1
                self._view.txt_result.controls.append(
                    ft.Text(f"Lo studente è iscritto a {len(self.getIscrCorsi(int(matricola)))} corsi: \n"))

                for b in self.getIscrCorsi(matricola):
                    self._view.txt_result.controls.append(ft.Text(b))
        if cnt == 0:
            self._view._txtNome.value = ""
            self._view._txtCognome.value = ""
            self._view.create_alert("Matricola non trovata!")
        self._view.update_page()










    def getCorsi(self):
        return self._model.getCorsi()

    def getIscritti(self,codice):
        return self._model.getIscritti(codice)

    def getStudenti(self):
        return self._model.getStudenti()

    def getIscrCorsi(self,matr):
        return self._model.getIscrCorsi(matr)