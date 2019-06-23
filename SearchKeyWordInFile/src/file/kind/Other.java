package file.kind;

import java.io.FileReader;
import java.io.IOException;
import java.io.LineNumberReader;

public class Other {
	public static String getContent(String filePath) {
		String content = null;
		LineNumberReader lineNumberReader = null;
		
		try {
			lineNumberReader = new LineNumberReader(new FileReader(filePath));
			String line = null;
			while ((line = lineNumberReader.readLine()) != null) {
//				System.out.println(line);
				content += lineNumberReader.readLine() + "\n";
			}
		} catch (IOException e) {
			// TODO: handle exception
			e.printStackTrace();
		} finally {
			// ¹Ø±ÕlineNumberReader
			try {
				if (lineNumberReader != null) {
					lineNumberReader.close();
				}
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
		
		return content;
	}
}
