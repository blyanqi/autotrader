# python 自动化交易系统

* 获取数据
* 分析数据
* 输出数据
* 执行交易
* 分析交易结果

```sh
python -m venv .venv
pip install --upgrade pip
```
## 安装依赖包

### akshare
https://akshare.akfamily.xyz/data/stock/stock.html#id10
`pip install akshare`

### pandas
https://pandas.pydata.org/docs/user_guide/10min.html
`pip install pandas`

### flask
https://flask.palletsprojects.com/en/stable/
`pip install Flask`
`flask --app  server run`
`flask --app  server run --host=0.0.0.0`
`flask --app  server run --debug`

https://jinja.palletsprojects.com/en/stable/templates/

### APScheduler
`pip install apscheduler`

### psutil
`pip install psutil`

### watchdog
`pip install watchdog`


## 目录结构
```sh
.
├── __init__.py
├── analysis # 分析数据
│   ├── __init__.py
│   ├── board.py
│   └── filter.py
├── data # 数据
│   ├── filter_buy_stock20250303.csv
│   ├── filter_buy_stock20250304.csv
│   ├── filter_rate20250303.csv
│   ├── filter_rate20250304.csv
│   ├── real_data20250303.csv
│   ├── real_data20250304.csv
│   ├── real_data_bj20250303.csv
│   ├── real_data_se20250303.csv
│   └── real_data_sh20250303.csv
├── entity # 实体
│   └── trader_entity.py
├── main.py # 主程序
├── policy  # 策略
│   └── policy.py
├── seek # 获取数据
│   └── seek_akshare.py
├── server.py # web 展示程序
├── task # 定时任务
│   └── task.py
├── templates
│   ├── hot_stock.html
│   └── index.html
└── trader # 交易
    ├── __init__.py
    ├── autoscpt
    │   ├── mock  # 模拟交易
    │   └── real  # 真实交易
    ├── mock_trader.py
    ├── real_trader.py
    ├── trader_exec.py # 交易执行
    └── trader_inf.py # 交易接口
```

### 流程
* 获取即时数据
* 对数据进行过滤
* 执行策略对过滤后的数据进行筛选
* 执行交易
> 获取数据是通过定时任务获取，定时任务通过apscheduler实现。
> 对数据进行过滤确定哪些数据是符合策略的，然后对符合策略的数据进行筛选。
> 策略主要负责在不同的时间段对指标进行筛选，比如在9:30-11:30和13:00-15:00的时间段对数据进行筛选。
> 交易主要负责对筛选后的数据进行交易，比如对筛选后的数据进行买入和卖出。

### 关于
仅供参考学习，请勿用于其他用途。
欢迎交流讨论，欢迎提issue，欢迎提pr。VX: blyq20067