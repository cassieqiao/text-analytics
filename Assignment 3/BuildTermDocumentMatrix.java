import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

import org.apache.commons.math.linear.Array2DRowRealMatrix;
import org.apache.commons.math.linear.RealMatrix;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.TermFreqVector;
import org.apache.lucene.queryParser.ParseException;
import org.apache.lucene.queryParser.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;


public class BuildTermDocumentMatrix {
	
	public static void main(String[] args) throws IOException, ParseException {
		String dataDir = "C:/Users/Cassie/Google Drive/MSiA/Fall 2014/MSiA 490/bios";
		String indexDir = "C:/Users/Cassie/Google Drive/MSiA/Fall 2014/MSiA 490/index";
		RealMatrix rs= buildTermDocumentMatrix(dataDir,indexDir);
		double[][] rsdata = rs.getData();
		
		
			
		int k =1;
		String[] words = TermFrequency(k,rsdata,indexDir);
		/*
		for (int i =0; i<words.length;i++){
			System.out.print(words[i]+"\n");
		}*/
		//NaiveSum(words);
	}
	

private static Map<String, Integer> computeTermIdMap(String indexDir) throws IOException {
	IndexReader reader = IndexReader.open(FSDirectory.open(new File(indexDir)), true);
    Map<String,Integer> termIdMap = new HashMap<String,Integer>();
    int id = 0;
	int n = reader.numDocs();
	for (int j =0;j<n;j++){
		TermFreqVector vector = reader.getTermFreqVector(j, "contents");
	    String[] terms = vector.getTerms();
	    for (int i = 0; i < terms.length; i++) {
	    	String termText = terms[i];              
	        if (termIdMap.containsKey(termText))
	            continue;
	        else termIdMap.put(termText, id++);
	    }
	}
    
    return termIdMap;
}

public static double computeTfIdfWeight(int termFreq, int docCount,int numDocs){
	{
        if (termFreq > 0)
        {
            return  (1+Math.log((double)termFreq)) * Math.log(numDocs / (double) docCount);
        }
        else
        {
            return 0;
        }
    }
	
}

public static  int searchword(String indexDir, String q)
		throws IOException, ParseException {
		int count = 0;
		Directory dir = FSDirectory.open(new File(indexDir));
		IndexSearcher is = new IndexSearcher(dir);
		QueryParser parser = new QueryParser(Version.LUCENE_30,
		"contents",
		new StandardAnalyzer(
		Version.LUCENE_30));
		Query query = parser.parse(q);
		TopDocs hits = is.search(query, 10);
		for(ScoreDoc scoreDoc : hits.scoreDocs) {
		Document doc = is.doc(scoreDoc.doc);
		count++; 
		}
		is.close();
		return count;
		
		}

public static RealMatrix buildTermDocumentMatrix (String dataDir, String indexDir) throws IOException, ParseException {
	IndexReader reader = IndexReader.open(FSDirectory.open(new File(indexDir)), true);
    Map<String, Integer> termIdMap = computeTermIdMap(indexDir);
    int numDocs = reader.numDocs();         
    int numTerms = termIdMap.size();    //total number of terms     
    RealMatrix tdMatrix = new Array2DRowRealMatrix(numTerms, numDocs);
    	
    for (int j =0;j<numDocs;j++){
		TermFreqVector vector = reader.getTermFreqVector(j, "contents");
	    String[] terms = vector.getTerms();
	    int[] termsFreq = vector.getTermFrequencies();
	    
	    for (int i = 0; i < terms.length; i++) {               
	    	String termText = terms[i]; 
			int row = termIdMap.get(termText);
            int termFreq = termsFreq[i];
            int docCount=searchword(indexDir,termText); 
            double weight = computeTfIdfWeight(termFreq, docCount, numDocs);
            tdMatrix.setEntry(row,j, termFreq);
        }
    }
       return tdMatrix;
}

public static String[] TermFrequency(int k, double[][] rsdata,String indexDir) throws IOException{
	double maxValue =0.0;
	Integer termrow =0;
	Integer termcolumn=1;
	Map<String, Integer> termIdMap = computeTermIdMap(indexDir);
	String strKey = null;
	String[] words=new String[k];

	
	for(int b=0;b<k;b++){
		for(int i = 0; i < rsdata.length; i++)
		   {
		      //for(int j = 0; j < rsdata[1].length; j++)
		      {
		    	  if (rsdata[i][1] > maxValue) {
		              maxValue = rsdata[i][1];
		    	  	  termrow=i;
		    	  	 // termcolumn=j;
		    	  	  }
		    	  
		      }
		   }
		for(Map.Entry entry: termIdMap.entrySet()){
	      if(termrow.equals(entry.getValue())){
	            strKey = (String) entry.getKey();
	            break; 
	        }}
		System.out.println(maxValue+" "+strKey+" at doc"+termcolumn);
		words[b]=strKey;
		rsdata[termrow][termcolumn]=0.0;
		maxValue=0.0;
	}
	
	return words;
}

public static void NaiveSum(String[] words) throws IOException{
	for(int b=0;b<words.length;b++){
		FileInputStream fstream = new FileInputStream("C:/Users/Cassie/Google Drive/MSiA/Fall 2014/MSiA 490/bios/1.txt");
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
		String line;
		while ((line = br.readLine()) != null) 
		{
		String[] sentences = line.split("\n|\\.|\\,");
			for (int a = 0; a < sentences.length; a++)
			{
				if (sentences[a].contains(words[b])){
					System.out.println(sentences[a]);
				}
			}
		}
	}

} 
}