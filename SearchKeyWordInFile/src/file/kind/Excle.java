package file.kind;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.text.NumberFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Iterator;

import org.apache.poi.hssf.extractor.ExcelExtractor;
import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFDataFormat;
import org.apache.poi.hssf.usermodel.HSSFDateUtil;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.extractor.XSSFExcelExtractor;
import org.apache.poi.xssf.usermodel.XSSFCell;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class Excle {
	// ֱ�ӳ�ȡxls�е�����
	public static String extractorXLS(String filePath) {
		String text = null;
		try {
			FileInputStream ips = new FileInputStream(filePath);
			HSSFWorkbook wb = new HSSFWorkbook(ips);
			ExcelExtractor ex = new ExcelExtractor(wb);
			ex.setFormulasNotResults(true);
			ex.setIncludeSheetNames(false);
			text = ex.getText();
			System.out.println(text);
			ex.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return text;
	}

	// ֱ�ӳ�ȡxlsx�е�����
	public String extractorXLSX(String filePath) {
		String text = null;
		try {
			FileInputStream ips = new FileInputStream(filePath);
			XSSFWorkbook wb = new XSSFWorkbook(ips);
			XSSFExcelExtractor ex = new XSSFExcelExtractor(wb);
			ex.setFormulasNotResults(true);
			ex.setIncludeSheetNames(false);
			text = ex.getText();
			System.out.println(text);
			ex.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return text;
	}

	// ͨ���Ե�Ԫ���������ʽ����ȡ��Ϣ ������Ҫ�жϵ�Ԫ������Ͳſ���ȡ��ֵ
	public static String readXLS(String filePath) {
		StringBuilder content = null;
		if (filePath.endsWith(".xls")) {
			content = new StringBuilder();
			try {
				FileInputStream ips = new FileInputStream(filePath);
				HSSFWorkbook workbook = new HSSFWorkbook(ips);
				HSSFSheet sheet = workbook.getSheetAt(0);
				for (Iterator<Row> ite = sheet.rowIterator(); ite.hasNext();) {
					HSSFRow row = (HSSFRow) ite.next();
					System.out.println();
					for (Iterator<Cell> itet = row.cellIterator(); itet.hasNext();) {
						HSSFCell cell = (HSSFCell) itet.next();
						// Cell cell = itet.next(); //Ҳ��

						// ------------------------------------------------
						if (convertCell(cell).length() > 0)
							content.append(convertCell(cell));
						content.append(" ");

						// -------------------------------------------------
						// ���¿��Ա������ָ�ʽ
						// switch (cell.getCellTypeEnum()) {
						// case BOOLEAN:
						// // �õ�Boolean����ķ���
						// System.out.print(cell.getBooleanCellValue() + " ");
						// break;
						// case NUMERIC:
						// // �ȿ��Ƿ������ڸ�ʽ
						// if (HSSFDateUtil.isCellDateFormatted(cell)) {
						// // ��ȡ���ڸ�ʽ
						// System.out.print(cell.getDateCellValue() + " ");
						// } else {
						// // ��ȡ����
						// System.out.print(cell.getNumericCellValue() + " ");
						// }
						// break;
						// case FORMULA:
						// // ��ȡ��ʽ
						// System.out.print(cell.getCellFormula() + " ");
						// break;
						// case STRING:
						// // ��ȡString
						// System.out.print(cell.getRichStringCellValue().toString() + " ");
						// break;
						// case BLANK:
						// break;
						// case ERROR:
						// break;
						// case _NONE:
						// break;
						// default:
						// break;
						// }
						// ----------------------------------------------------
					}
				}
				workbook.close();
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		} 
		
		return content.toString();
	}
	
	public static String readXLSX(String filePath) {
		StringBuilder content = null;
		
		if (filePath.endsWith(".xlsx")) {
			content = new StringBuilder();
			try {
				XSSFWorkbook workbook = new XSSFWorkbook(filePath);
				for (int sheet = 0; sheet < workbook.getNumberOfSheets(); sheet++) {
					if (null != workbook.getSheetAt(sheet)) {
						XSSFSheet aSheet = workbook.getSheetAt(sheet);
						for (int row = 0; row <= aSheet.getLastRowNum(); row++) {
							if (null != aSheet.getRow(row)) {
								XSSFRow aRow = aSheet.getRow(row);
								for (int cell = 0; cell < aRow.getLastCellNum(); cell++) {
									if (null != aRow.getCell(cell)) {
										XSSFCell aCell = aRow.getCell(cell);
										if (convertCell(aCell).length() > 0) {
											content.append(convertCell(aCell));
										}
									}
									content.append(" ");
								}
							}
						}
					}
				}
				workbook.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		return content.toString();
	}
	
	private static String convertCell(Cell cell) {
		NumberFormat formater = NumberFormat.getInstance();
		formater.setGroupingUsed(false);
		String cellValue = "";
		if (cell == null) {
			return cellValue;
		}

		switch (cell.getCellTypeEnum()) {
		case NUMERIC:
			// System.out.println(cell.getCellStyle().getDataFormat());
			if (HSSFDateUtil.isCellDateFormatted(cell)) {
				// �������ڸ�ʽ��ʱ���ʽ
				SimpleDateFormat sdf = null;
				if (cell.getCellStyle().getDataFormat() == HSSFDataFormat.getBuiltinFormat("h:mm")) {
					sdf = new SimpleDateFormat("HH:mm");
				} else {
					// ����
					sdf = new SimpleDateFormat("yyyy-MM-dd");
				}
				Date date = cell.getDateCellValue();
				cellValue = sdf.format(date);
			} else if (cell.getCellStyle().getDataFormat() == 58 || cell.getCellStyle().getDataFormat() == 31) {
				// �����Զ������ڸ�ʽ��m��d��(ͨ���жϵ�Ԫ��ĸ�ʽid�����id��ֵ��58)
				SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
				double value = cell.getNumericCellValue();
				Date date = org.apache.poi.ss.usermodel.DateUtil.getJavaDate(value);
				cellValue = sdf.format(date);
			} else {
				// ��������
				cellValue = formater.format(cell.getNumericCellValue());
			}
			break;
		case STRING:
			cellValue = cell.getStringCellValue();
			break;
		case BLANK:
			cellValue = cell.getStringCellValue();
			break;
		case BOOLEAN:
			cellValue = Boolean.valueOf(cell.getBooleanCellValue()).toString();
			break;
		case ERROR:
			cellValue = String.valueOf(cell.getErrorCellValue());
			break;
		case FORMULA:
			cellValue = cell.getCellFormula();
			break;
		default:
			cellValue = "";
		}
		return cellValue.trim();
	}

	public static void main(String[] args) throws Exception {
		String filePath = "E:\\15������.xls";
		String filePath1 = "E:\\2�ҵ��ղؼ�\\C�̴�С��¼.xlsx";
		String filePath2 = "E:\\1.xlsx";
		System.out.println(Excle.readXLS(filePath1));
		// System.out.println(xls.extractorXLSX(filePath1));
	}
}
