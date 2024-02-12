
# -*- coding: utf-8 -*-

import json
import requests


def get_score(content_input):
    """
    调用情感分类模型API获取文本的情感评分。
    """
    api_url = "https://api-inference.modelscope.cn/api-inference/v1/models/iic/nlp_structbert_sentiment-classification_chinese-base"
    headers = {"Authorization": f"Bearer f807c767-ac33-4a87-a421-ef4c6ef8cdf2"}

    data = json.dumps(content_input)
    response = requests.request("POST", api_url, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


def main():
    """
    主函数，用于接收输入内容并调用情感分类模型获取情感评分并打印结果。
    """
    while True:
        content = input("请输入内容：")
        content_input = {"input": content}
        output = get_score(content_input)["Data"]
        print(output)


if __name__ == '__main__':
    main()
