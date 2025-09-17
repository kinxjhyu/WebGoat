from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ping')
def ping():
    host = request.args.get('host', '127.0.0.1')
    # 취약: 사용자 입력을 쉘에 그대로 전달
    result = os.system("ping -c 1 " + host)
    return f"Result: {result}"

if __name__ == '__main__':
    app.run()

