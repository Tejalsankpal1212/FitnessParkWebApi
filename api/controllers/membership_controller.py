from app import app
from api.models.membership_model import membership_model
from flask import request

membershipModelObj= membership_model()

@app.route("/membership/getallmemberships")
def getallmemberships():
    return membershipModelObj.getallmemberships()

@app.route("/membership/getmembershipbyid")
def getmembershipbyid():
    return membershipModelObj.getmembershipbyid(request.form)

@app.route("/membership/postmembership",methods=["post"])
def postmembership():
    print(request.get_json())   
    return membershipModelObj.postmembership(request.get_json())

@app.route("/membership/putmembership",methods=["put"])
def putmembership():      
    return membershipModelObj.putmembership(request.get_json())

@app.route("/membership/deletemembership/<string:membershipid>",methods=["delete"])
def deletemembership(membershipid):      
    return membershipModelObj.deletemembership(membershipid)