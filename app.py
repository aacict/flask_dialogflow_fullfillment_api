from flask import Flask, jsonify, request
import json

with open("trending_products.json", "r") as json_file:
    trendingProductsData = json.load(json_file)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def studentInformation():
    student_info = {
        "student_number": "200573774",
        "student_name": "Ashish Thapa",
        "student_email": "aacict@gmail.com",
    }
    return jsonify(student_info)


@app.route("/webhook", methods=["GET", "POST"])
def fullfillmentWebhook():
    if request.method == "GET":
        return "This is fulfullment server, try from chatbot using intent"

    else:
        richContent = []
        trendingProductsData["CO"]
        for trendingProduct in trendingProductsData["CO"]:
            item = {
                    "title": trendingProduct["product-name"],
                    "actionLink": "",
                    "type": "info",
                    "subtitle": "",
                    "image": {
                        "src": {
                            "rawUrl": trendingProduct["product-image-url"]
                        }
                    },
                }

            if item:
                richContent.append(item)
                richContent.append({"type": "divider"})
        intentresp = {
            "fulfillmentMessages": [{"payload": {"richContent": [richContent]}}]
        }
        return jsonify(intentresp)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=8080)
