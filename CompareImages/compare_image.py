from PIL import Image
from tkinter import filedialog
import os
import time

class DHash(object):
    @staticmethod
    def calculate_hash(image):
        """
        计算图片的dHash值
        :param image: PIL.Image
        :return: dHash值,string类型
        """
        difference = DHash.__difference(image)
        # 转化为16进制(每个差值为一个bit,每8bit转为一个16进制)
        decimal_value = 0
        hash_string = ""
        for index, value in enumerate(difference):
            if value:  # value为0, 不用计算, 程序优化
                decimal_value += value * (2 ** (index % 8))
            if index % 8 == 7:  # 每8位的结束
                hash_string += str(hex(decimal_value)[2:].rjust(2, "0"))  # 不足2位以0填充。0xf=>0x0f
                decimal_value = 0
        return hash_string

    @staticmethod
    def hamming_distance(first, second):
        """
        计算两张图片的汉明距离(基于dHash算法)
        :param first: Image或者dHash值(str)
        :param second: Image或者dHash值(str)
        :return: hamming distance. 值越大,说明两张图片差别越大,反之,则说明越相似
        """
        # A. dHash值计算汉明距离
        if isinstance(first, str):
            return DHash.__hamming_distance_with_hash(first, second)

        # B. image计算汉明距离
        hamming_distance = 0
        image1_difference = DHash.__difference(first)
        image2_difference = DHash.__difference(second)
        for index, img1_pix in enumerate(image1_difference):
            img2_pix = image2_difference[index]
            if img1_pix != img2_pix:
                hamming_distance += 1
        return hamming_distance

    @staticmethod
    def __difference(image):
        """
        *Private method*
        计算image的像素差值
        :param image: PIL.Image
        :return: 差值数组。0、1组成
        """
        resize_width = 9
        resize_height = 8
        # 1. resize to (9,8)
        smaller_image = image.resize((resize_width, resize_height))
        # 2. 灰度化 Grayscale
        grayscale_image = smaller_image.convert("L")
        # 3. 比较相邻像素
        pixels = list(grayscale_image.getdata())
        difference = []
        for row in range(resize_height):
            row_start_index = row * resize_width
            for col in range(resize_width - 1):
                left_pixel_index = row_start_index + col
                difference.append(pixels[left_pixel_index] > pixels[left_pixel_index + 1])
        return difference

    @staticmethod
    def __hamming_distance_with_hash(dhash1, dhash2):
        """
        *Private method*
        根据dHash值计算hamming distance
        :param dhash1: str
        :param dhash2: str
        :return: 汉明距离(int)
        """
        difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
        return bin(difference).count("1")


# 目前有三个需求
# 1. 单个图片和单个图片比较
# 2. 单个图片和某个文件夹比较
# 3. 某个文件夹和另一个文件夹比较
class CompareImage:
    def __is_same(self, image1, image2):
        """
        *Private method*
        比较两个PIL.image对象是否相同
        :param
        :image: PIL.Image
        :return: 相同不同（布尔值True，False）
        """        
        hamming_distance = DHash.hamming_distance(image1, image2)
        if hamming_distance <= 5:
            return True
        return False


    def __get_image_list(self, folderpath):
        """
        *Private method*
        获取图片绝对路径
        :param folderpath: 文件夹绝对路径 
        :return: 文件夹下所有文件的绝对路径组成的列表
        """        
        filepath_list = []
        for dirpath, subdirname_list, filename_list in os.walk(folderpath):
            for filename in filename_list:
                filepath_list.append(os.path.join(dirpath, filename))
        return filepath_list


    def __get_MyImage_list(self, folderpath):
        """
        *Private method*
        获取自定义类MyImage列表
        :param folderpath: 文件夹绝对路径 
        :return: 自定义类MyImage列表
        """           
        filepath_list = self.__get_image_list(folderpath)
        MyImage_list = []
        for filepath in filepath_list:
            myImage = MyImage(Image.open(filepath), filepath)
            MyImage_list.append(myImage)
        return MyImage_list

    
    def compare_two_images(self):
        """
        单个图片和单个图片比较
        """            
        filepath1 = filedialog.askopenfilename(initialdir=os.getcwd(),title="Please select the first file to be compared:")
        filepath2 = filedialog.askopenfilename(initialdir=os.getcwd(),title="Please select the second file to be compared:")
        image1 = Image.open(filepath1)
        image2 = Image.open(filepath2)
        print("-------result----------")
        if self.__is_same(image1, image2):
            print(filepath1 + " 与\n" + filepath2 + " 相同")
        else:
            print(filepath1 + " 与\n" + filepath2 + " 不同")


    def compare_image_with_folder(self):
        """
        单个图片和某个文件夹比较
        """               
        filepath0 = filedialog.askopenfilename(initialdir=os.getcwd(), title="Please select the first file to be compared:")
        folderpath = filedialog.askdirectory(initialdir=os.getcwd(), title="Please select a folder:")
        image0 = Image.open(filepath0)
        filepath_list = self.__get_image_list(folderpath)
        flag = False
        print("-------result----------")
        for filepath in filepath_list:
            if self.__is_same(image0, Image.open(filepath)):
                print(filepath0 + " 与\n" + filepath + " 相同\n")
                flag = True
        if flag == False:
            print(filepath0 + " 与\n文件夹 " + folderpath + " 内的所有照片均不同")


    def compare_folder_with_folder(self):
        """
        某个文件夹和另一个文件夹比较
        """           
        folderpath1 = filedialog.askdirectory(initialdir=os.getcwd(), title="Please select the first folder:")
        folderpath2 = filedialog.askdirectory(initialdir=os.getcwd(), title="Please select the second folder:")
        myImage_list1 = self.__get_MyImage_list(folderpath1)
        myImage_list2 = self.__get_MyImage_list(folderpath2)
        flag = False
        print("-------result----------")
        for myImage1 in myImage_list1:
            for myImage2 in myImage_list2:
                if self.__is_same(myImage1.image, myImage2.image):
                    print(myImage1.src + " 与\n" + myImage2.src + " 相同\n")
                    flag = True
        if flag == False:
            print(filepath0 + " 与\n文件夹" + folderpath + " 内的所有照片均不同")

class MyImage:
    def __init__(self, image, src):
        """
        构造函数，保存图片路径
        :param image: PIL.Image
        :param src: 该图片绝对路径，string类型
        """
        self.image = image
        self.src = src

class Menu:
    def __init__(self):
        self.compareImage = CompareImage()

    def process(self):
        self.show()
        choice = self.get_choice()
        self.do_choice(choice)
    
    def show(self):
        """
        显示菜单
        """
        print("Please choose one function below：")
        print("1. compare one image with the other")
        print("2. compare one image with images in a folder")
        print("3. compare images in a folder with the others in another folder")


    def get_choice(self):
        choice = input("Please make your choice:")
        return choice

    def do_choice(self, choice):
        if int(choice) == 1:
            self.compareImage.compare_two_images()
        elif int(choice) == 2:
            self.compareImage.compare_image_with_folder()
        elif int(choice) == 3:
            self.compareImage.compare_folder_with_folder()
        

if __name__ == "__main__":
    start_time = time.time()
    menu = Menu()
    menu.process()
    end_time = time.time()
    print("程序耗时"+ str(end_time - start_time) +"秒")

