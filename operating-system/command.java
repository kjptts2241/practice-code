import java.io.*;
import java.util.*;

/* Unix-Dos Commands Comparison */

public class command {
    public static void main(String[] args) {

        try {
            File outFile = new File("command.out");
            if (!outFile.exists()) {
                outFile.createNewFile();
            }
            FileWriter fw = new FileWriter(outFile);
            PrintWriter writer = new PrintWriter(fw);


            List<String> commands = new ArrayList<String>();

            File inpFile = new File("command.inp");
            FileReader fr = new FileReader(inpFile);
            BufferedReader br = new BufferedReader(fr);

            String line = "";

            while((line=br.readLine()) != null) {
                commands.add(line);
            }

            br.close();

            commands.remove(0);

            Map<String, String> commandMap = new HashMap<>();
            commandMap.put("ls", "dir");
            commandMap.put("dir", "ls");
            commandMap.put("mkdir", "md");
            commandMap.put("md", "mkdir");
            commandMap.put("rmdir", "rd");
            commandMap.put("rd", "rmdir");
            commandMap.put("rm", "del");
            commandMap.put("del", "rm");
            commandMap.put("cp", "copy");
            commandMap.put("copy", "cp");
            commandMap.put("mv", "rename");
            commandMap.put("rename", "mv");
            commandMap.put("clear", "cls");
            commandMap.put("cls", "clear");
            commandMap.put("pwd", "cd");
            commandMap.put("cd", "pwd");
            commandMap.put("cat", "type");
            commandMap.put("type", "cat");
            commandMap.put("man", "help");
            commandMap.put("help", "man");
            commandMap.put("date", "time");
            commandMap.put("time", "date");
            commandMap.put("find", "find");
            commandMap.put("grep", "findstr");
            commandMap.put("findstr", "grep");
            commandMap.put("more", "more");
            commandMap.put("diff", "comp");
            commandMap.put("comp", "diff");
            commandMap.put("ed", "edlin");
            commandMap.put("edlin", "ed");
            commandMap.put("sort", "sort");
            commandMap.put("lsattr", "attrib");
            commandMap.put("attrib", "lsattr");
            commandMap.put("pushd", "pushd");
            commandMap.put("popd", "popd");
            commandMap.put("ps", "taskmgr");
            commandMap.put("taskmgr", "ps");
            commandMap.put("kill", "tskill");
            commandMap.put("tskill", "kill");
            commandMap.put("halt", "shutdown");
            commandMap.put("shutdown", "halt");
            commandMap.put("ifconfig", "ipconfig");
            commandMap.put("ipconfig", "ifconfig");
            commandMap.put("fsck", "chkdsk");
            commandMap.put("chkdsk", "fsck");
            commandMap.put("free", "mem");
            commandMap.put("mem", "free");
            commandMap.put("debugfs", "scandisk");
            commandMap.put("scandisk", "debugfs");
            commandMap.put("lpr", "print");
            commandMap.put("print", "lpr");

            for(String command : commands) {
                String commandMapping = commandMap.get(command);
                if (commandMapping != null) {
                    System.out.println(command + " -> " + commandMapping);
                    writer.println(command + " -> " + commandMapping);
                }
            }

            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}


