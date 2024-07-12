import exrex
import requests


class Zidian:

    def __init__(self, url, file_name, new_file_names):
        self.url = url
        self.file_name = file_name
        self.new_file_names = new_file_names


    def get_url(self):
        # 通过split切割出来是一个列表
        url_list = self.url.split(".")
        # 通过拿到url_list的列表长度
        # len(url_list)
        # 永远dou'qie第一位，因为第一位不纯粹，有http://内容
        # 第一位内容：  加循环写入new_url_list列表里面
        new_url_list = [url_list[0].split("://")[-1]]
        for i in url_list:
            if i == url_list[0] or i == url_list[-1]:
                continue  # 跳过
            new_url_list.append(i)
        return new_url_list


    def get_txt_contents(self):
        # 读取txt文件内容
        with open(f"{self.file_name}", "r") as f:
            muben_list = f.read().splitlines()
        return muben_list



    def put_txt_contents(self):
        # xiaoran xiaoliu  xiaoxiao
        with open(f"{self.new_file_names}", "a", newline="") as f:
            for a in self.get_txt_contents():
                for b in range(0, len(self.get_url())):
                    for c in range(0, len(self.get_url())):
                        if b == c:
                            continue
                        d = self.get_url()[b]
                        e = self.get_url()[c]
                        dicts02 = list(exrex.generate(rf"{d}{a}{e}"))
                        f.write(dicts02[0] + "\n")


if __name__ == '__main__':
    url = input("请输入url：")
    zidian = Zidian(url=url, file_name="muben.txt", new_file_names="new_dict2.txt")
    zidian.put_txt_contents()
