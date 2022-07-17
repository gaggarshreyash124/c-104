from base64 import standard_b64decode
import csv 
import statistics
import pandas as pd

df = pd.read_csv("height-weight.csv")
heightlist = df["Height(Inches)"].to_list()

heightmean = statistics.mean(heightlist)
print(heightmean)

heightmedian = statistics.median(heightlist)
print(heightmedian)

heightmode = statistics.mode(heightlist)
print(heightmode)

standarddiviation = statistics.stdev(heightlist)
print(standarddiviation)

heightfirstsdstart,heightfirstsdend = heightmean - standarddiviation,heightmean + standarddiviation

heightsecondsdstart,heightsecondsdend = heightmean - (2*standarddiviation),heightmean + (2*standarddiviation)

heightthirdsdstart,heightthirdsdend = heightmean - (3*standarddiviation),heightmean + (3*standarddiviation)

data1 = [result for result in heightlist if result > heightfirstsdstart and result < heightfirstsdend]
data2 = [result for result in heightlist if result > heightsecondsdstart and result < heightsecondsdend]
data3 = [result for result in heightlist if result > heightthirdsdstart and result < heightthirdsdend]

print("{}% of data for hieght lice within firststandarddiviation".format(len(data1)*100/len(heightlist)))
print("{}% of data for hieght lice within secondstandarddiviation".format(len(data2)*100/len(heightlist)))
print("{}% of data for hieght lice within thirdstandarddiviation".format(len(data3)*100/len(heightlist)))

