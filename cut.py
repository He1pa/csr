import jieba

# 分词文件
file = r'E:\code\csr\gbk\000001_2008年度社会责任报告.txt'
# 保存路径
save_file = r'E:\code\csr\分词\000001_2008年度社会责任报告.txt'

def remove_a(s):
    if (s != "\n") & (s != "”") & (s != "“") & (s != " ") & (s != "、") & (s != "，"):
        return s
if __name__ == "__main__":
    res = []
    
    with open(file,'r', encoding="gbk") as f:
        s = f.read()
        s = "".join([s for s in s.splitlines(True) if s.strip()]).strip()
        seg_list = jieba.lcut(s, cut_all=False)
        # 过滤中文符号
        res = list(filter(remove_a, seg_list))
        print(res)
    with open(save_file, 'w', encoding="utf-8") as f:
        data = " ".join(res)
        f.write(data)