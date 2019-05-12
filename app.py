# imported class Flask from package flask
# jsonify is a method, not a class
from flask import Flask, jsonify, request, render_template

# create an app using "Flask" 

# __name__ is a python variable which gives each file a unique name
app = Flask(__name__)

# what requests our app is going to understand
# we will use decorators for same
# @app

stores = [
    {
        "name" : "My Wonderful Store",
        "items" : 
        
        [
            {
             "name" : "My Item",
             "price" : 15.99
            }

        ]
    }
]

# here, our api will call this endpoint - "/store"
# browser by default only do "GET" requests
# we need to pass method as POST

@app.route("/")
def home():
    return render_template("index.html")

# POST/store data: {name:}
@app.route("/store" , methods = ["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name" : request_data["name"],
        "items" : []   
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET/ store/<string:name>
@app.route("/store/<string:name>")   # "http://127.0.0.1:5000/store/some_name"
def get_store(name):
    # iterate over stores
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message" : "store not found"} )




# GET/ store/    (will be getting list of all items in store)
@app.route("/store")   
def get_stores():
    # we want to return multiple stores, so we make it a dictionary of stores
    return jsonify({"stores" : stores }) 

# POST/store/<string : name>/item{name : price}
@app.route("/store/<string:name>/item" , methods = ["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name" : request_data["name"],
                "price" : request_data["price"]
            }

            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message" : "store not found"})






# GET/ store/<string:name>/item
@app.route("/store/<string:name>/item")   # "http://127.0.0.1:5000/store/some_name"
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items" : store["items"]})
    return jsonify({"message" : "store not found" })

    

app.run(port = 5000, debug=True)
