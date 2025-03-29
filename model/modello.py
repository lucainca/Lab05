from database.corso_DAO import corso_DAO
from database.studente_DAO import studente_DAO


class Model:

    def __init__(self):
        self._DAO= corso_DAO()
        self.DAOs = studente_DAO()

    def getCorsi(self):
        corsi = self._DAO.getCorsi()
        return corsi

    def getIscritti(self,codice):
        iscritti = self.DAOs.getIscritti(codice)
        return iscritti

    def getStudenti(self):
        studenti = self.DAOs.getStudenti()
        return studenti

    def getIscrCorsi(self,matr):
        iscrCorsi = self.DAOs.getIscrCorsi(matr)
        return iscrCorsi




