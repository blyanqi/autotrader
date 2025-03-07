class IoCContainer:
    # 用于存储服务的字典
    _services = {}
    # 用于存储单例服务的字典
    _singletons = {}

    def __init__(self):
        pass

    def getInstance(self):
        return self

    def register(self, name, cls, singleton=False):
        """
        注册服务到容器中
        :param name: 服务的名称
        :param cls: 服务的类
        :param singleton: 是否为单例模式
        """
        if singleton:
            self._singletons[name] = cls
        else:
            self._services[name] = cls

    def resolve(self, name, *args, **kwargs):
        """
        解析服务并创建实例
        :param name: 服务的名称
        :param args: 传递给类构造函数的位置参数
        :param kwargs: 传递给类构造函数的关键字参数
        :return: 创建的服务实例
        """
        if name in self._singletons:
            # 如果是单例服务，检查是否已经创建过实例
            if not hasattr(self, f"_{name}_instance"):
                setattr(self, f"_{name}_instance",
                        self._singletons[name](*args, **kwargs))
            return getattr(self, f"_{name}_instance")
        elif name in self._services:
            # 如果是普通服务，直接创建新实例
            return self._services[name](*args, **kwargs)
        else:
            raise ValueError(f"Service '{name}' not registered.")


# 示例使用
if __name__ == "__main__":
    class Database:
        def __init__(self, connection_string):
            self.connection_string = connection_string

        def connect(self):
            print(f"Connecting to database with {self.connection_string}")

    class UserService:
        def __init__(self, db: Database):
            self.db = db

        def get_user(self, user_id):
            self.db.connect()
            print(f"Fetching user with ID: {user_id}")

    # 创建IoC容器
    container = IoCContainer()

    # 注册服务
    container.register("db", Database, singleton=True)  # 数据库服务为单例
    container.register("user_service", UserService)

    # 解析服务
    db = container.resolve(
        "db", connection_string="mysql://localhost:3306/mydb")
    user_service = container.resolve("user_service", db=db)

    # 使用服务
    user_service.get_user(user_id=1)
