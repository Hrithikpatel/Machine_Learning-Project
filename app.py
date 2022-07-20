
from flask import Flask
from housing.logger import logging
from housing.exception import housing_exception
import sys

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing=housing_exception(e,sys)
        logging.info(housing.error_message)
        logging.info("Testing Logging Module")
    return "CI CD Pipeline has been eastablish"


if __name__=="__main__":
    app.run(debug=True)
