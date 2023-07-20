import utils.database as database
from flask import json
from flask import make_response

class payment_model():
    """docstring for department_model."""
    def __init__(self):
        self.conn=database.dbconnection.connect()
        self.conn.autocommit=True
        self.cur=self.conn.cursor(dictionary=True)


    def getallpayments(self):
        self.cur.callproc('sp_getallpayments')
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)

   
    def getpaymentbyid(self,paymentid):
        self.cur.callproc('sp_getpaymentbyid',paymentid)
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:   
            return make_response({"message":"No data found"},204)


    def getpaymentsbymemberid(self,memberId):
        self.cur.callproc('sp_getpaymentsbymemberid',memberId)
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:   
            return make_response({"message":"No data found"},204)


    def postpayment(self,data):
        try:
           
            result=None
            args = (data["deptname"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_postpayment',(args))      
            result=list(result_args.values())[1]
            print(result)
            if result:
                return make_response({"message":"Payment Created Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)
    
    def putpayment(self,data):
        try:
            print(data)
            result=None
            args = (data["memberid"],data["membername"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_putpayment',(args))      
            result=list(result_args.values())[2]
           
            if result:
                return make_response({"message":"Payment Updated Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)

    def deletepayment(self,paymentid):
        try:
           
            result=None
            args = (paymentid, (0, 'CHAR'))
            result_args =self.cur.callproc('sp_deletepayment',(args))      
            result=list(result_args.values())[1]
            print(result)
            if result:
                return make_response({"message":"Member Deleted Successfully"},200)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)
        
            

