from flask import Flask, jsonify, request

app = Flask(__name__)

next_id=4

sample_list = [
    {"item_id": 1, "name": "Microcontroller", "stock": 15},
    {"item_id": 2, "name": "Potentiometer", "stock": 42},
    {"item_id": 3, "name": "Servo Motor", "stock": 8}
]



@app.route("/hello")
def hello():
    message = {
        "message": "Welcome to the Electronic Inventory API",
         "status": "active"
    }
    return jsonify(message), 200
@app.route("/data", methods=['GET','POST'])
def data():
    global next_id

    if request.method == 'POST':

        content = request.get_json()

        newItem = {"ID": next_id, "name":content['name'], "stock":content['stock']}

        sample_list.append(newItem)
        next_id=next_id+1

        return jsonify(newItem),201

    return jsonify(sample_list), 200

if __name__ == '__main__':
    app.run(debug=True)