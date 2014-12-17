import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

import nu.xom.Serializer;
import edu.stanford.nlp.dcoref.Document;
import edu.stanford.nlp.ling.CoreAnnotations.SentencesAnnotation;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.pipeline.XMLOutputter;
import edu.stanford.nlp.util.CoreMap;




public class nlp {

	
	public static void main(String[] args) throws IOException {
		
		// Create an output writer
		PrintWriter xmlOut = null;
		try {
			xmlOut = new PrintWriter("C:/Users/Cassie/Google Drive/MSiA/Fall 2014/MSiA 490/hw/temp-out.xml");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		String contentForNLP = new String(Files.readAllBytes(Paths.get("C:/Users/Cassie/Google Drive/MSiA/Fall 2014/MSiA 490/small.txt")));
		
	    // creates a StanfordCoreNLP object, with POS tagging, lemmatization, NER, parsing, and coreference resolution 
	    Properties props = new Properties();
	    props.put("annotators", "tokenize, ssplit, pos, lemma, ner, parse, dcoref");
	    StanfordCoreNLP pipeline = new StanfordCoreNLP(props);
	    
	    // create an empty Annotation just with the given text
	    Annotation document = new Annotation(contentForNLP);
	    
	    // run all Annotators on this text
	    pipeline.annotate(document);
	   
	    // Print out the pipeline XML
	    pipeline.xmlPrint(document, xmlOut);
	    
	 
	}

}