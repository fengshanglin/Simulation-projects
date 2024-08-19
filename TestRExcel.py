# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# f = open(".\\TestExcels.xlsx",mode="rb")
# TesCSV = pd.read_csv("./TestExcels.xlsx",encoding="gb18030")
TesCSV = pd.read_excel("./TestExcels.xlsx",header=None,index_col=0)

# output
TesCSV.to_excel("./TestExcels01.xlsx",sheet_name="sheet1")

if __name__ == "__main__":
    print("Test")
