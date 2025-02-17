from flask import Flask,request,jsonify
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()
MONGO_URI=os.getenv('MONGO_URI')
client=pymongo.MongoClient(MONGO_URI)
db=client.test
collection=db['flask-tutorial']

app=Flask(__name__)

@app.route('/submit',methods=['POST'])
def submit():
    try:
       form_data=dict(request.json)
       collection.insert_one(form_data)
       return 'Data Submitted successfully'
    except:
        return 'Something went wrong'
@app.route('/view')
def view():
    data=collection.find()
    data=list(data)

    for item in data:
        print(item)
        del  item['_id']
    data={
        'data':data
    }

    return jsonify(data)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000,debug=True)
