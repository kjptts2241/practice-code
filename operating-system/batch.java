import java.io.*;
import java.util.*;
import java.util.stream.Stream;

/* Operating Systems Batch Simulation */

public class batch {
    public static void main(String[] args) {

        try {
            File outFile = new File("batch.out");
            if (!outFile.exists()) {
                outFile.createNewFile();
            }
            FileWriter fw = new FileWriter(outFile);
            PrintWriter writer = new PrintWriter(fw);


            List<String> batchs = new ArrayList<String>();

            File inpFile = new File("batch.inp");
            FileReader fr = new FileReader(inpFile);
            BufferedReader br = new BufferedReader(fr);

            String line = "";

            while((line=br.readLine()) != null) {
                batchs.add(line);
            }

            br.close();

            batchs.remove(0);


            int turnaroundTime = 0;
            int idleTime = 0;

            for(String batch : batchs) {
                String[] processTime = batch.split(" ");
                int[] process = Stream.of(processTime).mapToInt(Integer::parseInt).toArray();

                for (int i = 0; i < process.length; i++) {

                    if (process[i] != -1) {
                        if ((i + 1) % 2 == 0) {
                            idleTime += process[i];
                            turnaroundTime += process[i];
                        } else {
                            turnaroundTime += process[i];
                        }
                    }
                }
            }

            writer.println(idleTime + " " + turnaroundTime);

            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}


