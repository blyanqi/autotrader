
获取数据
分析数据
输出数据
执行交易
分析交易结果

```sh
python -m venv .venv
pip install --upgrade pip
```

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
├── main.py
├── policy # 策略
│   └── policy.py
├── seek # 获取数据
│   └── seek_akshare.py
├── server.py
├── task # 定时任务
│   └── task.py
├── templates
│   ├── hot_stock.html
│   └── index.html
└── trader # 交易
    ├── __init__.py
    ├── autoscpt
    │   ├── mock
    │   └── real
    ├── mock_trader.py
    ├── real_trader.py
    ├── trader_exec.py
    └── trader_inf.py
```