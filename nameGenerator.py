import sys
import random
import re
import time

class WhoManager():  #用于分配民族、省份，更加准确的定义一个人的信息（他是谁）
    def __init__(self):
        self.__province_file = r".\material\province.txt"
        self.__nation_file = r".\material\\nation.txt"

        self.__nation = []  #用于保存从文件中读取出来的各个少数民族
        self.__maxNation = ['汉族']
        self.__province = [] #用于保存从文件中读取出来的各个省份
        
    def __read_from_file(self, filename):  #从文件中读取需要生成的数据
        strlist = []
        with open(filename, "r") as f:
            for line in f.readlines():
                linestr = line.strip('\n')
                linestrlist = re.split('[，、 +]', linestr)
                strlist.extend(linestrlist)
        return strlist

    def __get_random_province(self):  #生成省份
        return random.choice(self.__province)

    def __get_random_nation(self):  #生成民族，考虑汉族比重更大，大概为92%
        chance = random.random()  #随机生成一个[0,1)间的数，小数点后有好多好多位
        if chance < 0.92:
            return self.__maxNation[0]
        return random.choice(self.__nation)
        

    def generate_where(self):
        self.__province = self.__read_from_file(self.__province_file)
        self.__nation = self.__read_from_file(self.__nation_file)

        Province = self.__get_random_province()
        Nation = self.__get_random_nation()

        return Province, Nation



class IDManager():    #用于分配学生的学号，学号信息包括学院，年级，班级等。同时生成出生日期
    def __init__(self):
        self.__existed_id_file = r".\record\IDPool.txt"
        #self.__full_file = r".\record\Full.txt"  #此文件路径用于保存分配人数已满的班级
        self.__sno = []             #字符串，模仿吉林大学教学号前两位生成学生学号开头前两位列表
        self.__grade = []           #整型，模仿吉林大学现有年级
        self.__class = []           #字符串，模仿吉林大学班级数15个班
        self.__num = []             #字符串，模仿吉林大学软件学院每个班平均30人
        self.__idPool = []          #形成一个学号池，避免重复
        self.__newID = []           #记录新生成学号，程序结束时将其写入文件中
        self.__full = []

        self.__date1 = (1994,1,1,0,0,0,0,0,0)  #设置最早出生日期时间元组（1994-01-01 00：00：00）
        self.__date2 = (2002,12,31,23,59,59,0,0,0)  #设置最晚出生日期时间元组（2002-12-31 23：59：59）
        self.__start = time.mktime(self.__date1) #生成开始时间戳
        self.__end = time.mktime(self.__date2)   #生成结束时间戳
        self.__date = ''                      #记录每次生成的生日

        self.__idPool = self.__get_existed_info(self.__existed_id_file)  #从文件中读取出已经分配过的ID
        self.__generate_basic_info()
        self.__full = self.__get_existed_info(self.__full_file)  


    def __generate_basic_info(self):  #可以产生143800个学号，也就是143800个数据
        for i in range(1, 10):  #生成学号
            for j in range(1, 10):
                self.__sno.append(str(i*10+j))

        for i in range(2014, 2018):  #现在有2014级~2017级
            self.__grade.append(i)

        for i in range(1, 16):  #生成班级
            if i < 10:
                self.__class.append(('0'+str(i)))
            else:
                self.__class.append(str(i))

        for i in range(1, 31):  #生成班级人数
            if i < 10:
                self.__num.append(('0'+str(i)))
            else:
                self.__num.append(str(i))
                

    def __get_existed_info(self,filename):  #从文件中读取已经存在了的学号
        strlist = []
        with open(filename, "r") as f:
            for line in f.readlines():
                linestr = line.strip('\n')
                linestrlist = re.split('[、 +]', linestr)
                strlist.extend(linestrlist)
        return strlist
                

    def __generate_birthday(self):  #值得注意的是出生日期和年级有很大的关系，所以为了方便，先产生出生日期，再限定生成年级
        t = random.randint(self.__start,self.__end)  #在开始时间戳和结束时间戳中随机取出一个
        date_touple=time.localtime(t)  #将时间戳生成时间元组
        self.__date = time.strftime("%Y-%m-%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）

    def __get_random_sno(self):
        return random.choice(self.__sno)

    def __get_random_grade(self):
        year = re.split(r'[-]', self.__date)  #通过出生日期如1997-03-20获取出生年份
        Grade = random.choice(self.__grade)
        while (Grade-int(year[0])) < 15 or (Grade-int(year[0])) > 20: #判断生成的年级是否合法，我们认为15~20岁才上大学都是可以的
            Grade = random.choice(self.__grade)
        
        return Grade
    
    def __get_random_class(self):
        return random.choice(self.__class)

    def __get_random_num(self):
        return random.choice(self.__num)

    def generate_id(self):
        self.__generate_birthday()


        newId = random.randint(10000000000,99999999999)

        while newId in self.__idPool:
            newId = random.randint(10000000000,99999999999)

        self.__idPool.append(newId)
        self.__newID.append(newId)
        return newId, self.__date

    def write_id_into_file(self,filename):
        with open(filename, "a") as f:
            for ID in self.__newID:
                f.write(str(ID)+'\n')


class GenetateInfo():
    def __init__(self, n):
        self.__surname_file = r".\material\surname.txt"   #存有姓的文件路径
        self.__male_file = r".\material\male.txt"         #存有男生名的路径
        self.__female_file = r".\material\female.txt"     #存有女生名的路径
        self.__fullname_file = r".\result\result.txt"     #将生成的名字存入的文件路径
        self.__existed_id_file = r".\record\IDPool.txt"

        self.__surname = []  #用于保存从文件读出来的姓
        self.__malename = []  #用于保存从文件读出来的男生名
        self.__femalename = [] #用于保存从文件读出来的女生名

        self.__sex = ['女', '男']

        self.__Idmanager = IDManager()
        self.__who = WhoManager()

        self.infoNum = n            #想要生成的信息个数

    
    def __read_from_file(self, filename):  #从文件中读取需要生成的数据
        strlist = []
        with open(filename, "r") as f:
            for line in f.readlines():
                linestr = line.strip('\n')
                linestrlist = re.split('[、 +]', linestr)
                strlist.extend(linestrlist)
        return strlist  #返回值是一个列表，形如["一","二","三","四","五","六"]

    def __generate_score(self):              #按比例生成分数
        chance = random.random()
        if chance < 0.03:
            score = random.uniform(0, 59)
        elif chance < 0.1:
            score = random.uniform(90, 100)
        elif chance < 0.3:
            score = random.uniform(60, 69)
        elif chance < 0.7:
            score = random.uniform(70, 79)
        else:
            score = random.uniform(80, 89)
        return score

    def __generate_class(self):
        return random.randint(1,10)


    def __write_into_file(self, filename):  #里面带的randint可以考虑改进为random.choice，这样看起来会不会更简单？
        #这个函数再拆分为两个函数应该更好，一个函数专门获取数据，一个函数将数据写入文件
        with open(filename,"a") as f:
            count = 0
            for i in range(int(self.infoNum)):           #生成信息
                full_name= ''
                num1 = random.randint(0,len(self.__surname)-1)   #生成一个随机数，随机选取一个姓
                sexJudge = random.randint(0,1)  #生成一个随机数表示性别，0代表女，1代表男
                if sexJudge:
                    num2 = random.randint(0,len(self.__malename)-1)    #生成一个随机数，随机选取一个男名
                    full_name = (self.__surname[num1]+self.__malename[num2])          #合成姓名
                else:
                    num2 = random.randint(0,len(self.__femalename)-1)   #生成一个随机数，随机选取一个女名
                    full_name = (self.__surname[num1]+self.__femalename[num2])          #合成姓名

                ID = self.__Idmanager.generate_id()  #生成一个学号以及出生日期  ID[0]是学号 ID[1]是出生日期
                where = self.__who.generate_where()   #生成省份和民族  where[0]是省份  where[1]是民族
                clas = self.__generate_class()
                score = self.__generate_score()

                #以“姓名，性别，学号，班级，出生日期，省份，民族”顺序
                f.write(full_name+' '+self.__sex[sexJudge] + ' '+str(ID[0])+ ' '+str(clas)+' '+str(ID[1])+' '+where[0]+' '+where[1])
                f.write('\n')

                count += 1
                self.record_time(count)

                

    def generate(self):
        self.__surname = self.__read_from_file(self.__surname_file)
        self.__malename = self.__read_from_file(self.__male_file)
        self.__femalename = self.__read_from_file(self.__female_file)
        print(len(self.__surname))
        print(len(self.__malename))
        print(len(self.__femalename))

        self.__write_into_file(self.__fullname_file)

        self.__Idmanager.write_id_into_file(self.__existed_id_file)


    def record_time(self, count):
        if count ==100:
            end = time.clock()
            print('100个数据耗时'+str(end-start))
        elif count == 1000:
            end = time.clock()
            print('1000个数据耗时'+str(end-start))
        elif count == 10000:
            end = time.clock()
            print('10000个数据耗时'+str(end-start))
        elif count == 30000:
            end = time.clock()
            print('30000个数据耗时'+str(end-start))
        elif count == 40000:
            end = time.clock()
            print('40000个数据耗时'+str(end-start))
        elif count == 50000:
            end = time.clock()
            print('50000个数据耗时'+str(end-start))
        elif count == 60000:
            end = time.clock()
            print('60000个数据耗时'+str(end-start))
        elif count == 70000:
            end = time.clock()
            print('70000个数据耗时'+str(end-start))
        elif count == 80000:
            end = time.clock()
            print('80000个数据耗时'+str(end-start))
        elif count == 90000:
            end = time.clock()
            print('90000个数据耗时'+str(end-start))
        elif count == 100000:
            end = time.clock()
            print('100000个数据耗时'+str(end-start))
        elif count == 130000:
            end = time.clock()
            print('130000个数据耗时'+str(end-start))

        

if __name__ == '__main__':
    count = input("Please input the number of information you want to generate:")
    start = time.clock()
    info = GenetateInfo(count)
    info.generate()
    end = time.clock()
    print("程序运行"+str(end-start))
