from flask import Flask, jsonify
import os

app = Flask(__name__)

count_file = '/app/count.txt'
if not os.path.exists(count_file):
    with open(count_file,'w') as file:
        file.write('0')
@app.route('/increment', methods=['POST'])
def increment():
    # Read current count
    with open(count_file, 'r') as file:
        count = int(file.read())

    # Increment the count
    count += 1

    # Save the updated count
    with open(count_file, 'w')as file:
        file.write(str(count))

    return jsonify(count=count)

@app.route('/count', methods=['GET'])
def get_count():
    with open(count_file, 'r') as file:
        count = int(file.read())
    return jsonify(count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)   