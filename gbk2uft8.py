## gbk to utf8

import os
import codecs

# 设置路径
srcPath = r'E:\code\csr\gbk'
targetPath = r'E:\code\csr\utf8'

# 设置要保存的文件格式
postfix = set(['txt'])  

class CCopyFile:
    def __init__(self, src, dst):
        def ReadFile(filePath, encoding=""):
            with codecs.open(filePath, "rb", encoding) as f:
                return f.read()

        def WriteFile(filePath, contents, encoding=""):
            with codecs.open(filePath, "wb", encoding) as f:
                f.write(contents)     

        def UTF8_2_GBK(src, dst):
            contents = ReadFile(src, encoding="utf-8")
            WriteFile(dst, contents, encoding="gb18030")

        def GBK_2_UTF8(src, dst):
            contents = ReadFile(src, encoding="gb18030")
            WriteFile(dst, contents, encoding="utf-8")

        def CopyFile(src, dst):
            with open(src, 'rb') as readStream:
                contents = readStream.read()
                with open(dst, 'wb') as writeStream:
                    writeStream.write(contents)

        '''
        匹配后缀，只保存所选的文件格式，并调用 GBK_2_UTF8。
        若要保存全部文件，则注释该句直接调用 CopyFile。
        注：
        1. GBK_2_UTF8 复制文件，并且将编码格式从GBK转为UTF-8
        2. CopyFile 直接复制文件，保留源文件的编码格式
        ''' 
        if src.split('.')[-1] in postfix:  
            GBK_2_UTF8(src, dst)
        else:
            CopyFile(src, dst)

# 将源文件夹整体复制到目标文件夹
def CopyDir(srcPath, targetPath):
    if os.path.isdir(srcPath) and os.path.isdir(targetPath):
        filelist_src = os.listdir(srcPath)
        for file in filelist_src:
            path = os.path.join(os.path.abspath(srcPath), file)    
            if os.path.isdir(path):
                path1 = os.path.join(os.path.abspath(targetPath), file)    
                if not os.path.exists(path1):                       
                    os.mkdir(path1)
                CopyDir(path, path1)          
            else:   
                path1 = os.path.join(targetPath, file)
                CCopyFile(path, path1)       
        return True
    else:     
        return False   

if __name__ == '__main__':  
    nRet = CopyDir(srcPath, targetPath) 
    if nRet:
        print('Copy Dir OK!')
    else:
        print('Copy Dir Failed!')