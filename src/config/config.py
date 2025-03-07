import yaml
import os


class ConfigLoader:
    _config = ""

    def __init__(self, config_file=""):
        """
        初始化配置加载器
        :param config_file: YAML配置文件路径
        """
        self.config_file = config_file
        ConfigLoader._config = self.load_config()

    def load_config(self):
        """
        加载YAML配置文件
        :return: 配置字典
        """
        if ConfigLoader._config:
            return ConfigLoader._config

        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"配置文件 {self.config_file} 不存在")

        with open(self.config_file, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        return config

    def get(self, key, default=None):
        """
        获取配置项
        :param key: 配置键（支持点分路径，如 'database.host'）
        :param default: 默认值
        :return: 配置值或默认值
        """
        keys = key.split(".")
        value = ConfigLoader._config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def get_nested_value(self, key, default=None):
        """
        递归获取嵌套路径的值
        :param data: 数据（字典或列表）
        :param path: 路径（如 "users.0.name"）
        :param default: 默认值
        :return: 路径对应的值或默认值
        """
        keys = key.split(".")
        value = ConfigLoader._config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            elif isinstance(value, list) and key.isdigit() and int(key) < len(value):
                value = value[int(key)]
            else:
                return default
        return value


# 示例使用
if __name__ == "__main__":
    # 创建配置加载器
    config_loader = ConfigLoader("config.yaml")

    # 获取配置项
    app_name = config_loader.get("application.name")
    log_level = config_loader.get("logging.level")
    db_host = config_loader.get("database.host")
    db_port = config_loader.get("database.port")

    print(f"App Name: {app_name}")
    print(f"Log Level: {log_level}")
    print(f"Database Host: {db_host}")
    print(f"Database Port: {db_port}")

    # 获取不存在的配置项，返回默认值
    unknown_key = config_loader.get("nonexistent.key", default="Default Value")
    print(f"Unknown Key: {unknown_key}")
