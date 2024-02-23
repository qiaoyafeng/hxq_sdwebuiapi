import os
config_path = __file__


class Config:
    @classmethod
    def get_home_path(cls):
        return os.path.dirname(config_path)

    @classmethod
    def check_path(cls, dir_path):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    @classmethod
    def get_temp_path(cls):
        temp_path = os.path.join(cls.get_home_path(), "temp")
        cls.check_path(temp_path)
        return temp_path

