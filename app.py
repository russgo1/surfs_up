# dependencies
import datetime as dt
import numpy as np
import pandas as pd
# sqalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Flask
from flask import Flask, jsonify

# Set up the Database 9.5.1
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create session link
session = Session(engine)

# Set up Flask application

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'