from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def is_prima(number):
    if number <=1:
        return False
    if number <=3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ganjil', methods=['POST'])
def ganjil():
    data = request.get_json()
    number = int(data['number'])
    ganjil = [i for i in range(1, number +1, 2)]
    return jsonify(result=', '.join(map(str, ganjil)))

@app.route('/prima', methods=['POST'])
def prima():
    data = request.get_json()
    number = int(data['number'])
    if number < 2:
        return jsonify({"error": "Masukkan lebih dari 1"})
    primes = [number for number in range(2, number + 1) if is_prima(number)]
    return jsonify(result=', '.join(map(str, primes)))    

@app.route('/segitiga', methods=['POST'])
def segitiga():
    data = request.get_json()
    number = data['number']
    result = []
    multiply = 1
    
    for i in number:
        result.append(i + '0' * multiply)
        multiply +=1
    
    return jsonify(result='<br>'.join(result))

if __name__ == '__main__':
    app.run(debug=True)