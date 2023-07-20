import utils.database as database
from flask import json
from flask import make_response

class member_model():
    """docstring for department_model."""
    def __init__(self):
        self.conn=database.dbconnection.connect()
        self.conn.autocommit=True
        self.cur=self.conn.cursor(dictionary=True)


    def getallmembers(self):
        self.cur.callproc('sp_getallmembers')
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No data found"},204)

   
    def getmemberbyid(self,memberId):
        
        self.cur.callproc('sp_getmemberbyid',(memberId,))
        for dbresult in self.cur.stored_results():
            result=dbresult.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:   
            return make_response({"message":"No data found"},204)
    

    def postmember(self,data):
        try:
           
            result=None 
            args = (data["firstname"],data["middlename"],data["lastname"],data["gender"],data["dateofbirth"],data["address"],data["city"],data["state"],data["zipcode"],data["emailid"],data["mobileno"],data["height"],data["weight"],data["chest"],data["waist"],data["arms"],data["thighs"],data["pasttreatment"],data["allergydetails"],data["createdby"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_postmember',(args))      
            result=list(result_args.values())[1]
            print(result)
            if result:  
                return make_response({"message":"Member Created Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)
    
    def postmemberfromapp(self,data):
        try:
            print(data)
            result=None 
            args = (data["firstname"],data["middlename"],data["lastname"],data["dateofbirth"],data["emailid"],data["mobileno"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_postmemberfromapp',(args))      
            result=list(result_args.values())[6]
            print(result)
            if result:  
                return make_response({"payload":result,"message":"Member Created Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)
    
    def putmember(self,data):
        try:
            print(data)
            result=None
            args = (data["memberid"],data["firstname"],data["middlename"],data["lastname"],data["gender"],data["dateofbirth"],data["address"],data["city"],data["state"],data["zipcode"],data["emailid"],data["mobileno"],data["height"],data["weight"],data["chest"],data["waist"],data["arms"],data["thighs"],data["pasttreatment"],data["allergydetails"],data["updatedby"], (0, 'CHAR'))
            result_args =self.cur.callproc('sp_putmember',(args))      
            result=list(result_args.values())[2]
           
            if result:
                return make_response({"message":"Member Updated Successfully"},201)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)

    def deletemember(self,memberid):
        try:
           
            result=None
            args = (memberid, (0, 'CHAR'))
            result_args =self.cur.callproc('sp_deletemember',(args))      
            result=list(result_args.values())[1]
            print(result)
            if result:
                return make_response({"message":"Member Deleted Successfully"},200)
            else:
                return make_response({"message":"No data found"},204)
           
        except Exception as e:
            print(e.args)
            return make_response({"exception":e.args},404)
        
            

