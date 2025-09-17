<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $targetDir = '/var/www/uploads/';
    $filename = $_FILES['file']['name']; // 취약: 원본 파일명 그대로 사용
    move_uploaded_file($_FILES['file']['tmp_name'], $targetDir . $filename);
    echo "Uploaded";
}
?>

