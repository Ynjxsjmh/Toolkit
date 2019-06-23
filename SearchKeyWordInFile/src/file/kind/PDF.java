package file.kind;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import org.apache.pdfbox.io.RandomAccessFile;
import org.apache.pdfbox.io.RandomAccessRead;
import org.apache.pdfbox.pdfparser.PDFParser;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.encryption.InvalidPasswordException;
import org.apache.pdfbox.text.PDFTextStripper;

public class PDF {
	public static String getTextFromPdf(String filePath) {
		String content = null;
		PDDocument document = null;
		RandomAccessRead read = null;
		try {
			read = new RandomAccessFile(new File(filePath), "rw");
			PDFParser parser = new PDFParser(read);
			parser.parse();
			document = parser.getPDDocument();
			PDFTextStripper stripper = new PDFTextStripper();
			content = stripper.getText(document);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (read != null) {
				try {
					read.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			if (document != null) {
				try {
					document.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		return content;
	}
	
	public static String readPdf(String filePath) {
		File input = new File(filePath);
		String content = null;
		try {
			PDDocument pd = PDDocument.load(input);
			PDFTextStripper stripper = new PDFTextStripper();
			content = stripper.getText(pd);
		} catch (InvalidPasswordException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return content;
	}

	public static void main(String[] args) throws IOException {
		PDF pdf = new PDF();
//		System.out.println(pdf.getTextFromPdf(
//				"D:\\SoftWare\\Java_EE_eclipse\\searchFileMaterial\\论文翻译 - 副本 (2)\\1国际学术刊物\\A类\\Quantifying the Effect of Code Smells.pdf"));
		File input = new File("D:\\SoftWare\\Java_EE_eclipse\\searchFileMaterial\\论文翻译 - 副本 (2)\\1国际学术刊物\\A类\\Quantifying the Effect of Code Smells.pdf");
		PDDocument pd = PDDocument.load(input);
		PDFTextStripper stripper = new PDFTextStripper();
		System.out.println(stripper.getText(pd));
	}
}
