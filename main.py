import numpy as np
import pandas as pd
import zystock as zys


if __name__ == '__main__':
    stock = zys.Stock('600019')
    print(stock.data)
    indexcalc = zys.IndexCalculator()
    stockdata = indexcalc.PickIndexs(stock.data, zys.PICKINDEXLIST)
    print(stockdata)
