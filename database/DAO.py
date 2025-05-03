from database.DB_connect import DBConnect
from model.Aereoporto import Aereoporto
from model.Voli import Voli


class DAO():
    @staticmethod
    def getAllAereoporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)

        for row in cursor:
            result.append(Aereoporto(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """Select *
                        FROM flights f
                        """
        cursor.execute(query)

        for row in cursor:
            result.append(Voli(**row))
        cursor.close()
        conn.close()
        return result