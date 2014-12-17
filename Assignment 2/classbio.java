import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.lang.StringBuilder;
import java.io.InputStreamReader;

public class classbio {
	
	public static void main(String[] args) throws UnsupportedEncodingException {
	
	String dir = "C:/Users/Cassie/Downloads/classbios.txt";
	
	FileInputStream fstream = null;
	try {
		fstream = new FileInputStream(dir);
	} catch (FileNotFoundException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
	StringBuilder builder = new StringBuilder();
	String strLine="";

	try {
		while ((strLine = br.readLine()) != null)   {
		  	
			builder.append(strLine);			
		}
		String text = builder.toString();
		Pattern pattern = Pattern.compile("([0-9][0-9])?--+");
		String[] split = pattern.split(text);
		int count =0;
		for(String element : split){
			if (element.length()>10) {
				count +=1;
				String filename = "C:/Users/Cassie/Google Drive/MSiA/Fall 2014/MSiA 490/bios/"+count+".txt";
				PrintWriter writer = new PrintWriter(filename, "UTF-8");
				writer.println(element);
				writer.close();
			}
			
		}
					
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	} catch (Exception e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}

	//Close the input stream
	try {
		br.close();
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	
	}
	

}
