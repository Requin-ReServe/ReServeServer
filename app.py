from flask import Flask, request

app = Flask("ASDFADFWFFWEFWEf")

@app.route('/')
def asdfasdf():
    try:
        print('Hello')
        data = request.json['seok']
    except:
        data = 'Null'

    return {
        "Data is ":data
    }, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)