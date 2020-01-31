"""
Simple web-server for the indeed map website.
"""
import http.server
import socketserver
import os

from flask import Flask, render_template, request, make_response, json

from back.jsonifyDataframe import createJsonFromDataframe
from back.indeedDataAnalyzer import analyzeIndeedData
from back.indeedScraper import scrapeIndeed

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    
    
@app.route('/', methods=['POST'])
def indexPOST():
   searchRequest = request.form['jobname']
   print("received post in server route /")
   print(searchRequest)
   
   indeedData = scrapeIndeed(searchRequest)
   #pass output from scrapeIndeed into the data analyzer to calculate mean, std, etc..
   indeedDataframe = analyzeIndeedData(indeedData)
   #Create the json to send back to the client from the dataframe with analyzed indeed data
   jsonToSend = createJsonFromDataframe(indeedDataframe)
    
   
   print(jsonToSend)
   print(type(jsonToSend))
    
   return jsonToSend
    
    
@app.route('/about', methods=['GET'])
def about():
    return 'about page'
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
