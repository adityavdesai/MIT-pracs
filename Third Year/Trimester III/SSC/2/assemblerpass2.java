/*
    Name: Aditya Desai
    Panel: 3
    Roll no.: PC - 15
    Assembler Pass 2
*/

import java.io.*;
import java.util.*;

class Symbol
{
	String name;
	int addr;
	int len;
	Symbol(String n,int a,int l)
	{
		this.name = n;
		this.addr = a;
		this.len = l;
	}
}

public class assemblerpass2
{
	public static void main(String[] args) throws IOException
	{
		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new FileReader("pass1_output.txt"));
		String line;

		ArrayList<Symbol> symbol_table = new ArrayList<Symbol>();

		int cont_flag = 1;

		while(cont_flag == 1)
		{
			System.out.println("Enter symbol name:");
			String sym = sc.nextLine();
			System.out.println("Enter symbol address:");
			int address = sc.nextInt();
			System.out.println("Enter symbol length:");
			int len = sc.nextInt();

			symbol_table.add(new Symbol(sym,address,len));

			System.out.println("Enter 1 to continue :");
			cont_flag = sc.nextInt();
		}

		Iterator<Symbol> d = symbol_table.iterator();
		Symbol temp;
		while(d.hasNext())
		{
			temp = d.next();
			System.out.println(temp.name + " " + temp.addr + " " + temp.len);
		}

		BufferedWriter bw = new BufferedWriter(new FileWriter("pass2_output.txt"));
		
		int first = 1;
		while((line = br.readLine()) != null)
		{
			if(first == 1)
			{
				first = 0;
			}
			else
			{
				String[] words = line.split("\\s+");
				int length = words[1].length();
				String[] instr = words[1].substring(1,length-1).split(","); 
				if(instr[0].equals("AD") && (instr[1].equals("1") || instr[1].equals("2")))
				{

				}
				else
				{
					String nline = "";
					nline = nline + words[0] + " + ";
					if(instr[0].equals("IS"))
					{
						if(instr[1].equals(0))
						{
							nline = nline + "00 0 000" + " ";
						}
						else
						{
							nline = nline + instr[1] + " ";
							int l2 = words[2].length();
							String[] arg = words[2].substring(1,l2-1).split(",");
							if(arg[0].equals("S"))
							{
								Symbol s = symbol_table.get(Integer.parseInt(arg[1]));
								nline = nline + s.addr + " ";
							}
							else
							{
								nline = nline + arg[0] + " ";
							}

							l2 = words[3].length();
							arg = words[3].substring(1,l2-1).split(",");
							if(arg[0].equals("S"))
							{
								int index = Integer.parseInt(arg[1]) - 1;
								Symbol s = symbol_table.get(index);
								nline = nline + s.addr + " ";
							}
							else
							{
								nline = nline + arg[0] + " ";
							}
						}
					}
					else if(instr[0].equals("DL") && instr[1].equals("1"))
					{
						nline = nline + "00 0 ";
						int lenx = words[2].length();
						String[] arg = words[2].substring(1,lenx-1).split(",");
						nline = nline + arg[1] + " ";
					}
					bw.write(nline);
					bw.newLine();
				}
			}
		}
		bw.close();
	}
}