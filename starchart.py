from flask import Flask, request

import requests as requests #may need to pip install requests

import json

app = Flask(__name__)

key = "H6948P-WPKW3GLAKW" 

@app.route("/search/<string:body>/<string:day>/<string:month>/<string:year>", methods=["GET"])
def findBody(body,day, month,year):
	print("got date")
	date="{}-{}-{}".format(year, month, day)
	st = format(body,date)
	try:
		res = request.get("http://api.wolframalpha.com/v2/query?input={}+position+{}&appid={}&format=plaintext&podtitle=Result&formattype=plaintext&assumption=DateOrder_**Year.Month.Day--".format(body,date,key))
		loc = res.split("\n")[4]
		print(loc)
		return jsonify(loc)
	except:
		console.log("it is not a da working")
		
	

 

if __name__ == '__main__':

	app.run(debug=True, port=5001)
