# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from database.corso_DAO import corso_DAO
from model.corso import Corso
from model.studente import Studente
from database.corso_DAO import corso_DAO


class studente_DAO:
    def __init__(self):

        self.daoC = corso_DAO()
    def getStudenti(self):
        studenti = []
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select * from studente """
        cursor.execute(query)

        for row in cursor:
            studenti.append(Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"]))
        return studenti


    def getIscritti(self, codice):
        iscritti = []
        studIscritti = []
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select * from iscrizione i where codins=%s """

        cursor.execute(query, (codice,))
        for isc in cursor:
            iscritti.append(isc)

        for row in iscritti:
            for stud in self.getStudenti():
                if stud.matricola == row["matricola"]:
                    studIscritti.append(stud)
        return studIscritti


    def getIscrCorsi(self,matricola):
        iscr = []
        iscrCorsi = []

        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select * from iscrizione i where matricola=%s """
        cursor.execute(query, (matricola,))
        for cors in cursor:
            iscr.append(cors)

        for i in iscr:
            for c in self.daoC.getCorsi():
                if i["codins"] == c.codins:
                    iscrCorsi.append(c)

        print(iscr)
        return iscrCorsi



if __name__ == "__main__":
    dao= corso_DAO()
    dao1 = studente_DAO()
   # dao1.getIscritti("01NBAPG")

if __name__ == '__main__':
    dao = studente_DAO()
    print(dao.getIscrCorsi(197220))
   # print(dao.getStudenti())

if __name__ == '__main__':
    dao = studente_DAO()
    print(dao.getStudenti())

