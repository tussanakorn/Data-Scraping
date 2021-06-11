from flask import Flask,json, jsonify, request
import pandas as pd

api = Flask(__name__)

@api.route('/hello/api1')
def hello():
    return "Hello"

@api.route('/list')
def hello1():
    return jsonify([{'name' : 'film'},{'name1' : 'waen'}])

@api.route('/string')
def hello2():
    return "Hello2"

@api.route('/list')
def hello3():
    return jsonify([1,2,3,4,5])

@api.route('/dict')
def hello4():
    return {
        "Confirmed":3162,
        "Recovered":3040,
        "Hospitalized":64,
        "Deaths":58,
        "NewConfirmed":4,
        "NewRecovered":2,
        "NewHospitalized":2,
        "NewDeaths":0,
        "UpdateDate":"26/06/2020 11:46",
        "Source":"https://covid19.th-stat.com/",
        "DevBy":"https://www.kidkarnmai.com/",
        "SeverBy":"https://smilehost.asia/"
    }


# accept imput parameters
@api.route('/param')
def get_param():
    param1 = request.args.get('param1',default=1, type=int) # requests.args['param1']
    param2 = request.args.get('param2', type=int)
    param3 = request.args.get('param3')
    try:
        param3 = int(param3) 
    except:
        return {'error': 'param3 must be number only'} 

    if param3 == None:
        return {'error':'give me param3'}
    return {'param1':param1, 'param2':param2, 'param3':param3}

@api.route('/add_number')
def add_number():
    num1 = request.args.get('num1', type = int) 
    num2 = request.args.get('num2', type = int) 
    return {'result' : num1 + num2}


# with open('today_data.json', 'r') as f:
#   data = json.load(f)

df = pd.read_json('today_data.json')

# example : serving covid data from file
#@api.route('/api/covid/all')
#def serve_all():
    #result_json = json.loads(df.to_json(date_format='iso', orient='records' ))
   # return jsonify(result_json)

# Example : filter death count
@api.route('/api/covid')
def serve_covid():
    num_death = request.args.get('death', type=int)
    num_recovered = request.args.get('recovered', type=int)
    query = (df['Deaths'] == num_death) & (df['Recovered'] == num_recovered)
    filter_df = df[query]
    result_json = json.loads(filter_df.to_json(date_format='iso', orient='records' ))
    return jsonify(result_json)

if __name__ == "__main__":
    api.run(debug=True)


