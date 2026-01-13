from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage
items = []

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()

    item = {
        "id": len(items) + 1,
        "name": data.get("name")
    }

    items.append(item)
    return jsonify(item), 201

if __name__ == "__main__":
    app.run(debug=True)
