from app import app
from api.models.staff_model import staff_model
from flask import request

staffModelObj= staff_model()

@app.route("/staff/getalltrainers")
def getalltrainers():
    return staffModelObj.getalltrainers()