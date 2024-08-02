# -*- coding: utf-8 -*-

"""
文件读写

| 操作模式  具体含义
| r 读取（默认）
| w 写入（会先截断之前的内容）
| x 写入，如果文件已经存在会产生异常
| a 追加，将内容写入到已有文件的末尾
| rb 读取二进制模式
| wb 写入二进制模式
| t 文本模式（默认）
| + 更新（即可以读又可以写
"""

from math import sqrt
import json


def main_a():
    file_path = "test.xlsx"

    try:

        f = open(file=file_path, mode="r", encoding="utf-8")

        f.read()

    except Exception as e:

        print(f"An error occurred: {e}")

    finally:

        print("Done")


def is_prime(number: int):
    for factor in range(2, int(sqrt(number) + 1)):

        if number % factor == 0:
            return False

    return True if number != 1 else False


def main_b():
    filenames: tuple = ("a.txt", "b.txt", "c.txt")
    file: list = []

    try:
        for filename in filenames:
            file.append(open(filename, "w", encoding="utf-8"))

        for number in range(1, 10000):

            if is_prime(number):
                if number < 100:
                    file[0].write(str(number) + "\n")

                elif number < 1000:
                    file[1].write(str(number) + "\n")

                else:
                    file[2].write(str(number) + "\n")

    except Exception as e:

        print(f"An error occurred: {e}")

    finally:

        print("Done")


def main_c():

    try:

        with open("Guido van Rossum.png", "rb") as f1:
            data = f1.read()

            with open("Guido.png", "wb") as f2:
                f2.write(data)

    except Exception as e:

        print(f"An error occurred: {e}")


def main_d():

    try:

        show: dict = {
            'name': 'quanma',
            'age': 19,
            'birthday': '0722',
            'research': [
                {
                    'a': 'data science',
                    'b': 'public analysis'
                }
            ]
        }

        with open(file="test.json", mode="w", encoding="utf-8") as f:
            json.dump(show, f)

    except Exception as e:

        print(f"An error occurred: {e}")


if __name__ == '__main__':
    # main_a()
    # main_b()
    # main_c()
    main_d()
