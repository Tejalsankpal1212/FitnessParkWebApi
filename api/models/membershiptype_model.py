import utils.database as database
from flask import json
from flask import make_response

class membershiptype_model():
    """docstring for department_model."""
    def __init__(self):
        self.conn=database.dbconnection.connect()
        self.conn.autocommit=True
        self.cur=self.conn.cursor(dictionary=True)


    def getallmembershiptypes(self):
        self.cur.callproc('sp_getallmembership_categories')
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)

   
    def getmembershiptypebyid(self,membershipid):
        self.cur.callproc('sp_getmembershipbyid',membershipid)
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:   
            return make_response({"message":"No data found"},204)


    def postmembershiptype(self,data):
        try:
           
            result=None
            args = (data["membershiptypename"],data["createdby"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_postmembership_categories',(args))      
            result=list(result_args.values())[1]
            print(result)
            if result:
                return make_response({"message":"Membership Type Created Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)
    
    def putmembershiptype(self,data):
        try:
            print(data)
            result=None
            args = (data["membershiptypeid"],data["membershiptypename"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_putmembership',(args))      
            result=list(result_args.values())[2]
           
            if result:
                return make_response({"message":"Membership Type Updated Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)

    def deletemembershiptype(self,membershipid):
        try:
           
            result=None
            args = (membershipid, (0, 'CHAR'))
            result_args =self.cur.callproc('sp_deletemembership',(args))      
            result=list(result_args.values())[1]
            print(result)
            if result:
                return make_response({"message":"Membership Deleted Successfully"},200)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)
        
            

