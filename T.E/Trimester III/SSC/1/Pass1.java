import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;


class Operand {
    String mnop;
    String cl;
    int mcop;

    Operand () {
        mnop = ""; cl = ""; mcop = -1;
    } 

    Operand (String mnop, String cl, int mcop) {
        mnop = mnop; cl = cl;  mcop = mcop; 
    }
}


class Register {
    String name;
    int id;

    Register (String name, int id) {
        name = name; id = id; 
    }
}

class SymbolData {
    int addr;
    int len;

    SymbolData() {
        addr = -1; len = 1;
    }

    SymbolData(int addr, int len) {
        addr = addr; len = len;
    } 
}

class Pass1 {

    public static void main(String[] args) throws IOException {
        
        // Genereating the OPTABLE
        ArrayList<Operand> optable = new ArrayList<Operand>(15);
        optable.add(new Operand("STOP","IS",0));
		optable.add(new Operand("ADD","IS",1));
		optable.add(new Operand("SUB","IS",2));
		optable.add(new Operand("MULT","IS",3));
		optable.add(new Operand("MOVER","IS",4));
		optable.add(new Operand("MOVEM","IS",5));
		optable.add(new Operand("COMP","IS",6));
		optable.add(new Operand("BC","IS",7));
		optable.add(new Operand("DIV","IS",8));
		optable.add(new Operand("READ","IS",9));
		optable.add(new Operand("PRINT","IS",10));
		optable.add(new Operand("DC","DL",1));
		optable.add(new Operand("DS","DL",2));
		optable.add(new Operand("START","AD",1));
		optable.add(new Operand("END","AD",2));

        // Identifying the registers
        Register ra = new Register("AREG", 1);
        Register rb = new Register("BREG", 2);

        // Declaring the SYMBOL TABLE
        HashMap<String, SymbolData> symtable = new HashMap<String, SymbolData>();

        // Read assembly code from file
        FileReader file = new FileReader("assembly.txt");
        BufferedReader br = new BufferedReader(file);

        System.out.print(br.readLine());
        br.close();
    }
}