import numpy as np
import pandas as pd
from .GlobalParams import *
from urllib import request
from .utils import *
import os

class Stock(object):
    def __init__(self, stockid):
        self.id = stockid
        self.stock_url0 = 'http://quotes.money.163.com/service/chddata.html?code=0{}'
        self.stock_url1 = 'http://quotes.money.163.com/service/chddata.html?code=1{}'
        self.data = self._UrlGetAndOpen()
        self._CleanAndRename()
        self._ltszbugprocess()
        self._isNone_process()

    def _UrlGetAndOpen(self):
        if self.id[0] == '6':
            url = self.stock_url0.format(self.id)
        elif self.id[0] in ['0','3']:
            url = self.stock_url1.format(self.id)
        else:
            url = None
        req = request.Request(url)
        req.add_header = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 ' \
                         '(KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 ' \
                         'SE 2.X MetaSr 1.0'
        data = request.urlopen(req).read().decode('gbk')
        if len(data) <= 67:
            self.fname = None
            print('{} download failed'.format(url))
        else:
            self.fname = os.path.join(STOCKDATASAVEDIR, '{}.csv'.format(self.id))
            with open(self.fname, 'a') as f:
                f.write(data)
            print('{} download successed, save at {}'.format(url, self.fname))
            data = pd.read_csv(self.fname)
        return data

    def _CleanAndRename(self):
        '''
        Rename index and clean useless index
        '''
        data = self.data
        rm_col_list = ['股票代码','名称','成交笔数']
        new_colname = {'日期':'date', '收盘价':'close', '最高价':'high', \
                       '最低价':'low', '开盘价':'open', '前收盘':'qsp', \
                       '涨跌额':'zdy', '涨跌幅':'rate', '换手率':'hsl', \
                       '成交量':'cjl', '成交金额':'cjje', '总市值':'zsz', \
                       '流通市值':'ltsz'}
        for rm_col in rm_col_list:
            data = data.drop(rm_col, axis=1)
        data = data.rename(columns= new_colname)
        self.data = data

    def _ltszbugprocess(self):
        d = self.data['ltsz']
        d2 = d.isin(['流通市值'])
        rep_begin = d2[d2 == True].index.tolist()
        if len(rep_begin) == 0:
            pass
        else:
            self.data = self.data.loc[0:rep_begin[0]-1,:]

    def _isNone_process(self):
        data = self.data
        colname_list = ['close','high','low','open','qsp','zdy','rate','hsl', \
                        'cjl','cjje','zsz','ltsz']
        for colname in colname_list:
            d = data[colname]
            data[colname] = d.where(~d.isin(['None']),0)
            data[colname] = data[colname].astype('float')
        self.data = data

if __name__ == '__main__':
    stock = Stock('600019')
    indexcalc = IndexCalculator()
    stock = indexcalc.PickIndexs(stock.data, PICKINDEXLIST)
    print(stock)

