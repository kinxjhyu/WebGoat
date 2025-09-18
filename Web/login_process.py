from flask import Flask, request
import pymysql

app = Flask(__name__)

# MySQL 연결 정보
DB_HOST = "localhost"
DB_USER = "root"        # MySQL 사용자 이름
DB_PASSWORD = "1212"    # MySQL 비밀번호
DB_NAME = "user_db"     # 사용할 데이터베이스

@app.route('/login', methods=['POST'])
def login():
    # 클라이언트에서 전달된 데이터
    username = request.form.get('username')
    password = request.form.get('password')

    # MySQL 연결
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8mb4'
    )
    cursor = conn.cursor()

    # SQL 쿼리를 직접 문자열로 생성 (SQL Injection 방지 안 함)
    sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(sql)
    result = cursor.fetchall()

    # 로그인 성공 여부 확인
    if len(result) > 0:
        return "로그인 성공!"
    else:
        return "사용자명 또는 비밀번호가 잘못되었습니다."

    # 연결 종료
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
