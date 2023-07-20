from app import app
from api.models.payment_model import payment_model
from flask import request


paymentModelobj=payment_model()

@app.route("/payment/getallpayments")
def getallpayments():
    return paymentModelobj.getallpayments()

@app.route("/payment/getpaymentbyid")
def getpaymentbyid():
    return paymentModelobj.getpaymentbyid(request.form)

@app.route("/payment/getpaymentsbymemberid")
def getpaymentsbymemberid():
    return paymentModelobj.getpaymentsbymemberid(request.form)

@app.route("/payment/postpayment",methods=["post"])
def postpayment():      
    return paymentModelobj.postpayment(request.get_json())

@app.route("/payment/putpayment",methods=["put"])
def putpayment():      
    return paymentModelobj.putpayment(request.get_json())

@app.route("/payment/deletepayment/<string:paymentid>",methods=["delete"])
def deletepayment(paymentid):      
    return paymentModelobj.deletepayment(paymentid)