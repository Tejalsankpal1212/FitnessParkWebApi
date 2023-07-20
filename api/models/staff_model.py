import utils.database as database
from flask import json
from flask import make_response

class staff_model():
    """docstring for department_model."""
    def __init__(self):
        self.conn=database.dbconnection.connect()
        self.conn.autocommit=True
        self.cur=self.conn.cursor(dictionary=True)


    def getalltrainers(self):
        self.cur.callproc('sp_getalltrainers')
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)
