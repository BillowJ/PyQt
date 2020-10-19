import  csv
import  re
dic = {}

def ReHelper(str):
        price = re.findall('\d+', str)[0]
        return int(price)


with open("E:/Diplomat_Project/MyProject/pac/RunTo/DATA_2020_09_04.csv") as CsvFile:
    CsvFileReader = csv.reader(CsvFile)
    header_row = next(CsvFileReader)
    for row in CsvFileReader:
        print(row[3], '===========\n')
        location_ = row[4]
        if location_ in dic:
            print("exist")
            # n0_ = int(row[4][0])
            # n1_ = int(row[4][1])
            # print(n0_, type(n0_))
            # print(n1_, type(n1_))
            dic[row[4]][0] += ReHelper(row[2])
            dic[row[4]][1] += ReHelper(row[3])
        else:
            # row[4] 地区
            # 房租价格
            finalPrice = ReHelper(row[2])
            print('finalPrice: %d', finalPrice)
            dic.setdefault(row[4], []).append(finalPrice)
            # 租房面积大小
            finalArea = ReHelper(row[3])
            dic.setdefault(row[4], []).append(finalArea)
            print('finalAre: %s', finalArea)
            print(dic[row[4]])


print(dic)
for val in enumerate(dic):
    print( "values: ", val)

for val in dic:
    print("val: ", val)
    print("val val: ", dic[val])

file = "E:/Diplomat_Project/MyProject/pac/RunTo/DATA_2020_09_05.csv"
file_ = re.findall("([^/]*)(\\.\\w+)$", file)
print(file_[0][0])
# E:/Diplomat_Project/MyProject/pac/RunTo/DATA_2020_10_05.html
print(100/3)
