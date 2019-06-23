package file.search;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.io.*;
import file.content.Content;

public class SearchKeyWord extends JFrame {
	private static final long serialVersionUID = 1L;
	
	private JLabel hintLabel;
	private JButton selectButton;
	private JTextField inputKeywordField;
	
	public SearchKeyWord() {
		// TODO Auto-generated constructor stub
		super("Search Keyword");
		
		hintLabel = new JLabel("Please Input Keyword");
		inputKeywordField = new JTextField(10);
		selectButton = new JButton("Choose Folder");
		
		JPanel upJPanel = new JPanel();
		JPanel downJPanel = new JPanel();
		
		upJPanel.setLayout(new FlowLayout());
		upJPanel.add(hintLabel);
		upJPanel.add(inputKeywordField);
		
		downJPanel.add(selectButton);
		
		Container container = getContentPane();
		container.setLayout(new BorderLayout());
		container.add(upJPanel, BorderLayout.NORTH);
		container.add(downJPanel, BorderLayout.SOUTH);
		
		selectButton.addMouseListener(new FileChooser());
		
		setVisible(true);
		setLocationRelativeTo(null);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		pack();
	}
	
	public static void main(String[] args) {
		SearchKeyWord searchKeyWord = new SearchKeyWord();
	}
	
	
	class FileChooser extends MouseAdapter {
		private String keyword;
		
		public void mouseClicked(MouseEvent event) {
//			super.mouseClicked(event);
			JFileChooser chooser = new JFileChooser();
//			chooser.setMultiSelectionEnabled(true); //���ö�ѡ����ȡѡ����ļ�ʱ��ʹ��File[] files = chooser.getSelectedFiles();
			chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY); // ѡ���ļ���

			chooser.showOpenDialog(null);
			
			this.keyword = inputKeywordField.getText();
			
			try {
				long beginTime = System.currentTimeMillis();
				String filePath = chooser.getSelectedFile().getAbsolutePath();

				chooser.setCurrentDirectory(new File(filePath)); // ����ʱ�ԡ������ļ�ѡȡ��Ĭ��·��Ϊ�ϴδ�·�� chooser������ȫ�ֶ���
				
				getSubFile(filePath);

				long endTime = System.currentTimeMillis();
				System.out.println("��ʱ��" + (endTime - beginTime) + "ms");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (NullPointerException e) {
				// TODO: handle exception
				e.printStackTrace();
			}
		}
		
		public void getSubFile(String filePath) throws IOException {   // �������ļ��е��ļ�
			// System.out.println("����getSubFile");

			// ��Ҫ�ж������Ƿ�������Ŀ¼������������
			File dir = new File(filePath);

			//--------------------------------------------------------------
			File[] listFiles = dir.listFiles();
			for (int i = 0; i < listFiles.length; i++) {
				if (listFiles[i].isDirectory()) {
					getSubFile(listFiles[i].getAbsolutePath());
				} else {
					searchFile(listFiles[i], this.keyword);
				}
			}
		}
		
		public void searchFile(File file, String keyWord) {
			String filePath = file.getAbsolutePath();
			String fileContent = Content.getContent(filePath);
			
			if (fileContent != null && fileContent.indexOf(keyWord) > 0) {
				System.out.println(filePath);
			}
		}
	}
}