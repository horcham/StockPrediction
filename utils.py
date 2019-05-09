import pandas as pd
import numpy as np
from GlobalParams import *

class IndexCalculator():
    def __init__(self):
        self.allindexlist = ['MA3', 'MA5', 'MA6', 'MA10', 'MA12', 'MA20', \
                     'MA24', 'MA30', 'MA50', 'MTM12', 'MTM12MA6', \
                     'DDD', 'DMA_AMA10', 'BBI', 'BOLL', 'STD', \
                     'BOLL_UP', 'BOLL_LOWER', 'IFUPPSY', 'PSY', \
                     'PSYMA6', 'EMA12', 'EMA26', 'DIF', 'DEA', \
                     'MACD']

    def _ma3_data(self, closed):
        close_len = closed.shape[0]
        ma3 = np.zeros([close_len])
        for i in range(0, close_len-2, 1):
            ma3[i] = ((sum(closed[i:(i+3)]))/3)
        return ma3
    def _ma5_data(self, closed):
        close_len = closed.shape[0]
        ma5 = np.zeros([close_len])
        for i in range(0, close_len-4, 1):
            ma5[i] = ((sum(closed[i:(i+5)]))/5)
        return ma5
    def _ma6_data(self, closed):
        close_len = closed.shape[0]
        ma6 = np.zeros([close_len])
        for i in range(0, close_len-5, 1):
            ma6[i] = ((sum(closed[i:(i+6)]))/6)
        return ma6
    def _ma10_data(self, closed):
        close_len = closed.shape[0]
        ma10 = np.zeros([close_len])
        for i in range(0, close_len-9, 1):
            ma10[i] = ((sum(closed[i:(i+10)]))/10)
        return ma10
    def _ma12_data(self, closed):
        close_len = closed.shape[0]
        ma12 = np.zeros([close_len])
        for i in range(0, close_len-11, 1):
            ma12[i] = ((sum(closed[i:(i+12)]))/12)
        return ma12
    def _ma20_data(self, closed):
        close_len = closed.shape[0]
        ma20 = np.zeros([close_len])
        for i in range(0, close_len-19, 1):
            ma20[i] = ((sum(closed[i:(i+20)]))/20)
        return ma20
    def _ma24_data(self, closed):
        close_len = closed.shape[0]
        ma24 = np.zeros([close_len])
        for i in range(0, close_len-23, 1):
            ma24[i] = ((sum(closed[i:(i+24)]))/24)
        return ma24
    def _ma30_data(self, closed):
        close_len = closed.shape[0]
        ma30 = np.zeros([close_len])
        for i in range(0, close_len-29, 1):
            ma30[i] = ((sum(closed[i:(i+30)]))/30)
        return ma30
    def _ma50_data(self, closed):
        close_len = closed.shape[0]
        ma50 = np.zeros([close_len])
        for i in range(0, close_len-49, 1):
            ma50[i] = ((sum(closed[i:(i+50)]))/50)
        return ma50
    def _mtm12_data(self, closed):
        close_len = len(closed)
        mtm12 = []
        for i in range(0,  close_len - 12,  1):
            mtm12.append((closed[i]-closed[i+12]))
        while len(mtm12) != close_len:
            mtm12.append(0)
        return np.array(mtm12)
    def _mtm12ma6_data(self, mtm12, closed):
        close_len = len(closed)
        mtm12ma6 = []
        for i in range(0,  close_len - 5,  1):
            mtm12ma6.append((sum(mtm12[i:(i + 6)])) / 6)
        while len(mtm12ma6) != close_len:
            mtm12ma6.append(0)
        return np.array(mtm12ma6)
    def _DDD_data(self, ma10, ma50, closed):
        close_len = len(closed)
        DDD = []
        for i in range(0, close_len, 1):
            DDD.append(ma10[i] - ma50[i])
        while len(DDD) != close_len:
            DDD.append(0)
        return np.array(DDD)
    def _DMA_AMA10_data(self, DDD, closed):
        close_len = len(closed)
        AMA = []
        for i in range(0, close_len - 9, 1):
            AMA.append(sum(DDD[i:(i+10)]) / 10)
        while len(AMA) != close_len:
            AMA.append(0)
        return np.array(AMA)
    def _BBI_data(self, ma3, ma6, ma12, ma24, closed):
        close_len = len(closed)
        BBI = []
        for i in range(0, close_len, 1):
            BBI.append((ma3[i]+ma6[i]+ma12[i]+ma24[i]) / 4)
        return np.array(BBI)
    def _BOLL_data(self, ma20):
        return ma20
    def _std_20_data(self, closed):
        close_len = len(closed)
        std = []
        for i in range(0, close_len - 20):
            std.append((np.std(np.array(closed[i:(i+20)]))))
        while len(std) != close_len:
            std.append(0)
        return np.array(std)
    def _BOLL_UP_data(self, BOLL, std, closed):
        close_len = len(closed)
        BOLL_UP = []
        for i in range(0, close_len):
            BOLL_UP.append(BOLL[i] + 2 * std[i])
        while len(std) != close_len:
            BOLL_UP.append(0)
        return np.array(BOLL_UP)
    def _BOLL_LOWER_data(self, BOLL, std, closed):
        close_len = len(closed)
        BOLL_LOWER = []
        for i in range(0, close_len):
            BOLL_LOWER.append(BOLL[i] - 2 * std[i])
        while len(std) != close_len:
            BOLL_LOWER.append(0)
        return np.array(BOLL_LOWER)
    def _ifup_psy_data(self, rate, closed):
        ifup = []
        for i in range(0, len(closed)):
            if rate[i] > 0:
                ifup.append(1)
            else:
                ifup.append(0)
        return np.array(ifup)
    def _PSY_data(self, ifup_psy_data, closed):
        close_len = len(closed)
        PSY = []
        for i in range(0, close_len-11, 1):
            PSY.append(sum(ifup_psy_data[i:(i+12)])/12*100)
        while len(PSY) != close_len:
            PSY.append(0)
        return np.array(PSY)
    def _PSYMA6_data(self, PSY, closed):
        close_len = len(closed)
        PSYMA6 = []
        for i in range(0,  close_len - 5,  1):
            PSYMA6.append(sum(PSY[i:(i + 6)]) / 6)
        while len(PSYMA6) != close_len:
            PSYMA6.append(0)
        return np.array(PSYMA6)
    def _EMA12_data(self, closed):
        close_len = len(closed)
        EMA12_begin = closed[close_len-1]
        EMA12 = []
        while len(EMA12) != close_len-1:
            EMA12.append(0)
        EMA12.append(float(EMA12_begin))
        for i in range(close_len - 2, -1, -1):
            EMA12[i] = EMA12[i+1]*11/13 + closed[i]*2/13
        return np.array(EMA12)
    def _EMA26_data(self, closed):
        close_len = len(closed)
        EMA26_begin = closed[close_len-1]
        EMA26 = []
        while len(EMA26) != close_len-1:
            EMA26.append(0)
        EMA26.append(float(EMA26_begin))
        for i in range(close_len - 2, -1, -1):
            EMA26[i] = EMA26[i+1]*25/27 + closed[i]*2/27
        return np.array(EMA26)
    def _DIF_data(self, EMA12, EMA26, closed):
        close_len = len(closed)
        DIF = []
        for i in range(0, close_len, 1):
            DIF.append(EMA12[i] - EMA26[i])
        return np.array(DIF)
    def _DEA_data(self, DIF, closed):
        close_len = len(closed)
        DEA = []
        while len(DEA) != close_len :
            DEA.append(0)
        for i in range(close_len - 2,  -1,  -1):
            DEA[i] = DEA[i + 1] * 8 / 10 + DIF[i] * 2 / 10
        return np.array(DEA)
    def _MACD_data(self, DIF, DEA, closed):
        close_len = len(closed)
        MACD = []
        for i in range(0,close_len,1):
            MACD.append((DIF[i]-DEA[i])*2)
        return np.array(MACD)

    def _fetch_data(self,data,colname,t='series.values'):
        if t == 'series':
            return data[colname]
        elif t == 'array':
            return np.array(data[colname])
        elif t == 'series.values':
            return data[colname].values

    def _CalcAllIndexs(self, data):
        closed = self._fetch_data(data,'close',t='series.values')
        rate = self._fetch_data(data,'rate',t='series.values')
        MA3 = self._ma3_data(closed)
        MA5 = self._ma5_data(closed)
        MA6 = self._ma6_data(closed)
        MA10 = self._ma10_data(closed)
        MA12 = self._ma12_data(closed)
        MA20 = self._ma20_data(closed)
        MA24 = self._ma24_data(closed)
        MA30 = self._ma30_data(closed)
        MA50 = self._ma50_data(closed)
        MTM12 = self._mtm12_data(closed)
        MTM12MA6 = self._mtm12ma6_data(MTM12,closed)
        DDD = self._DDD_data(MA10, MA50, closed)
        DMA_AMA10 = self._DMA_AMA10_data(DDD, closed)
        BBI = self._BBI_data(MA3, MA6, MA12, MA24,closed)
        BOLL = MA20
        STD = self._std_20_data(closed)
        BOLL_UP = self._BOLL_UP_data(BOLL, STD, closed)
        BOLL_LOWER = self._BOLL_LOWER_data(BOLL, STD, closed)
        IFUPPSY = self._ifup_psy_data(rate, closed)
        PSY = self._PSY_data(IFUPPSY, closed)
        PSYMA6 = self._PSYMA6_data(PSY,closed)
        EMA12 = self._EMA12_data(closed)
        EMA26 = self._EMA26_data(closed)
        DIF = self._DIF_data(EMA12, EMA26, closed)
        DEA = self._DEA_data(DIF, closed)
        MACD = self._MACD_data(DIF, DEA, closed)
        _index = [MA3, MA5, MA6, MA10, MA12, MA20, MA24, MA30, MA50, \
                 MTM12, MTM12MA6, DDD, DMA_AMA10, BBI, BOLL, STD, \
                 BOLL_UP, BOLL_LOWER, IFUPPSY, PSY, PSYMA6, EMA12, \
                 EMA26, DIF, DEA, MACD]
        index = {}
        for i, ix in enumerate(self.allindexlist):
            index[ix] = _index[i]
        self.index = index

    def PickIndexs(self, data, pickindexlist):
        self._CalcAllIndexs(data)
        data_columns = data.columns.values.tolist()
        pickindexdata = [data]
        for i, ix in enumerate(self.allindexlist):
            if pickindexlist[ix] is True:
                data_columns.append(ix)
                pickindexdata.append(self.index[ix])
        new_data_columns = data_columns
        new_data = np.column_stack(pickindexdata)
        new_data = pd.DataFrame(new_data, columns=new_data_columns)
        return new_data









