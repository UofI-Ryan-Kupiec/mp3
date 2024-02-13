from flask import Flask, request
app = Flask(__name__)
seed_value = 0

@app.route('/',methods = ['POST', 'GET'])
def seed():
    global seed_value
    
    if request.method == 'POST':
      seed_req = request.get_json()
      seed_value = seed_req.get("num", seed_value)
      return "Seed updated!"
    else:
      return str(seed_value)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)