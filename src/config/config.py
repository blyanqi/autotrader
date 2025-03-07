from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class ConfigReloadHandler(FileSystemEventHandler):
    def __init__(self, config_loader):
        self.config_loader = config_loader

    def on_modified(self, event):
        if event.src_path == self.config_loader.config_file:
            print("配置文件已修改，重新加载...")
            self.config_loader.load_config()


# 示例
if __name__ == "__main__":
    config_loader = ConfigLoader("config.yaml")
    event_handler = ConfigReloadHandler(config_loader)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
