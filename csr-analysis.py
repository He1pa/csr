import numpy as np
import pandas as pd
import jieba
import os
import xlwt

# 分词txt目录
dir = r'E:\code\csr\gbk\CSR报告txt2'
# 词典
dict_file = r'E:\code\csr\中文金融情感词典_姜富伟等(2020).xlsx'

res_file = r'E:\code\csr\tones.xls'


# 过滤中文符号
def remove_a(s):
    if (s != "\n") & (s != "”") & (s != "“") & (s != " ") & (s != "、") & (s != "，"):
        return s

# jieba 分词
def jieba_cut(file):
    with open(file,'r', encoding="gbk") as f:
        s = f.read()
        s = "".join([s for s in s.splitlines(True) if s.strip()]).strip()
        seg_list = jieba.lcut(s, cut_all=False)
        # 过滤中文符号
        res = list(filter(remove_a, seg_list))
    return res

def cal_tone(file, pos_arr, neg_arr):
    # 分词
    tokens = jieba_cut(file)
    pospct = list(filter(lambda s: s in pos_arr, tokens))
    negpct = list(filter(lambda s: s in neg_arr, tokens))

    # 算法1 无权重
    tone = (len(pospct) - len(negpct)) / (len(pospct) + len(negpct))
    return tone


if __name__ == "__main__":
    # 新建excel
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("csr")

    # 制作词典
    pos_dict = pd.read_excel(
        dict_file, sheet_name="positive", index_col=None)
    # 去掉词典中的 \n 换行符
    pos_arr = [s.replace("\n", "") for s in pos_dict['Positive Word']]


    neg_dict = pd.read_excel(
        dict_file, sheet_name="negative", index_col=None)

    neg_arr = [s.replace("\n", "") for s in neg_dict['Negative Word']]

    for root, dirs, files in os.walk(dir, topdown=False):
        for i, file in enumerate(files):
            filename = os.path.join(root, file)
            tone = cal_tone(filename, pos_arr, neg_arr)
            id = file[0:6]
            year = file[7: -4]
            sheet.write(i, 0, id)
            sheet.write(i, 1, year)
            sheet.write(i, 2, tone)
            print(id, year, tone)
            if i > 1:
                break
    workbook.save(res_file)
    


