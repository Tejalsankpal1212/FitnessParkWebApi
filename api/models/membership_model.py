import utils.database as database
from flask import json
from flask import make_response

class membership_model():
    """docstring for department_model."""
    def __init__(self):
        self.conn=database.dbconnection.connect()
        self.conn.autocommit=True
        self.cur=self.conn.cursor(dictionary=True)


    def getallmemberships(self):
        self.cur.callproc('sp_getallmemberships')
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)

   
    def getmembershipbyid(self,membershipid):
        self.cur.callproc('sp_getmembershipbyid',membershipid)
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:   
            return make_response({"message":"No data found"},204)


    def postmembership(self,data):
        try:
           
            result=None

            if data["numberofsessions"]=="":
                numerofsessions=0
            else:
                numerofsessions=data["numberofsessions"]
            
            #print("Number Of Sessions are : "+ data["number_of_sessions"])

            args = (data["membershipname"],data["membershiptype"],data["membershipperiod"],
                    data["membershipscope"],numerofsessions,data["membershipamount"],
                    data["membershipclass"],data["createdby"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_postmembership',(args))
            result=list(result_args.values())[8]  
            print(result_args.values())
            if result:
                return make_response({"message":"Membership Created Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)
    
    def putmembership(self,data):
        try:
            print(data)
            result=None
            args = (data["membershipId"],data["membershipname"],data["membershiptype"],data["membershipperiod"],data["membershipscope"],data["numberofsessions"],data["membershipamount"],data["membershipclass"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_putmembership',(args))      
            result=list(result_args.values())[2]
           
            if result:
                return make_response({"message":"Membership Updated Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)

    def deletemembership(self,membershipid):
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
        
            

