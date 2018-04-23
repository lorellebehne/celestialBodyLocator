from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

import json

app = Flask(__name__)
CORS(app)

key = "H6948P-WPKW3GLAKW" 
long = 0.0
@app.route("/search", methods=["GET"])
def findBody():
	print("got date")
	year = request.args["year"]
	month = request.args["month"]
	day = request.args["day"]
	body = request.args["body"]
	date="{}-{}-{}".format(year, month, day)
	res = requests.get("http://api.wolframalpha.com/v2/query?input={}+position+{}&appid={}&format=plaintext&podtitle=Result&formattype=plaintext&assumption=DateOrder_**Year.Month.Day--".format(body,date,key)).text.split("\n")
	#loc = res.split("\n")[4]
	latHMS = []
	change = False
	str = ""
	print(res[24])
	for i in res[24][32:]:
		if i in "-.1234567890":
			str+=i
			change = False
		else:
			if not change:
				latHMS.append(str)
			str = ''
			change = True
	
	#outs : <plaintext>right ascension | 23^h 14^m 53.2^s
	longHMS = []
	change = False
	str = ""
	for i in res[25][14:]:
		if i in "-.1234567890":
			str+=i
			change = False
		else:
			if not change:
				longHMS.append(str)
			str = ''
			change = True
			
	lat = float(latHMS[0])*15+float(latHMS[1])/60+float(latHMS[2])/60/60
	if lat > 180:
		lat = lat -360
	long = float(longHMS[0])+float(longHMS[1])/60+float(longHMS[2])/60/60
	print(lat, long)
	#outs : declination | -3DEGREE SYMBOL 27&apos; 20&quot;</plaintext>
	#return(res[25])
	
	return jsonify(latHMS,longHMS)

if __name__ == '__main__':

	app.run(debug=True, port=5001)
