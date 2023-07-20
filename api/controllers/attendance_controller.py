from app import app
from api.models.attendance_model import attendance_model
from flask import request


attendanceModelobj=attendance_model()

@app.route("/attendance/getallattendance")
def getallattendance():
    return attendanceModelobj.getallattendance()

@app.route("/attendance/gettotalattendance")
def gettotalattendance():
    return attendanceModelobj.gettotalattendance()

@app.route("/attendance/gettodaysattendance")
def gettodaysattendance():   
    return attendanceModelobj.gettodaysattendance()

@app.route("/attendance/gettop5attendance")
def gettop5attendance():   
    return attendanceModelobj.gettop5attendance()

@app.route("/attendance/getattendancebyempid")
def getattendancebyempid():
    return attendanceModelobj.getattendancebyempid

@app.route("/attendance/postattendance",methods=["post"])
def postattendance():
    return attendanceModelobj.postattendance(request.form)