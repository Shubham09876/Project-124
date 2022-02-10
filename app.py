from flask import Flask , jsonify , request

app = Flask(__name__)

contacts = [
    {
        "id": 1 ,
        "title": u"6291400028",
        "description": u"My contact",
        "done" : False
    } , 

    { 
        "id" : 2,
        "title" : u"9475885748",
        "description": u"My friend's contact",
        "done" : False
     } , 

     {
      "description": "My brother's contact", 
      "done": False, 
      "id": 3, 
      "title": "6290313805"
    }
]

@app.route('/addContact' , methods=['POST'])

def addContactNumber():

    if not request.json:
        return jsonify({
            "status": "Error",
            "message": "Please enter a contact number"
        } , 400)

    contact = {
        "id" : contacts[ -1 ][ "id" ] + 1,
        "title" : request.json["title"],
        "description" : request.json.get["description"],
        "done" : False
    }

    contacts.append(contact)

    return jsonify({
        "status" : "Success",
        "message" : "Contact added successfully"
    })

@app.route('/getContact')

def getContactNumber():
    return jsonify({
        "data" : contacts 
    })

if( __name__ == '__main__' ):
    app.run(debug = True)