import java.io.File;
import java.io.FileFilter;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.FileReader;

import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
	
public class Indexer {
		
	public static void main(String[] args) throws Exception {
		String dataDir = "C:/Users/Cassie/Google Drive/MSiA/Fall 2014/MSiA 490/hw";
		String indexDir = "C:/Users/Cassie/Google Drive/MSiA/Fall 2014/MSiA 490/hw/projct_index";
		Indexer indexer = new Indexer(indexDir);
		long start = System.currentTimeMillis();
		int numIndexed;
		try {
			numIndexed = indexer.index(dataDir, new TextFilesFilter());
			} finally {
			indexer.close();
			}
			long end = System.currentTimeMillis();
			System.out.println("Indexing " + numIndexed + " files took "
			+ (end - start) + " milliseconds");
			}
	
	private IndexWriter writer;
	
	public Indexer(String indexDir) throws IOException {
		Directory dir = FSDirectory.open(new File(indexDir));
		
		writer = new IndexWriter(dir,
				new StandardAnalyzer(
				Version.LUCENE_30),
				true,
				IndexWriter.MaxFieldLength.UNLIMITED);
		}
	
	public void close() throws IOException {
		writer.close();
		}
	
	public int index(String dataDir, FileFilter filter)
			throws Exception {
			File[] files = new File(dataDir).listFiles();
			for (File f: files) {
				if (!f.isDirectory() &&
				!f.isHidden() &&
				f.exists() &&
				f.canRead() &&
				(filter == null || filter.accept(f))) {
				indexFile(f);
				}
				}
				return writer.numDocs();
				}

	private static class TextFilesFilter implements FileFilter {
		public boolean accept(File path) {
		return path.getName().toLowerCase()
		.endsWith(".txt");
		}
		}
	
	protected Document getDocument(File f) throws Exception {
		Document doc = new Document();
		doc.add(new Field("contents", new FileReader(f), Field.TermVector.YES));
	    doc.add(new Field("filename", f.getName(),
	    		Field.Store.YES, Field.Index.NOT_ANALYZED));
	    		doc.add(new Field("fullpath", f.getCanonicalPath(),
	    		Field.Store.YES, Field.Index.NOT_ANALYZED));
	    return doc;
		}
	
	private void indexFile(File f) throws Exception {
		System.out.println("Indexing " + f.getCanonicalPath());
		Document doc = getDocument(f);
		writer.addDocument(doc);
		}
	
	

	}
	
	
	

