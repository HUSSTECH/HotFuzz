
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)
app.debug = True

# List of UK Gov Ministries
ministries = ['Prime Ministers Office, 10 Downing Street',
'Deputy Prime Ministers Office',
'Attorney Generals Office',
'Cabinet Office',
'Department for Business, Innovation & Skills',
'Department for Communities and Local Government',
'Department for Culture, Media & Sport',
'Department for Education',
'Department for Environment, Food & Rural Affairs',
'Department for International Development',
'Department for Transport',
'Department for Work and Pensions',
'Department of Energy & Climate Change',
'Department of Health',
'Foreign & Commonwealth Office',
'HM Treasury',
'Home Office',
'Ministry of Defence',
'Ministry of Justice',
'Northern Ireland Office',
'Office of the Advocate General for Scotland',
'Office of the Leader of the House of Commons',
'Office of the Leader of the House of Lords',
'Scotland Office',
'UK Export Finance',
'Wales Office']

@app.route('/')
def index():
	return render_template('index.html', title='HotFuzz')

@app.route('/outputList')
def outputList():
	query = request.query_string[12:]
	print(query)

	matched = [string for string in ministries if re.search(".*?".join(query),string,flags=re.IGNORECASE)]

	return jsonify(ministries=matched)
