import logging

import azure.functions as func
from flask import Flask , redirect

app = Flask(__name__) 



#code for Azure function
def main(req: func.HttpRequest,context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.WsgiMiddleware(app.wsgi_app).handle(req,context)


#code for flask application

@app.route("/")

def index():
    logging.info("Flask app about to redirect")
    return redirect("https://portal.azure.com",code = 301)