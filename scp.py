from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    url = data['url']

    # SQLMap কমান্ড রান করুন এবং আউটপুট সংগ্রহ করুন
    result = subprocess.run(['python3', 'sqlmap/sqlmap.py', '-u', url, '--batch'], capture_output=True, text=True)

    return jsonify({'result': result.stdout})

if __name__ == '__main__':
    app.run(debug=True)
  
