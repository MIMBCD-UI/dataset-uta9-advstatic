# IMPORTS
import pandas as pd 
from scipy import stats
import numpy as np
import scipy.stats as stats
from statsmodels.stats.multicomp import (pairwise_tukeyhsd, MultiComparison)
import scikit_posthocs as sp

#FILES
dataset = pd.read_csv("../Statistics_Final/nasa_and_sus.csv",sep=";")
f = open("outputs_dunn.txt","w")
f_hs = open("outputs_dunn_holm_sidak.txt","w")
f_h = open("outputs_dunn_holm.txt","w")
f_bh = open("outputs_dunn_fdr_bh.txt","w")
f_b = open("outputs_dunn_bonferroni.txt","w")

f.write("#########################\n")
f.write("##    SUS UTA 9     ##\n")
f.write("#########################\n\n")
f.write(str(sp.posthoc_dunn(dataset, 
                            val_col="SUS_Option1", 
                            group_col="Experience",
                            sort=False)) 
        + "\n")

f.write("\n\n")
f.write("#########################\n")
f.write("##    SUS UTA 4     ##\n")
f.write("#########################\n\n")
f.write(str(sp.posthoc_dunn(dataset, 
                            val_col="SUS_Option2", 
                            group_col="Experience",
                            sort=False)) 
        + "\n")

f.write("\n\n")
f.write("#########################\n")
f.write("##   NASA UTA 9     ##\n")
f.write("#########################\n\n")
f.write(str(sp.posthoc_dunn(dataset, 
                            val_col="NASA_Option1", 
                            group_col="Experience",
                            sort=False)) 
        + "\n")

f.write("\n\n")
f.write("#########################\n")
f.write("##   NASA UTA 4     ##\n")
f.write("#########################\n\n")
f.write(str(sp.posthoc_dunn(dataset, 
                            val_col="NASA_Option2", 
                            group_col="Experience",
                            sort=False)) 
        + "\n")

f.close()

#--------------------------------------------------------------------------------------------

f_hs.write("#########################\n")
f_hs.write("##    SUS UTA 9     ##\n")
f_hs.write("#########################\n\n")
f_hs.write(str(sp.posthoc_dunn(dataset, 
                            val_col="SUS_Option1", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="holm-sidak")) 
        + "\n")

f_hs.write("\n\n")
f_hs.write("#########################\n")
f_hs.write("##    SUS UTA 4     ##\n")
f_hs.write("#########################\n\n")
f_hs.write(str(sp.posthoc_dunn(dataset, 
                            val_col="SUS_Option2", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="holm-sidak")) 
        + "\n")

f_hs.write("\n\n")
f_hs.write("#########################\n")
f_hs.write("##   NASA UTA 9     ##\n")
f_hs.write("#########################\n\n")
f_hs.write(str(sp.posthoc_dunn(dataset, 
                            val_col="NASA_Option1", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="holm-sidak")) 
        + "\n")

f_hs.write("\n\n")
f_hs.write("#########################\n")
f_hs.write("##   NASA UTA 4     ##\n")
f_hs.write("#########################\n\n")
f_hs.write(str(sp.posthoc_dunn(dataset, 
                            val_col="NASA_Option2", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="holm-sidak")) 
        + "\n")

f_hs.close()


#--------------------------------------------------------------------------------------------

f_bh.write("#########################\n")
f_bh.write("##    SUS UTA 9     ##\n")
f_bh.write("#########################\n\n")
f_bh.write(str(sp.posthoc_dunn(dataset, 
                            val_col="SUS_Option1", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="fdr_bh")) 
        + "\n")

f_bh.write("\n\n")
f_bh.write("#########################\n")
f_bh.write("##    SUS UTA 4     ##\n")
f_bh.write("#########################\n\n")
f_bh.write(str(sp.posthoc_dunn(dataset, 
                            val_col="SUS_Option2", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="fdr_bh")) 
        + "\n")

f_bh.write("\n\n")
f_bh.write("#########################\n")
f_bh.write("##   NASA UTA 9     ##\n")
f_bh.write("#########################\n\n")
f_bh.write(str(sp.posthoc_dunn(dataset, 
                            val_col="NASA_Option1", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="fdr_bh")) 
        + "\n")

f_bh.write("\n\n")
f_bh.write("#########################\n")
f_bh.write("##   NASA UTA 4     ##\n")
f_bh.write("#########################\n\n")
f_bh.write(str(sp.posthoc_dunn(dataset, 
                            val_col="NASA_Option2", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="fdr_bh")) 
        + "\n")


f_bh.close()

#--------------------------------------------------------------------------------------------

f_h.write("#########################\n")
f_h.write("##    SUS UTA 9     ##\n")
f_h.write("#########################\n\n")
f_h.write(str(sp.posthoc_dunn(dataset, 
                            val_col="SUS_Option1", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="holm")) 
        + "\n")

f_h.write("\n\n")
f_h.write("#########################\n")
f_h.write("##    SUS UTA 4     ##\n")
f_h.write("#########################\n\n")
f_h.write(str(sp.posthoc_dunn(dataset, 
                            val_col="SUS_Option2", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="holm")) 
        + "\n")

f_h.write("\n\n")
f_h.write("#########################\n")
f_h.write("##   NASA UTA 9     ##\n")
f_h.write("#########################\n\n")
f_h.write(str(sp.posthoc_dunn(dataset, 
                            val_col="NASA_Option1", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="holm")) 
        + "\n")

f_h.write("\n\n")
f_h.write("#########################\n")
f_h.write("##   NASA UTA 4     ##\n")
f_h.write("#########################\n\n")
f_h.write(str(sp.posthoc_dunn(dataset, 
                            val_col="NASA_Option2", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="holm")) 
        + "\n")

f_h.close()

#--------------------------------------------------------------------------------------------

f_b.write("#########################\n")
f_b.write("##    SUS UTA 9     ##\n")
f_b.write("#########################\n\n")
f_b.write(str(sp.posthoc_dunn(dataset, 
                            val_col="SUS_Option1", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="bonferroni")) 
        + "\n")

f_b.write("\n\n")
f_b.write("#########################\n")
f_b.write("##    SUS UTA 4     ##\n")
f_b.write("#########################\n\n")
f_b.write(str(sp.posthoc_dunn(dataset, 
                            val_col="SUS_Option2", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="bonferroni")) 
        + "\n")

f_b.write("\n\n")
f_b.write("#########################\n")
f_b.write("##   NASA UTA 9     ##\n")
f_b.write("#########################\n\n")
f_b.write(str(sp.posthoc_dunn(dataset, 
                            val_col="NASA_Option1", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="bonferroni")) 
        + "\n")

f_b.write("\n\n")
f_b.write("#########################\n")
f_b.write("##   NASA UTA 4     ##\n")
f_b.write("#########################\n\n")
f_b.write(str(sp.posthoc_dunn(dataset, 
                            val_col="NASA_Option2", 
                            group_col="Experience",
                            sort=False,
                            p_adjust="bonferroni")) 
        + "\n")


f_b.close()

#--------------------------------------------------------------------------------------------