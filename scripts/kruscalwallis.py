# IMPORTS
import pandas as pd 
from scipy import stats
import numpy as np


#FILES
dataset = pd.read_csv("../Statistics_Final/nasa_and_sus.csv",sep=";")
f = open("outputs_kruscal.txt","w")

#LISTS
sus_1_junior = []
sus_2_junior = []
nasa_1_junior = []
nasa_2_junior = []

sus_1_intern = []
sus_2_intern = []
nasa_1_intern = []
nasa_2_intern = []


sus_1_senior = []
sus_2_senior = []
nasa_1_senior = []
nasa_2_senior = []

#DIVIDE INFORMATION
for c, r in dataset.iterrows():
    #print("c: " + str(c))
    #print("r: " + str(r))
    if(r["Experience"]=="Junior"):
        sus_1_junior = sus_1_junior + [r["SUS_Option1"]]
        sus_2_junior = sus_2_junior + [r["SUS_Option2"]]
        nasa_1_junior = nasa_1_junior + [r["NASA_Option1"]]
        nasa_2_junior = nasa_2_junior + [r["NASA_Option2"]]


    elif(r["Experience"]=="Intern"):
        sus_1_intern = sus_1_intern + [r["SUS_Option1"]]
        sus_2_intern = sus_2_intern + [r["SUS_Option2"]]
        nasa_1_intern = nasa_1_intern + [r["NASA_Option1"]]
        nasa_2_intern = nasa_2_intern + [r["NASA_Option2"]]


    elif(r["Experience"]=="Senior"):
        sus_1_senior = sus_1_senior + [r["SUS_Option1"]]
        sus_2_senior = sus_2_senior + [r["SUS_Option2"]]
        nasa_1_senior = nasa_1_senior + [r["NASA_Option1"]]
        nasa_2_senior = nasa_2_senior + [r["NASA_Option2"]]

sus_kw1 = stats.kruskal(sus_1_junior, sus_1_intern, sus_1_senior)
sus_kw2 = stats.kruskal(sus_2_junior, sus_2_intern, sus_2_senior)
nasa_kw1 = stats.kruskal(nasa_1_junior, nasa_1_intern, nasa_1_senior)
nasa_kw2 = stats.kruskal(nasa_2_junior, nasa_2_intern, nasa_2_senior)


sus_c1 =  len(sus_1_junior) + len(sus_1_intern) + len(sus_1_senior) 
sus_c2 =  len(sus_2_junior) + len(sus_2_intern) + len(sus_2_senior) 
nasa_c1 =  len(nasa_1_junior) + len(nasa_1_intern) + len(nasa_1_senior) 
nasa_c2 =  len(nasa_2_junior) + len(nasa_2_intern) + len(nasa_2_senior) 


sus_chi1 = stats.chi2.ppf(1-.05, df=sus_c1-1)
sus_chi2 = stats.chi2.ppf(1-.05, df=sus_c2-1)
nasa_chi1 = stats.chi2.ppf(1-.05, df=nasa_c1-1)
nasa_chi2 = stats.chi2.ppf(1-.05, df=nasa_c2-1)


f.write("For the  critical chi-square value:\nDegrees of freedom = c-1, alpha = 0.05\n\n")

f.write("If the critical chi-square value is less than the H statistic, reject the null hypothesis that the medians are equal.\n\n")
f.write("If the chi-square value is not less than the H statistic, there is not enough evidence to suggest that the medians are unequal.\n")

f.write("\nSUS UTA 9, c = " + str(sus_c1) + ", chi-square = " + str(sus_chi1) + "\n\n")
f.write(str(sus_kw1) + "\n")
f.write("\nSUS UTA 4, c = " + str(sus_c2) + ", chi-square = " + str(sus_chi2) + "\n\n")
f.write(str(sus_kw2) + "\n")
f.write("\nNASA UTA 9, c = " + str(nasa_c1) + ", chi-square = " + str(nasa_chi1) + "\n\n")
f.write(str(nasa_kw1) + "\n")
f.write("\nNASA UTA 4, c = " + str(nasa_c2) + ", chi-square = " + str(nasa_chi2) + "\n\n")
f.write(str(nasa_kw2) + "\n")


f.close()