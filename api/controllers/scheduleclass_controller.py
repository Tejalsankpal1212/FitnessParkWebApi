from app import app
from api.models.scheduleclass_model import scheduleclass_model
from flask import request

scheduleclassModelObj= scheduleclass_model()

@app.route("/scheduleclass/getallscheduleclasses")
def getallscheduleclasses():
    return scheduleclassModelObj.getallscheduleclasses()

@app.route("/scheduleclass/getscheduleclassbyid")
def getscheduleclassbyid():
    return scheduleclassModelObj.getscheduleclassbyid(request.form)

@app.route("/scheduleclass/postscheduleclass",methods=["post"])
def postscheduleclass():      
    return scheduleclassModelObj.postscheduleclass(request.get_json())

@app.route("/scheduleclass/putscheduleclass",methods=["put"])
def putscheduleclass():      
    return scheduleclassModelObj.putscheduleclass(request.get_json())

@app.route("/scheduleclass/deletescheduleclass/<string:scheduleclassid>",methods=["delete"])
def deletescheduleclass(scheduleclassid):      
    return scheduleclassModelObj.deletescheduleclass(scheduleclassid)