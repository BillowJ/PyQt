# Python 3.7
# Designed by BillowJ

from pyecharts.charts import Bar
import pyecharts.options as opts
import os, time
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

    # 正则提取数据
    def ReHelper(self, str):
        price = re.findall('\d+', str)[0]
        return int(price)

    #
    def CsvHandle(self):
        dic1 = {}
        with open(self.DataFile) as CsvFile:
            CsvFileReader = csv.reader(CsvFile)
            header_row = next(CsvFileReader)
            for row in CsvFileReader:
                # 各个地区
                location_ = row[4]
                if location_ in dic1:
                    price_ = self.ReHelper(row[2])
                    area_  = self.ReHelper(row[3])
                    dic1[row[4]][0] += price_
                    dic1[row[4]][1] += area_
                    if dic1[row[4]][2] < price_:
                        dic1[row[4]][2] = price_
                    if dic1[row[4]][3] > price_ :
                        dic1[row[4]][3] = price_
                else :
                    # row[4] 地区
                    # 房租价格
                    finalPrice = self.ReHelper(row[2])
                    dic1.setdefault(row[4], []).append(finalPrice)
                    # 租房面积大小
                    finalArea = self.ReHelper(row[3])
                    dic1.setdefault(row[4], []).append(finalArea)
                    # 最高租金
                    dic1.setdefault(row[4], []).append(finalPrice)
                    # 最低租金
                    dic1.setdefault(row[4], []).append(finalPrice)
        return dic1

    def Graphing(self):
        x_vals = []
        y_avgs = []
        y_mins = []
        y_maxs = []
        for item in self.dic:
            x_vals.append(item)
            # 保留2位小数
            y_avgs.append(round((self.dic[item][0])/(self.dic[item][1]), 2))
            y_maxs.append(self.dic[item][2])
            y_mins.append(self.dic[item][3])
        bar = (
            Bar()
            .add_xaxis(x_vals)
            .add_yaxis('均价', y_avgs)
            .add_yaxis('最大值', y_maxs)
            .add_yaxis('最小值', y_mins)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True, font_size=14),
                             markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(y=40, name="价格线=40")]))
            .set_global_opts(title_opts=opts.TitleOpts(title='柱状图示例-租金', subtitle='三个指标'),
                             xaxis_opts=opts.AxisOpts(name='租金'),
                             yaxis_opts=opts.AxisOpts(name='单位:¥'))
        )
        curPath = os.getcwd().replace('\\', '/')
        # curTime = time.strftime("%Y_%m_%d", time.localtime(time.time()))
        file_ = re.findall("([^/]*)(\\.\\w+)$", self.DataFile)
        print(file_[0][0][5:])
        Time = file_[0][0][5:]
        FileName = curPath + "/DATA_{}.html".format(Time)
        self.FinalDataFilePath = FileName
        bar.render(FileName)
    # 继承实现接口
    def analyzeData(self):
        file_ = re.findall("([^/]*)(\\.\\w+)$", self.DataFile)
        file_ = os.getcwd().replace('\\', '/') + file_[0][0] + ".html"
        print(file_)
        if os.path.exists(file_):
            return file_

        # 处理给定的数据文件
        self.dic = self.CsvHandle()
        self.Graphing()
        return self.FinalDataFilePath