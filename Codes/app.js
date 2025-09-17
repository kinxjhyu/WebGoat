const express = require('express');
const app = express();

app.get('/greet', (req, res) => {
  const name = req.query.name || 'guest';
  // 취약: 사용자 입력을 HTML에 직접 삽입함
  res.send(`<html><body>Hello ${name}</body></html>`);
});

app.listen(3000);

