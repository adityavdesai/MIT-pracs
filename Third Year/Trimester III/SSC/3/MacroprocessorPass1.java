/*
    Name: Aditya Desai
    Panel: 3
    Roll no.: PC - 15
    Macroprocessor Pass 1
*/

import java.util.Vector;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

class MDT {
    int index;
    String inst;
    MDT(int i, String a) {
        this.index = i;
        this.inst = a;
    }
}

class MNT {
    int index,mdt_index;
    String name;
    Vector<String> ala;
    MNT(int i, String a, int ind, Vector<String> b) {
        this.index = i;
        this.name = a;
        this.mdt_index = ind;
        this.ala = b;
    }
}

class MacroprocessorPass1 {
    
    public static void main(String[] kwargs) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("macro_code.txt"));
        Vector<MDT> mdt = new Vector<MDT>();
        Vector<MNT> mnt = new Vector<MNT>();
        Vector<String> isc = new Vector<String>();
        String line;
        boolean isMacro = false;
        while((line = br.readLine()) != null) {
            line = line.trim();
            if(line.isEmpty()) continue;
            if(line.contains("MACRO")) isMacro = true; //start entering into MDT
            if(isMacro) {
                line = br.readLine(); 
                
                String word[] = line.split("\\s+");    // Split by whitespace

                String args[] = word[1].split("\\,");    // Split by ,
                
                Vector<String> arg = new Vector<String>();
                for(int i = 0; i < args.length; i++) {
                    String p = args[i];
                    if(args[i].contains("=")) p = args[i].substring(0,args[i].indexOf('='));
                    arg.addElement(p);
                }
                mnt.addElement(new MNT(mnt.size() + 1, word[0], mdt.size() + 1, arg));
                mdt.addElement(new MDT(mdt.size() + 1, line));
                line = br.readLine();
                while(!line.equals("MEND")) {
                    if(line.contains("&")) {
                        int i = line.indexOf('&');
                        MNT h = mnt.get(mnt.size() - 1);
                        int j;
                        for(j = 0; j < h.ala.size(); j++) {
                            if(line.substring(i).equals(h.ala.get(j)))
                                break;
                        }
                        mdt.addElement(new MDT(mdt.size() + 1, line.substring(0,i)+"#"+(j+1)));
                    }
                    else mdt.addElement(new MDT(mdt.size() + 1, line));
                    line = br.readLine();
                }
                if(line.equals("MEND")) mdt.addElement(new MDT(mdt.size() + 1, line));
                isMacro = false;
            }
            else {
                isc.addElement(line);
            }
        }
        br.close();

        System.out.println("MDT:-");
        BufferedWriter bw = new BufferedWriter(new FileWriter("MDT.txt"));
        for(int i = 0; i < mdt.size(); i++) {
            MDT word = mdt.get(i);
            System.out.println(word.index+"\t"+word.inst);
            bw.write(word.index+"\t"+word.inst + "\n");
        }
        bw.close();

        System.out.println("\nMNT:-");
        bw = new BufferedWriter(new FileWriter("MNT.txt"));
        for(int i = 0; i < mnt.size(); i++) {
            MNT word = mnt.get(i);
            System.out.println(word.index+"\t"+word.name+"\t"+word.mdt_index);
            bw.write(word.index+"\t"+word.name+"\t"+word.mdt_index + "\n");
        }
        bw.close();

        System.out.println("\nALA:-");
        bw = new BufferedWriter(new FileWriter("ALA.txt"));
        for(int i = 0; i < mnt.size(); i++) {
            MNT word = mnt.get(i);
            for(int j = 0; j < word.ala.size(); j++) {
                System.out.print(word.ala.get(j)+"\t");
                bw.write(word.ala.get(j)+"\t");
            }
            bw.write("\n");
            System.out.println();
        } 
        bw.close();
          
        System.out.println("\nIntermediate code:-");
        bw = new BufferedWriter(new FileWriter("Intermediate.txt"));
        for(int i = 0; i < isc.size(); i++) {
            System.out.println(isc.get(i));
            bw.write(isc.get(i) + "\n");
        }
        bw.close();
    }
}



/*
    INPUT:-

MACRO
INCR1	&FIRST,&SECOND=DATA9
A	1,&FIRST
L	2,&SECOND
MEND
MACRO
INCR2	&ARG1,&ARG2
L	3,&ARG1
ST	4,&ARG2
MEND
PRG2	START
	USING	*,BASE
INCR1	DATA1,DATA12
INCR2	DATA3,DATA4
FOUR	DC	F'4'
FIVE	DC	F'5'
BASE	EQU	8
TEMP	DS	'1'F
	DROP	8
	END


    OUTPUT:-

MDT:-
1       INCR1   &FIRST,&SECOND=DATA9
2       A       1,#1
3       L       2,#2
4       MEND
5       INCR2   &ARG1,&ARG2
6       L       3,#1
7       ST      4,#2
8       MEND

MNT:-
1       INCR1   1
2       INCR2   5

ALA:-
&FIRST  &SECOND
&ARG1   &ARG2

Intermediate code:-
PRG2    START
USING   *,BASE
INCR1   DATA1,DATA12
INCR2   DATA3,DATA4
FOUR    DC      F'4'
FIVE    DC      F'5'
BASE    EQU     8
TEMP    DS      '1'F
DROP    8
END

*/