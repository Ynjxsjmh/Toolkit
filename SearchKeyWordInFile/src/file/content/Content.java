package file.content;

import file.kind.Excle;
import file.kind.Other;
import file.kind.PDF;
import file.kind.PPT;
import file.kind.Word;

public class Content {
	public static String getContent(String filePath) {
		String suffix = filePath.split("\\.")[1];   //java spilt������.���ַ�Ҫ��ת���\\
		String content = null;
		
		if (suffix.equals("exe") || suffix.equals("class")) {
			return null;
		}
		
		switch (suffix) {
		case "pdf":
			content = PDF.getTextFromPdf(filePath);
			break;
		case "doc":
			content = Word.readDoc(filePath);
			break;
		case "docx":
			content = Word.readDocx(filePath);
			break;
		case "ppt":
			content = PPT.readPPT(filePath);
			break;
		case "pptx":
			content = PPT.readPPTX(filePath);
			break;
		case "xls":
			content = Excle.readXLS(filePath);
			break;
		case "xlsx":
			content = Excle.readXLSX(filePath);
			break;
		default:
			content = Other.getContent(filePath);
			break;
		}
		
		return content;
	}
}
