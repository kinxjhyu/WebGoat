import java.util.Random;

public class CryptoExample {
    public byte[] generateToken() {
        Random rnd = new Random();
        byte[] token = new byte[16];
        for (int i = 0; i < token.length; i++) {
            token[i] = (byte) rnd.nextInt(256);
        }
        return token;
    }
}

