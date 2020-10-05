# Python 3.7
# Designed by BillowJ

from pyecharts.charts import Bar
import csv
import re
import pandas as pd
#基类
class DiagramMaker:
    def __init__(self, DataFile):
        self.DataFile = DataFile
        # 图表文件地址
        self.FinalDataFilePath = ''
    def analyzeData(self):
        pass
    def get(self):
        # print("this is get function")
        return self.FinalDataFilePath

# 扇形图类
class SectorDiagramMaker(DiagramMaker):
    def __init__(self, DataFile):
        super().__init__(DataFile)
        # super(DiagramMaker, self).__init__(DataFile)
        self.analyzeData()

        self.dic = {}
    def ReHelper(self, str):
        price = re.findall('\d+', str)[0]
        return int(price)
    # 继承实现接口
    def analyzeData(self):
        # df = pd.read_csv(self.DataFile, encoding='gbk')
        # print("打开Excel文件成功？")
        dic1 = { }
        with open(self.DataFile) as CsvFile:
            CsvFileReader = csv.reader(CsvFile)
            header_row = next(CsvFileReader)

            for row in CsvFileReader:
                print(row[4])
                location_ = row[4]
                if location_ in dic1:
                    print("exist")
                    dic1[row[4]][0] += self.ReHelper(row[2])
                    dic1[row[4]][1] += self.ReHelper(row[3])
                else :
                    # row[4] 地区
                    # 房租价格
                    finalPrice = self.ReHelper(row[2])
                    print('finalPrice: %d', finalPrice)
                    dic1.setdefault(row[4], []).append(finalPrice)
                    # 租房面积大小
                    finalArea = self.ReHelper(row[3])
                    dic1.setdefault(row[4], []).append(finalArea)
                    print('finalAre: %s', finalArea)

        print(dic1)