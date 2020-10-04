# Python 3.7
# Designed by BillowJ

from pyecharts.charts import Bar
import csv
import pandas as pd
#基类
class DiagramMaker:
    def __init__(self, DataFile):
        self.DataFile = DataFile
        self.FinalDataFilePath = ''
    def analyzeData(self):
        pass
    def get(self):
        # print("this is get function")
        return self.FinalDataFilePath

#扇形图类
class SectorDiagramMaker(DiagramMaker):
    def __init__(self, DataFile):
        super().__init__(DataFile)
        # super(DiagramMaker, self).__init__(DataFile)
        self.analyzeData()
    #继承实现接口
    def analyzeData(self):
        df = pd.read_csv(self.DataFile, encoding='gbk')
        print("打开Excel文件成功？")
        keys = []
        print(df)
        mean_df = df['晋安区'].mean()
        # for row in df[1:]:
        #     if row[4] not in keys:
        #         keys.append(row[4])
        print(keys)
        # '''
        # with open(self.DataFile) as CsvFile:
        #     CsvFileReader = csv.reader(CsvFile)
        #     header_row = next(CsvFileReader)
        #     df = pd.DataFrame(header_row)
        #     print(df['仓山区'].mean())
        #     keys = []
        #     for index, column_header in enumerate(header_row):
        #         print(index, column_header)
        #
        #     for row in CsvFileReader:
        #         # X轴：不同区市
        #         keys[row[4]] += row[2]
        #
        #     print(keys)
        #     self.FinalDataFilePath = 'xxx'
        #
        # '''
