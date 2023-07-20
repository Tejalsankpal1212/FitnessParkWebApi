#! C:\Users\Swapnil\AppData\Local\Programs\Python\Python311

from flask import Flask,jsonify
from flask_cors import CORS

app=Flask(__name__)
cors=CORS(app)


if __name__=='__main__':
    app.run(debug=True,port=8001)


import api.controllers.attendance_controller as attendance_controller
import api.controllers.scheduleclass_controller as scheduleclass_controller
import api.controllers.member_controller as member_controller
import api.controllers.membership_controller as membership_controller
import api.controllers.membershiptype_controller as membershiptype_controller
import api.controllers.payment_controller as payment_controller
import api.controllers.staff_controller as staff_controller