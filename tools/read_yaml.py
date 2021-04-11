# noinspection PyUnresolvedReferences
import config
import os
# noinspection PyUnresolvedReferences
import yaml
# 定义函数
def read_yaml(filename):
    arr = []
    file_path = config.BASE_PATH + os.sep+"data"+os.sep+filename
    # print(file_path)
    # 获取文件流
    with open(file_path, "r",encoding="utf-8") as f:
        #遍历，调用yaml.safa.load(f).values()
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
        return arr

if __name__ == '__main__':
    print(read_yaml("mp_login.yaml"))