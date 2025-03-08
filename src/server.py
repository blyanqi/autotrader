
import os
from pathlib import Path
from flask import Flask, render_template, jsonify, request
from src.core.container import IoCContainer
from src.core.logger import Logger
import src.core.service as service

app = Flask(__name__)

curDir = os.path.dirname(__file__)
container = IoCContainer()
config = container.resolve("config", f"{curDir}/config/config.yaml")
logger = Logger.get_logger("web")


resp_success = {
    "code": 0,
    "msg": "success"
}

resp_error = {
    "code": 1,
    "msg": "error"
}


@app.route("/")
def hello_world():
    return render_template('index.html', stocks=filter.test_filter().to_dict(orient="records"))


@app.route("/api/sellAll", methods=['POST'])
def sell_all():
    try:
        trader = container.resolve("realTrader")
        traderExec = container.resolve("traderExec", trader)
        traderExec.sell_all()
    except:
        logger.error("sell all error")
        return jsonify(resp_error), 200
    return jsonify(resp_success), 200


@app.route("/api/buy", methods=['POST'])
def buy():
    try:
        trader = container.resolve("realTrader")
        traderExec = container.resolve("traderExec", trader)
        item = request.json
        logger.info(item)
        traderExec.buy(item["code"], item["num"])
    except Exception as e:
        logger.error(e)
        return jsonify(resp_error), 200
    return jsonify(resp_success), 200


@app.route("/api/sell", methods=['POST'])
def sell():
    try:
        trader = container.resolve("realTrader")
        traderExec = container.resolve("traderExec", trader)
        item = request.json
        logger.info(item)
        traderExec.sell(item["code"], item["num"])
    except Exception as e:
        logger.error(e)
        return jsonify(resp_error), 200
    return jsonify(resp_success), 200


@app.route("/api/autoBuy", methods=['POST'])
def auto_buy():
    try:
        type1 = config.get_nested_value("policy.0")
        seek = container.resolve("seek")
        trader = container.resolve("realTrader")
        traderExec = container.resolve("traderExec", trader)
        filter = container.resolve("filter")
        policy = container.resolve("policy", filter)
        seek.real_data()
        policy.top_volumerate_day()
        traderExec.policy_buy_stock(type1["name"])
    except:
        logger.error("auto buy error")
        return jsonify(resp_error), 200
    return jsonify(resp_success), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
