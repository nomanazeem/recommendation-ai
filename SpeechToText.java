import java.io.BufferedReader;
import java.io.InputStreamReader;

public class SpeechToText {

    public static void main(String[] args) {
        try {
            ProcessBuilder pb = new ProcessBuilder("python3", "speech_to_text3.py");
            pb.redirectErrorStream(true);
            Process process = pb.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            process.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}