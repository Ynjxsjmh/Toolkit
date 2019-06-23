package file.kind;

import java.io.File;
import java.io.FileInputStream;

import org.apache.poi.hwpf.HWPFDocument;
import org.apache.poi.hwpf.extractor.WordExtractor;
import org.apache.poi.openxml4j.opc.OPCPackage;
import org.apache.poi.xwpf.extractor.XWPFWordExtractor;
import org.apache.poi.xwpf.usermodel.XWPFDocument;

public class Word {
	public static String readDoc(String filePath) {
		String text = "";
		File file = new File(filePath);
		try {
			if (filePath.endsWith(".doc")) {
				FileInputStream fis = new FileInputStream(file);
				HWPFDocument doc = new HWPFDocument(fis);
				// ------------------------------------------------------------------
				WordExtractor extractor = new WordExtractor(doc);
				text = extractor.getText();
				// -----------------------------------------------------------------
				// String doc1 = doc.getDocumentText();
				// System.out.println(doc1);
				// -----------------------------------------------------------------
				// StringBuilder doc2 = doc.getText();
				// System.out.println(doc2);
				// -----------------------------------------------------------------
				// Range rang = doc.getRange();
				// String doc3 = rang.text();
				// System.out.println(doc3);
				// -----------------------------------------------------------------
				text = text.replaceAll("(\\r\\n){2,}", "\r\n"); // 去掉word文档中的多个换行
				text = text.replaceAll("(\\n){2,}", "\n");
				fis.close();
				extractor.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return text;
	}
	
	public static String readDocx(String filePath) {
		String text = "";
		try {
			if (filePath.endsWith(".docx")) {
				// -----------------------------------------------------------------
				 File file = new File(filePath);
				 FileInputStream fins = new FileInputStream(file);
				 XWPFDocument doc = new XWPFDocument(fins);
				 XWPFWordExtractor extractor = new XWPFWordExtractor(doc);
				 text = extractor.getText();

				// ----------------------------------------------------------------
				//FileInputStream fis = new FileInputStream(new File(filePath)); // 最简洁
				//OPCPackage oPCPackage = OPCPackage.open(fis);
				//XWPFWordExtractor extractor = new XWPFWordExtractor(oPCPackage);
				//text = extractor.getText();

				// ----------------------------------------------------------------
				// OPCPackage oPCPackage = POIXMLDocument.openPackage(filePath);
				// XWPFDocument xwpf = new XWPFDocument(oPCPackage);
				// POIXMLTextExtractor ex = new XWPFWordExtractor(xwpf);
				// text = ex.getText();
				// -----------------------------------------------------------------

				text = text.replaceAll("(\\r\\n){2,}", "\r\n");
				text = text.replaceAll("(\\n){2,}", "\n");
//				fis.close();
				extractor.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return text;
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String filePath = "E:\\1courseware&&PPT\\DB2\\DB2实验报告2_学号_姓名.doc";
		String filePath2 = "E:\\1courseware&&PPT\\计算机伦理学\\55161108 宋栿浒 计算机职业道德论文.doc";
		String filePath1 = "E:\\1courseware&&PPT\\DB2\\DB2实验报告1_学号_姓名.docx";
		String content = Word.readDoc(filePath2);
		System.out.println(content);
	}
}
