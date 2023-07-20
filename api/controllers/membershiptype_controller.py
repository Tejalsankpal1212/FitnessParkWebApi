from app import app
from api.models.membershiptype_model import membershiptype_model
from flask import request

membershiptypeModelObj= membershiptype_model()

@app.route("/membershiptype/getallmembershiptypes")
def getallmembershiptypes():
    return membershiptypeModelObj.getallmembershiptypes()

@app.route("/membershiptype/getmembershiptypebyid")
def getmembershiptypebyid():
    return membershiptypeModelObj.getmembershiptypebyid(request.form)

@app.route("/membershiptype/postmembershiptype",methods=["post"])
def postmembershiptype():      
    return membershiptypeModelObj.postmembershiptype(request.get_json())

@app.route("/membershiptype/putmembershiptype",methods=["put"])
def putmembershiptype():      
    return membershiptypeModelObj.putmembershiptype(request.get_json())

@app.route("/membershiptype/deletemembershiptype/<string:membershiptypeid>",methods=["delete"])
def deletemembershiptype(membershiptypeid):      
    return membershiptypeModelObj.deletemembership(membershiptypeid)