import yaml, os


class GetFileData:
    def __init__(self):
        pass

    def get_yml_data(self, yaml_name):
        """
        解析yaml文件
        :param yaml_name: yaml文件的全名
        :return: 返回yaml文件数据
        """
        with open("./Data" + os.sep + yaml_name, "r",encoding='utf-8') as f:
            return yaml.safe_load(f)
