<?php
// login_process.php

$servername = "localhost";
$username = "root"; // MySQL 사용자 이름
$password = "Zmffkdnem123"; // MySQL 비밀번호
$dbname = "user_db"; // 사용할 데이터베이스

// MySQL 연결
$conn = new mysqli($servername, $username, $password, $dbname);

// 연결 체크
if ($conn->connect_error) {
    die("연결 실패: " . $conn->connect_error);
}

// 로그인 정보 받기
$user = $_POST['username'];
$pass = $_POST['password'];

// SQL 쿼리 준비
$sql = "SELECT * FROM users WHERE username = ? AND password = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $user, $pass); // s는 문자열을 의미
$stmt->execute();
$result = $stmt->get_result();

// 로그인 성공 여부 확인
if ($result->num_rows > 0) {
    echo "로그인 성공!";
} else {
    echo "사용자명 또는 비밀번호가 잘못되었습니다.";
}

// 연결 종료
$stmt->close();
$conn->close();
?>
