from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from netmiko import Netmiko
import util
import json
from ntc_templates.parse import parse_output
from pythonping import ping
# Init app
app = Flask(__name__)
# Database
# This containst the default config for a local SQLite flat file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysqlitedb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)
# BGP Database Class/Model
#Here is the class to create/use the SQL table/columns, a primary key is edit/replace columns as needed
class TABLE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.String(15))
    mac = db.Column(db.String(14))
    timeadded = db.Column(db.DateTime, default=datetime.utcnow)
    timestamp = db.Column(db.DateTime)
    
    def __repr__(self):
        return '<%r>' % self.id
# BGP Schema for Marshmallow API Functionality
# fields in the schema should match columns in the db
class TABLESchema(ma.Schema):
    class Meta:
        fields = ('id', 'device', 'ip', 'mac', 'timeadded', 'timestamp')
# Init Schema        
TABLE_schema = TABLESchema()
TABLESs_schema = TABLESchema(many=True)

"""
To build/rebuild the db, execute the following after stopping the app, closing the python console and deleting the old .db file:
from app import db
db.create_all()
"""
#App Routes
#The first route is the index route which is required. Best practive is to limit methods to those supported.
# Typical function show with a post method for form, otherise a default listing of all db entries
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        device = request.form['device']
        data = TABLE.query.filter(TABLE.device == device).all()
        return render_template('index.html', data=data)
    else:
        data = TABLE.query.all()
        return render_template('index.html', data=data)

#This route links to the first python action, things to populate your DB or manipulate it's fields
@app.route('/action', methods=['POST', 'GET'])
def action()
    if request.method == 'POST':
        device = request.form['device']
        net_device = util.CiscoDeviceRO(host=device)
        net_connect = Netmiko(**net_device.__dict__)
        # insert python code to extract appropriate data and set varaibles for DB entry
        # example for ip interfaces brief data, adapt as needed and use ntc parsers or custom regex to extract vars
        ip_int_bri = net_connect.send_command("show ip interface brief")
        # ipaddr = 
        # macaddr = 
        # timestamp = 
        # gracefully disconnect from device
        net_connect.disconnect()
        
        new_entry = TABLE(device=device, ip=ipaddr, mac=macaddr, timestamp=now)
        db.session.add(new_entry)
        db.session.commit()
        data = TABLE.query.filter(TABLE.device == device).all()
        return render_template('action.html', data=data) 
    else:       
        return render_template('action.html')        
    
    
 
    


# API Routes
# API Data Post
@app.route('/api/<device>', methods = ['POST'])
def api_function(device):
    data = TABLE.query.filter(TABLE.device == device).all()
    result = TABLESs_schema.dump(arps)
    return jsonify(result) 


if __name__ == "__main__":
    app.run(host='0.0.0.0')
