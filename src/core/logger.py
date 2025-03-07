import logging
import os
from logging.handlers import RotatingFileHandler


class Logger:
    _loggers = {}  # 用于缓存日志实例，避免重复创建

    @staticmethod
    def get_logger(name="default", log_level=logging.INFO, log_file=None, max_bytes=10*1024*1024, backup_count=5):
        """
        获取日志实例
        :param name: 日志名称
        :param log_level: 日志级别（DEBUG, INFO, WARNING, ERROR, CRITICAL）
        :param log_file: 日志文件路径（如果为None，则不写入文件）
        :param max_bytes: 单个日志文件的最大字节数
        :param backup_count: 备份日志文件的数量
        :return: 配置好的Logger对象
        """
        if name in Logger._loggers:
            return Logger._loggers[name]

        # 创建Logger对象
        logger = logging.getLogger(name)
        logger.setLevel(log_level)

        # 创建日志格式
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # 添加控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # 如果指定了日志文件，添加文件处理器
        if log_file:
            # 确保日志文件的目录存在
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            file_handler = RotatingFileHandler(
                log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        # 缓存日志实例
        Logger._loggers[name] = logger
        return logger


# 示例使用
if __name__ == "__main__":
    # 创建日志实例
    logger = Logger.get_logger(
        name="my_app",
        log_level=logging.DEBUG,
        log_file="logs/app.log"
    )

    # 测试日志
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
