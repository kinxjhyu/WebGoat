import java.sql.*;

public class VulnerableJdbc {
    public void getUser(String username) throws Exception {
        Connection conn = DriverManager.getConnection("jdbc:mysql://db:3306/app", "user", "pass");
        Statement stmt = conn.createStatement();
        // 취약: 사용자 입력을 문자열로 직접 결합
        String sql = "SELECT * FROM users WHERE username = '" + username + "'";
        ResultSet rs = stmt.executeQuery(sql);
        while (rs.next()) {
            System.out.println(rs.getString("email"));
        }
        rs.close();
        stmt.close();
        conn.close();
    }
}

