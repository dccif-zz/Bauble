from gen import gendata
if __name__ == "__main__":
    num = int(input("请输入要生成的数据个数:").strip())
    filename = input("请输入文件名，默认为data").strip()
    if filename != '':
        gendata(num, filename)
    gendata(num)