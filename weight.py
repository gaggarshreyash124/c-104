import csv 
import statistics
import pandas as pd

df = pd.read_csv("height-weight.csv")
weightlist = df["Weight(Pounds)"].to_list()

weightmean = statistics.mean(weightlist)
print(weightmean)

weightmedian = statistics.median(weightlist)
print(weightmedian)

weightmode = statistics.mode(weightlist)
print(weightmode)

standarddiviation = statistics.stdev(weightlist)
print(standarddiviation)

weightfirstsdstart,weightfirstsdend = weightmean - standarddiviation,weightmean + standarddiviation

weightsecondsdstart,weightsecondsdend = weightmean - (2*standarddiviation),weightmean + (2*standarddiviation)

weightthirdsdstart,weightthirdsdend = weightmean - (3*standarddiviation),weightmean + (3*standarddiviation)

data1 = [result for result in weightlist if result > weightfirstsdstart and result < weightfirstsdend]
data2 = [result for result in weightlist if result > weightsecondsdstart and result < weightsecondsdend]
data3 = [result for result in weightlist if result > weightthirdsdstart and result < weightthirdsdend]

print("{}% of data for hieght lice within firststandarddiviation".format(len(data1)*100/len(weightlist)))
print("{}% of data for hieght lice within secondstandarddiviation".format(len(data2)*100/len(weightlist)))
print("{}% of data for hieght lice within thirdstandarddiviation".format(len(data3)*100/len(weightlist)))