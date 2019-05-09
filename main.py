import numpy as np
import pandas as pd
from StockData import Stock
from utils import IndexCalculator
from GlobalParams import *


if __name__ == '__main__':
    stock = Stock('600019')
    print(stock.data)
    indexcalc = IndexCalculator()
    stockdata = indexcalc.PickIndexs(stock.data, PICKINDEXLIST)
    print(stockdata)
