/*
    Name: Aditya Desai
    Panel: 3
    Roll no.: PC - 15
    Assembler Pass 1
*/

import java.io.*;
import java.util.*;

class Operands {
	public String getStatement_class() {
		return statement_class;
	}

	public String getMachine_code() {
		return machine_code;
	}

	String statement_class;
	String machine_code;

	public Operands createTuple(String statement_class, String machine_code) {
		Operands Operands = new Operands();
		Operands.statement_class = statement_class;
		Operands.machine_code = machine_code;
		return Operands;
	}

	public Map<String, Operands> getOptable() {
		Map<String, Operands> op_table = new HashMap<>();
		op_table.put("STOP", createTuple("IS", "0"));
		op_table.put("ADD", createTuple("IS", "1"));
		op_table.put("SUB", createTuple("IS", "2"));
		op_table.put("MULT", createTuple("IS", "3"));
		op_table.put("MOVER", createTuple("IS", "4"));
		op_table.put("MOVEM", createTuple("IS", "5"));
		op_table.put("COMP", createTuple("IS", "6"));
		op_table.put("BC", createTuple("IS", "7"));
		op_table.put("DIV", createTuple("IS", "8"));
		op_table.put("READ", createTuple("IS", "9"));
		op_table.put("PRINT", createTuple("IS", "10"));
		op_table.put("DC", createTuple("DL", "1"));
		op_table.put("DS", createTuple("DL", "2"));
		op_table.put("START", createTuple("AD", "1"));
		op_table.put("END", createTuple("AD", "2"));
		op_table.put("ORIGIN", createTuple("AD", "3"));
		op_table.put("EQU", createTuple("AD", "4"));
		op_table.put("LTORG", createTuple("AD", "5"));
		op_table.put("AREG", createTuple("RG", "1"));
		op_table.put("BREG", createTuple("RG", "2"));
		op_table.put("CREG", createTuple("RG", "3"));
		op_table.put("EQ", createTuple("CC", "1"));
		op_table.put("LT", createTuple("CC", "2"));
		op_table.put("GT", createTuple("CC", "3"));
		op_table.put("LE", createTuple("CC", "4"));
		op_table.put("GE", createTuple("CC", "5"));
		op_table.put("NE", createTuple("CC", "6"));
		return op_table;
	}
}

class Tablevalue {
	int address;
	int index;

	public int getAddress() {
		return address;
	}

	public void setAddress(int address) {
		this.address = address;
	}

	public int getIndex() {
		return index;
	}

	public void setIndex(int index) {
		this.index = index;
	}
}

public class assemblerpass1 {
	public static boolean isOpCode(String token) {
		if ((new Operands()).getOptable().containsKey(token))
			return true;
		return false;
	}

	public static String stringOfTuple(Operands tuple) {
		return "(" + tuple.getStatement_class() + "," + tuple.getMachine_code() + ") ";
	}

	public static boolean isNumeric(String str) {
		try {
			Double.parseDouble(str);
			return true;
		} catch (NumberFormatException e) {
			return false;
		}
	}

	public static void printTable(BufferedWriter bw, LinkedHashMap<String, Tablevalue> symbol_table) throws IOException {
		for (String key : symbol_table.keySet()) {
			bw.write(key + "\t" + symbol_table.get(key).getAddress() + "\t" + symbol_table.get(key).getIndex() + "\n");
		}
	}
	
	public static int setLiteralTable(int address, LinkedHashMap<String, Tablevalue> literal_table) {
		for(String key : literal_table.keySet()) {
			Tablevalue tabValueHolder = literal_table.get(key);
			if(tabValueHolder.getAddress() == 0) {
				tabValueHolder.setAddress(address);
				address++;
			}
		}
		return address;
	}

	public static void main(String[] args) throws IOException {
		Map<String, Operands> OPTAB = (new Operands()).getOptable(); // get Optable
		LinkedHashMap<String, Tablevalue> symbol_table = new LinkedHashMap<>();
		LinkedHashMap<String, Tablevalue> literal_table = new LinkedHashMap<>();
		List<Integer> pool_table = new ArrayList<>();
		int symbol_table_pointer = 1;
		int literal_table_pointer = 1;
		int address_pointer = 0;
		ArrayList<String> intermediateCode = new ArrayList<>();
		try {
			File file = new File("assembly.txt"); // read ALP
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			String line;
			String intermediateLine = "";

			while ((line = br.readLine()) != null) {
				String[] tokens = line.split(" ");
				int tokenCounter = 0;
				if (address_pointer != 0)
					intermediateLine += String.valueOf(address_pointer) + ") ";
				for (int i = 0; i < tokens.length; i++) {
					Operands optuple = new Operands();
					String token = tokens[i];
					if (isOpCode(token)) {
						optuple = OPTAB.get(token);
						if (token.equals("END")) {
							intermediateLine = "";
							intermediateLine += stringOfTuple(OPTAB.get(token));
							address_pointer = setLiteralTable(address_pointer, literal_table);
							pool_table.add(literal_table_pointer);
							break;
						}	
						if(token.equals("LTORG")) {
							intermediateLine = "";
							address_pointer = setLiteralTable(address_pointer, literal_table);
							pool_table.add(literal_table_pointer);
						}
						if (optuple.getStatement_class().equals("RG") || optuple.getStatement_class().equals("CC"))
							intermediateLine += "(" + optuple.getMachine_code() + ") ";
						else
							intermediateLine += stringOfTuple(optuple);
						if (token.equals("START")) {
							address_pointer = Integer.parseInt(tokens[i + 1]) - 1;
							intermediateLine += "(C," + Integer.parseInt(tokens[i + 1]) + ") ";
							i++;
						} else if (token.equals("ORIGIN")) {
							Tablevalue symbol_table_item = symbol_table.get(tokens[i + 1]);
							address_pointer = symbol_table_item.getAddress();
							i++;
						}

					} else if (symbol_table.containsKey(token)) {
						intermediateLine += "(S," + symbol_table.get(token).getIndex() + ") ";
					} else if (tokenCounter == 0) { // if Label
						Tablevalue symbol_table_item = new Tablevalue();
						symbol_table_item.setAddress(address_pointer);
						symbol_table_item.setIndex(symbol_table_pointer);
						symbol_table.put(token, symbol_table_item);
						// intermediateLine += "(S," + symbol_table_pointer + ") ";
						symbol_table_pointer++;
					} else if (isNumeric(token)) {
						if (tokens[i - 1].equals("DS")) {
							Tablevalue symbol_table_item = new Tablevalue();
							symbol_table_item.setAddress(address_pointer);
							symbol_table_item.setIndex(symbol_table.get(tokens[i - 2]).getIndex());
							symbol_table.put(tokens[i - 2], symbol_table_item);
						} else if (tokens[i - 1].equals("DC")) {
							Tablevalue symbol_table_item = new Tablevalue();
							symbol_table_item.setAddress(address_pointer);
							symbol_table_item.setIndex(symbol_table.get(tokens[i - 2]).getIndex());
							symbol_table.put(tokens[i - 2], symbol_table_item);
						}
						intermediateLine += "(C," + token + ") ";
					} else {
						if (token.startsWith("=")) {
							Tablevalue littabHolder = new Tablevalue();
							littabHolder.setIndex(literal_table_pointer);
							intermediateLine += "(L," + literal_table_pointer + ") "; 
							literal_table_pointer++;
							literal_table.put(token, littabHolder);
						} else {
							Tablevalue symbol_table_item = new Tablevalue();
							symbol_table_item.setAddress(-1);
							symbol_table_item.setIndex(symbol_table_pointer);
							symbol_table.put(token, symbol_table_item);
							intermediateLine += "(S," + String.valueOf(symbol_table_pointer) + ") ";
							symbol_table_pointer++;
						}

					}
					tokenCounter++;
				}
				address_pointer++;
				tokenCounter = 0;
				intermediateCode.add(intermediateLine);
				intermediateLine = "";
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		File fout = new File("pass1_output.txt");
		FileOutputStream fos = new FileOutputStream(fout); 
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
		for (String line : intermediateCode) {
			bw.write(line + "\n");
		}
		bw.write("\nSYMBOL TABLE: \n");
		printTable(bw, symbol_table);
		bw.write("\nLITERAL TABLE: \n");
		printTable(bw, literal_table);
		bw.write("\npool_table:\n");
		for(int i : pool_table) {
			bw.write(String.valueOf(i) + "\n");
		}
		bw.close();
	}
}