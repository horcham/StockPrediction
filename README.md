# StockPrediction
Tools for getting and modeling Chinese stocks

这是一个针对中国股票市场分析和建模的project，它的名字叫`zystock`, 它支持以下功能：

- [x] 输入股票代码，自动获取该股票的所有历史数据
- [x] 计算该股票的常用指标
- [ ] 快速使用深度学习模块，构建模型

## Requirements
 - numpy 1.14.0
 - pandas 0.22.0

## install
```python
git clone https://github.com/horcham/StockPrediction
pip install -r requirements
python setup.py install
```

## Quick Start
### 获取给定股票的所有历史数据
 - 在`GlobalParams.py`中的`STOCKDATASAVEDIR`中填入保存股票原始数据的地址。默认为`stock_data`(请使用绝对路径)
 - 用给定股票代码，初始化`Stock`类。例如股票代码为`600019`（宝钢股份），则
   ```python
   import numpy as np
   import pandas as pd
   import zystock as zys
   stock = zys.Stock('600019')    # 用股票代码初始化`Stock`类，并获取数据
   print(stock.data)          # 输出股票数据
   ```
   其中，`close`：收盘价， `high`：最高价， `low`：最低价， `open`：开盘价， `qsp`：前收盘， `zdy`：涨跌额
   `rate`：涨跌幅， `hsl`：换手率， `cjl`：成交量， `cjje`：成交金额， `zsz`：总市值， `ltsz`：流通市值
   
### 计算常用指标
  - 指标有：
    - MA3
    - MA5
    - MA6
    - MA10
    - MA12
    - MA20
    - MA24
    - MA30
    - MA50
    - MTM12
    - MTM12MA6
    - DDD
    - DMA_AMA10
    - BBI
    - BOLL
    - STD20
    - BOLL_UP
    - BOLL_LOWER
    - IFUP_PSY
    - PSY
    - PSYMA6
    - EMA12
    - EMA26
    - DIF
    - DEA
    - MACD
  - 在`GlobalParams.py`中的`PICKINDEXLIST`中，选择所需要的指标，需要的`True`，不需要的`False`。默认为全`True`。
  - 初始化`IndexCalculator`类，并计算指标
  ```python
  indexcalc = zys.IndexCalculator()   # 初始化`IndexCalculator`类
  stockdata = indexcalc.PickIndexs(stock.data, zys.PICKINDEXLIST)  # 用`Stock`嗦获取的数据计算指标
  print(stockdata)  # 输出数据与指标
  ```
  ### run demo
  运行`python main.py`
