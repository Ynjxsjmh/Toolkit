package file.kind;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.List;

import org.apache.poi.hslf.extractor.PowerPointExtractor;
import org.apache.poi.openxml4j.exceptions.InvalidFormatException;
import org.apache.poi.openxml4j.exceptions.OpenXML4JException;
import org.apache.poi.openxml4j.opc.OPCPackage;
import org.apache.poi.xslf.extractor.XSLFPowerPointExtractor;
import org.apache.poi.xslf.usermodel.XMLSlideShow;
import org.apache.poi.xslf.usermodel.XSLFSlide;
import org.apache.xmlbeans.XmlException;
import org.openxmlformats.schemas.drawingml.x2006.main.CTRegularTextRun;
import org.openxmlformats.schemas.drawingml.x2006.main.CTTextBody;
import org.openxmlformats.schemas.drawingml.x2006.main.CTTextParagraph;
import org.openxmlformats.schemas.presentationml.x2006.main.CTGroupShape;
import org.openxmlformats.schemas.presentationml.x2006.main.CTShape;
import org.openxmlformats.schemas.presentationml.x2006.main.CTSlide;

public class PPT {
	public static String readPPT(String filePath) {
		String content = null;
		if (filePath.endsWith(".ppt")) {
			try {
				FileInputStream in = new FileInputStream(filePath);
				PowerPointExtractor extractor = new PowerPointExtractor(in);
				content = extractor.getText();
				extractor.close();
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		} 
		return content;
	}
	
	
	public static String readPPTX(String filePath) {
		String content = null;
		if (filePath.endsWith(".pptx")) {
			try {
				FileInputStream in = new FileInputStream(filePath);
				OPCPackage d = OPCPackage.open(in);
				XSLFPowerPointExtractor extractor = new XSLFPowerPointExtractor(d);
				content = extractor.getText();
				extractor.close();
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (InvalidFormatException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (XmlException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (OpenXML4JException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		return content;
	}
	
	
	//逐个幻灯片抽取.pptx内容
	public String readPPTXByPart(String filePath) {
		String content = null;
		StringBuilder sb = new StringBuilder();
		try {
			FileInputStream in = new FileInputStream(filePath);
			XMLSlideShow xmlSlideShow = new XMLSlideShow(in);
			List<XSLFSlide> slides = xmlSlideShow.getSlides();
			for (XSLFSlide slide : slides) {
				CTSlide rawSlide = slide.getXmlObject();
				CTGroupShape gs = rawSlide.getCSld().getSpTree();
				CTShape[] shapes = gs.getSpArray();
				for (CTShape shape : shapes) {
					CTTextBody tb = shape.getTxBody();
					if (null == tb) {
						continue;
					}
					CTTextParagraph[] paras = tb.getPArray();
					for (CTTextParagraph textParagraph : paras) {
						CTRegularTextRun[] textRuns = textParagraph.getRArray();
						for (CTRegularTextRun textRun : textRuns) {
							sb.append(textRun.getT());
						}
					}
				}
			}
			xmlSlideShow.close();
			content = sb.toString();
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		return content;
	}

	public static void main(String[] args) {
		String filePath = "E:\\1courseware&&PPT\\2015年软件学院卓越工程师课程(统一建模语言UML)\\DEV275_06_ClassDiagrams(1).ppt";
		String filePath1 = "E:\\A2Z.pptx";
		System.out.println(PPT.readPPT(filePath1));
	}
}
