from app import app
from api.models.member_model import member_model
from flask import request

memberModelObj= member_model()

@app.route("/member/getallmembers")
def getallmembers():
    return memberModelObj.getallmembers()

@app.route("/member/getmemberbyid/<string:memberid>")
def getmemberbyid(memberid):
    print(memberid)
    return memberModelObj.getmemberbyid(memberid)

@app.route("/member/postmember",methods=["post"])
def postmember():      
    return memberModelObj.postmember(request.get_json())

@app.route("/member/postmemberfromapp",methods=["post"])
def postmemberfromapp():      
    return memberModelObj.postmemberfromapp(request.get_json())

@app.route("/member/putmember",methods=["put"])
def putmember():      
    return memberModelObj.putmember(request.get_json())

@app.route("/member/deletemember/<string:memberid>",methods=["delete"])
def deletemember(memberid):      
    return memberModelObj.deletemember(memberid)