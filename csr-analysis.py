import numpy as np
import pandas as pd
import jieba

# 分词txt文件
file = r'E:\code\csr\gbk\000001_2008年度社会责任报告.txt'
# 词典
dict_file = r'E:\code\csr\中文金融情感词典_姜富伟等(2020).xlsx'


# 过滤中文字符
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


if __name__ == "__main__":
    # 分词
    tokens = jieba_cut(file)

    # 制作词典
    pos_dict = pd.read_excel(
        dict_file, sheet_name="positive", index_col=None)
    # 去掉词典中的 \n 换行符
    pos_arr = [s.replace("\n", "") for s in pos_dict['Positive Word']]

    # 积极词汇
    pospct = list(filter(lambda s: s in pos_arr, tokens))

    neg_dict = pd.read_excel(
        dict_file, sheet_name="negative", index_col=None)

    neg_arr = [s.replace("\n", "") for s in neg_dict['Negative Word']]

    negpct = list(filter(lambda s: s in neg_arr, tokens))

    # 算法1 无权重
    tone = (len(pospct) - len(negpct)) / (len(pospct) + len(negpct))
    print(tone)


