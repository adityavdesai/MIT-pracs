/*
    Name: Aditya Desai
    Panel: 3
    Roll no.: PC - 15
    Macroprocessor Pass 2
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
    MNT(int i, String a, int ind) {
        this.index = i;
        this.name = a;
        this.mdt_index = ind;
    }
}

class MacroprocessorPass2 {
    private static int searchMNT(Vector<MNT> a, String b) {
        int i,pos = -1;
        for(i = 0; i < a.size(); i++) {
            if(a.get(i).name.equals(b)) { pos = i; break; }
        }
        return pos;
    }

    public static void main(String[] args) throws Exception {
        Vector<MDT> mdt = new Vector<MDT>();
        Vector<MNT> mnt = new Vector<MNT>();
        Vector<String> isc = new Vector<String>();
        String line;
        Boolean flag;

        BufferedReader br = new BufferedReader(new FileReader("MDT.txt"));
        while((line = br.readLine()) != null) {
            String row[] = line.split("\\s+", 2);
            mdt.addElement(new MDT(Integer.parseInt(row[0]), row[1]));
        }
        br.close();

        br = new BufferedReader(new FileReader("MNT.txt"));
        while((line = br.readLine()) != null) {
            String row[] = line.split("\\s+");
            mnt.addElement(new MNT(Integer.parseInt(row[0]), row[1], Integer.parseInt(row[2])));
        }
        br.close();

        br = new BufferedReader(new FileReader("Intermediate.txt"));
        while((line = br.readLine()) != null) {
            isc.addElement(line);
        }
        br.close();
        
        for(int i = 0; i < isc.size(); i++) {
            String instr[] = isc.get(i).split("\\s+");

            int loc = searchMNT(mnt,instr[0]);
            if(loc == -1) System.out.println(isc.get(i));

            else if(loc != -1) {
                int mdt_ind = mnt.get(loc).mdt_index;
                String ala[] = instr[1].split("\\,");
                StringBuffer ss = new StringBuffer();
                for(int j = mdt_ind; j < mdt.size(); j++) {
                    flag = false;
                    String inst = mdt.get(j).inst;
                    if(inst.equals("MEND")) break;
                    else {
                        for(int k = 0; k < inst.length(); k++) {
                            if(!flag && inst.charAt(k) != '#') System.out.print(inst.charAt(k));
                            else if(!flag && inst.charAt(k) == '#') flag = true;
                            else if(flag && inst.charAt(k) == ',') {
                                int pos = Integer.parseInt(ss.toString());
                                System.out.print(ala[pos - 1]);
                                ss.delete(0, ss.length());
                                flag = false;
                            }
                            else if(flag) {
                                ss.append(inst.charAt(k));
                            }
                        }
                        if(ss.length() > 0) {
                            int pos = Integer.parseInt(ss.toString());
                            System.out.print(ala[pos - 1]);
                            System.out.println();
                            ss.delete(0, ss.length());
                        }
                    }
                }
            }
        }
    }

}


/*

    INPUT:-

MDT:-
1	INCR1	&FIRST,&SECOND=DATA9
2	A	1,#1
3	L	2,#2
4	MEND
5	INCR2	&ARG1,&ARG2
6	L	3,#1
7	ST	4,#2
8	MEND

MNT:-
1	INCR1	1
2	INCR2	5

Intermediate:-
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

PRG2    START
USING   *,BASE
A       1,DATA1
L       2,DATA12
L       3,DATA3
ST      4,DATA4
FOUR    DC      F'4'
FIVE    DC      F'5'
BASE    EQU     8
TEMP    DS      '1'F
DROP    8
END

*/