package engine;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

import javax.swing.JFileChooser;
import javax.swing.filechooser.FileNameExtensionFilter;

//import connection.Database;

public class SafMigracia {
	
	private static JFileChooser ourFileSelector = new JFileChooser();
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ourFileSelector.setFileSelectionMode(JFileChooser.FILES_ONLY);
	   	ourFileSelector.showSaveDialog(null);	   	
	   	File fl = ourFileSelector.getSelectedFile();
	   	String source_path = fl.getAbsolutePath();
	   	
	   	ArrayList<Uzivatel> uzivatelia = new ArrayList<Uzivatel>();
	   		   	
	   	try(BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(source_path),"Windows-1250"))){

		    
		    String riadok = br.readLine();
		   
		    while (riadok != null) {   	
		    	String[] splited = riadok.split("\\|");
		    	ArrayList<String> temp = new ArrayList<String>(Arrays.asList(splited));
		    	ArrayList<String> list = new ArrayList<String>();
		    	for (String prvok: temp){
		    		if (!prvok.equals("")){
		    			list.add(prvok.trim());
		    		}
		    	}
		    	
		    	Uzivatel uzivatel = new Uzivatel();
		    	uzivatel.meno = list.get(0);
		    	uzivatel.priezvisko = list.get(1);
		    	uzivatel.gender = list.get(2);
		    	uzivatel.dat_narodenia = list.get(3);
		    	uzivatel.bydlisko = list.get(4);
		    	uzivatel.mail = list.get(5); //niesu v DB modely, ignorujem
		    	uzivatel.discipliny = list.get(6); //niesu v DB modely, ignorujem
		    	uzivatel.klub = list.get(7);
		    	uzivatel.telefon = list.get(8);
		    	uzivatel.suhlas = list.get(9);
		    	uzivatel.user_id = list.get(10);
		    	
		    	
		    	uzivatelia.add(uzivatel);

		        riadok = br.readLine();
		    }

		}
		catch (IOException e){}
	   	
		MojaDatabase db = new MojaDatabase();
	   	db.vlozUzivatelov(uzivatelia);
	}
}


class Uzivatel{
	public String meno, priezvisko, gender, dat_narodenia, bydlisko, mail, klub, telefon, discipliny, suhlas, user_id;
	
	
	public Uzivatel(){
		meno = "";
		priezvisko = "";
		gender = "";
		dat_narodenia = "";
		bydlisko = "";
		mail = "";
		klub = "";
		telefon = "";
		suhlas = "";
		user_id = "";
		discipliny = "";
	}
}

class MojaDatabase extends connection.Database{
	
	public void vlozUzivatelov(ArrayList<Uzivatel> uzivatelia){
		
		try{
			super.CreateConnection();
			for (Uzivatel u: uzivatelia){
				String sql = String.format("INSERT INTO Hraci (krstne_meno, priezvisko, pohlavie, datum_narodenia, miesto_bydliska, klub, telefonne_cislo) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')", u.meno, u.priezvisko,u.gender, u.dat_narodenia, u.bydlisko, u.klub, u.telefon);      
				System.out.println(sql);
				super.InsertUpdateDeleteQuery(sql);
			}
			
			
			super.DisconectConnection();
		}
		catch(Exception e){}
	}
}