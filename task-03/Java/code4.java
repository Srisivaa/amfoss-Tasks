import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.stream.IntStream;

public class DiamondPattern {
    public static void main(String[] args) {
        try {
            String content = new String(Files.readAllBytes(Paths.get("input.txt")));
            int n = Integer.parseInt(content.trim());
            
            StringBuilder diamond = new StringBuilder();
            
            for (int i = 0; i < n; i++) {
                diamond.append(" ".repeat(Math.max(0, n - i - 1)))
                        .append("*".repeat(2 * i + 1))
                        .append("\n");
            }
            for (int i = n - 2; i >= 0; i--) {
                diamond.append(" ".repeat(Math.max(0, n - i - 1)))
                        .append("*".repeat(2 * i + 1))
                        .append("\n");
            }
            
            Files.write(Paths.get("output.txt"), diamond.toString().getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}