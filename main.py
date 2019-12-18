import numpy as np
import pandas as pd
import zystock as zys


if __name__ == '__main__':
    stock = zys.Stock('600019')
    stock.calculateIndex()
    stock.saveStockData('./data/dataWithIndex/600019.csv')
