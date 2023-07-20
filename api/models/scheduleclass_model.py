import utils.database as database
from flask import json
from flask import make_response

class scheduleclass_model():
    """docstring for department_model."""
    def __init__(self):
        self.conn=database.dbconnection.connect()
        self.conn.autocommit=True
        self.cur=self.conn.cursor(dictionary=True)


    def getallscheduleclasses(self):
        self.cur.callproc('sp_getallclasses')
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)

   
    def getscheduleclassbyid(self,classId):
        self.cur.callproc('sp_getclassbyid',classId)
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:   
            return make_response({"message":"No data found"},204)


    def postscheduleclass(self,data):
        try:
           
            result=None
            args = (data["classname"],data["trainer"],data["location"],data["startdate"],data["enddate"],data["bookingfee"],data["classdays"],data["starttime"],data["endtime"],data["createdby"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_postclass',(args))      
            result=list(result_args.values())[1]
            print(result)
            if result:
                return make_response({"message":"Class Scheduled Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)   
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)
    
    def putscheduleclass(self,data):
        try:

            result=None
            args = (data["classid"],data["classname"],data["trainer"],data["location"],data["bookingfee"],data["classdays"],data["starttime"],data["endtime"],data["updatedby"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_putclass',(args))      
            result=list(result_args.values())[2]
           
            if result:
                return make_response({"message":"Class Updated Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)

    def deletescheduleclass(self,deptid):
        try:
           
            result=None
            args = (deptid, (0, 'CHAR'))
            result_args =self.cur.callproc('sp_deletescheduleclass',(args))      
            result=list(result_args.values())[1]
            print(result)
            if result:
                return make_response({"message":"Class Deleted Successfully"},200)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)
        
            

