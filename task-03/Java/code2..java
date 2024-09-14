import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;

public class FileCopy {
    public static void main(String[] args) {
        try {
            // Read from input.txt and write to output.txt
            String content = new String(Files.readAllBytes(Paths.get("input.txt")));
            Files.write(Paths.get("output.txt"), content.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
