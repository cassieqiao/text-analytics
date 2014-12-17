import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.queryParser.ParseException;
import org.apache.lucene.queryParser.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;


public class Searcher {
	public static void main(String[] args) throws 
	IOException, ParseException {
		String indexDir = "C:/Users/Cassie/Google Drive/MSiA/Fall 2014/MSiA 490/index";
		Scanner reader = new Scanner(System.in);
		System.out.println("Enter the string you want to search:");
		//get user input for a
		String input=reader.nextLine();		
		String q = input;
		search(indexDir, q);
	}
	
	
	public static void search(String indexDir, String q)
			throws IOException, ParseException {
			Directory dir = FSDirectory.open(new File(indexDir));
			IndexSearcher is = new IndexSearcher(dir);
			QueryParser parser = new QueryParser(Version.LUCENE_30,
			"contents",
			new StandardAnalyzer(
			Version.LUCENE_30));
			int count=0;
			Query query = parser.parse(q);
			System.out.println(query);
			TopDocs hits = is.search(query, 10);
			for(ScoreDoc scoreDoc : hits.scoreDocs) {
			Document doc = is.doc(scoreDoc.doc);
			String path = doc.get("fullpath");
			FileInputStream fstream = new FileInputStream(path);
			BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
			String line;
			while ((line = br.readLine()) != null) 
	        {
				String[] sentences = line.split("\n|\\.|\\,");

				for (int i = 0; i < sentences.length; i++)
	            {
				
	            	if (sentences[i].contains(q)){
	            		System.out.println(sentences[i]);
	            	}
	            }
	        }
				br.close();
			
			} 
			is.close();
			}
}
