mt_path = "train.mt"
pe_path = "train.pe"
mt_new_path = "train_new.mt"
pe_new_path = "train_new.pe"

"""给数据添加标签"""
# hyp, ref = [], []
# with open(mt_path, "r", encoding="utf-8") as mt:
#     with open(pe_path, "r", encoding="utf-8") as pe:
#         for i, (m, p) in enumerate(zip(mt, pe)):
#             m = m.strip() + "(" + str(i) + ")\n"
#             p = p.strip() + "(" + str(i) + ")\n"
#             hyp.append(m)
#             ref.append(p)
# with open(mt_new_path, "w", encoding="utf-8") as mt:
#     mt.writelines(hyp)
# with open(pe_new_path, "w", encoding="utf-8") as pe:
#     pe.writelines(ref)

"""读取计算hter的分子分母，并计算hter，保留小数后6位"""
sum_path = "out.txt.sum"
hters = []
with open(sum_path, "r", encoding="utf-8") as file:
    for i in range(5):
        file.readline()
    scores = file.readlines()
for score in scores:
    score = score.split("|")
    try:
        numEr = float(score[-3].strip())
    except:
        break
    numWd = float(score[-2].strip())
    hter = round(numEr / numWd, 6)
    hters.append(hter)
print(hters)

"""读取hter文件中的数值"""
hter_path = "train.hter"
hters_ref = []
with open(hter_path, "r", encoding="utf-8") as file:
    hter_ref = file.readlines()
    for item in hter_ref:
        item = float(item.strip())
        hters_ref.append(item)
print(hters_ref)

"""统计"""
num = 0
total = 0
for idx, (i, j) in enumerate(zip(hters, hters_ref)):
    if i==j:
        num += 1
    if i != j:
        print(idx, i, j)
    total += 1
print("TER计算的评分与官方给的hter分数相比：相等的数有{}个，总数有{}个".format(num, total))
