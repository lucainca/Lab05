# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection

from model.corso import Corso



class corso_DAO:

    def getCorsi(self):
        corsi = []
        cnx=get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select * from corso """
        cursor.execute(query)

        for row in cursor:

            corsi.append(Corso (row["codins"],row["crediti"],row["nome"],row["pd"]))

        return corsi









if __name__ == '__main__':
    dao = corso_DAO()

    print(dao.getCorsi())

