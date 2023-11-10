import java.io.*;
import java.util.*;

/* Sort student information */

public class test {
    public static void main(String[] args) {

        try {
            File outFile = new File("test.out");
            if (!outFile.exists()) {
                outFile.createNewFile();
            }
            FileWriter fw = new FileWriter(outFile);
            PrintWriter writer = new PrintWriter(fw);


            List<String> students = new ArrayList<String>();

            File inpFile = new File("test.inp");
            FileReader fr = new FileReader(inpFile);
            BufferedReader br = new BufferedReader(fr);

            String line = "";

            while((line=br.readLine()) != null) {
                students.add(line);
            }

            br.close();

            students.remove(0);
            Collections.sort(students);


            int max = 0;

            for(String student : students) {
                int idx = student.lastIndexOf(" ");
                if(idx > max) {
                    max = idx;
                }
            }

            List<String> lastName = new ArrayList<String>();

            for(String student : students) {
                int idx = student.lastIndexOf(" ");
                StringBuffer str = new StringBuffer(student);
                int remain = max - student.substring(0, idx).length();
                for(int j=0; j<remain; j++) {
                    str.insert(idx, " ");
                }

                lastName.add(str.substring(max+1));

                System.out.println(str);
                writer.println(str);
            }

            System.out.println(" ");
            writer.println(" ");

            Set<String> set = new HashSet<String>(lastName);
            ArrayList<String> al = new ArrayList<>(set);

            Collections.sort(al);

            for (String str : al) {
                if(Collections.frequency(lastName, str) != 1) {
                    System.out.println(str + " " + Collections.frequency(lastName, str));
                    writer.println(str + " " + Collections.frequency(lastName, str));
                }
            }

            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
