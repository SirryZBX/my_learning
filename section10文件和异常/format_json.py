# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:format_json.py
@CreateTime:2022/4/17 17:37
"""

import json


def formatting_json():
    """对json文件数据进行格式化"""
    file_name = 'test.json'
    dict_json = {"a": 1, "b": {"list": [1, 2, 3], "str": "测试"}, "c": 3}
    with open(file_name, 'w', encoding='utf-8') as f:
        # 对字典进行格式化 indent 缩进 separators: 元素间以逗号分隔,
        # key-value间以冒号分隔  ensure_ascii保证中文不出现乱码
        format_json = json.dumps(dict_json, indent=4,
                                 separators=(',', ':'), ensure_ascii=False)
        print(format_json)
        print(type(format_json))
        # 将内容写入文件
        json.dump(format_json, f)


formatting_json()


def get_json_file():
    """获得json文件内容"""
    file_name = 'test.json'
    with open(file_name) as f:
        # 从文件读取内容
        contents = json.load(f)
        # 将获得的内容从str转换成字典
        dict_contents = json.loads(contents)
        print(dict_contents)
        print(type(dict_contents))


get_json_file()

