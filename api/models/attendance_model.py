import utils.database as database
from flask import json
from flask import make_response

class attendance_model():
    """docstring for attendance_model."""
    def __init__(self):
        self.conn=database.dbconnection.connect()
        #self.conn.autocommit=True
        self.cur=self.conn.cursor(dictionary=True)


    def getallattendance(self):
        #self.cur.execute("SELECT att_id, emp_id,DATE_FORMAT(date, '%Y-%m-%d') , duration, DATE_FORMAT(time, '%h:%i') FROM tblattendance")
        self.cur.callproc('sp_getallattendance')
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)
        
    def gettop5attendance(self):
        #self.cur.execute("SELECT att_id, emp_id,DATE_FORMAT(date, '%Y-%m-%d') , duration, DATE_FORMAT(time, '%h:%i') FROM tblattendance")
        self.cur.callproc('sp_gettop5attendance')
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)
        
    def gettotalattendance(self):
        #self.cur.execute("SELECT att_id, emp_id,DATE_FORMAT(date, '%Y-%m-%d') , duration, DATE_FORMAT(time, '%h:%i') FROM tblattendance")
        self.cur.callproc('sp_gettotalattendance')
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)
        
    def gettodaysattendance(self):
        #self.cur.execute("SELECT att_id, emp_id,DATE_FORMAT(date, '%Y-%m-%d') , duration, DATE_FORMAT(time, '%h:%i') FROM tblattendance")
        self.cur.callproc('sp_gettodaysattendance')
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)

   
    def getattendancebyid(self,attId):
        self.cur.callproc('sp_getattendancebyid',attId)
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)


    def postattendance(self,data):
        try:
            result=None
            print(data['empid'])
            args = (data['empid'], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_postattendance',(args))      
            result=list(result_args.values())[1]
            print(result)
            if result=='1':
                return make_response({"message":"Attendance Marked Successfully"},201)
            elif result=='2':
                return make_response({"message":"Attendance Already Marked"},201)
            else:
                return make_response({"message":"No data found"},204)
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)            
        