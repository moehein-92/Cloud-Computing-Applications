from flask import Flask, request
import json

app = Flask(__name__)

seed = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    global seed
    
    if request.method == 'GET':
        return str(seed)
    
    elif request.method == 'POST':
        seed = json.loads(request.data)['num']
        return "Post successful."

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
