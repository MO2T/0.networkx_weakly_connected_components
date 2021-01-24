#弱连通社区分化
# 生成数据
import random
import pandas as pd

print('=====生成数据文件开始=====')
# 数据字段模拟
seq_bank = ['中国人民银行', '中国农业银行','南京银行','工商银行','农业银行','建设银行','浦发银行','NULL']
seq_start = ['A', 'B','C','D','E','F','G','H']
seq_end = ['D','E','F','G','H','I', 'J','K',]
seq_type = ['NULL']
seq_dt = ['202012']
seq_asset = ['1', '2', '3', '4', '5']
seq_bad_asset = ['1', '2', '3', '4', '5']
seq_five = ['1', '2', '3', '4', '5', 'NULL']
seq_label = ['公司']

# 生成节点关系表
count = 10000
# 担保金额上界
guarantee_upper = 10000
# 担保金额下界
guarantee_lower = 1000
s = []
for i in range(count):
    s.append([random.choice(seq_start)+str(random.randint(0, int(0.4*count))),random.choice(seq_end)+str(random.randint(0, int(0.4*count))),random.choice(seq_bank),random.randint(guarantee_lower, guarantee_upper),random.choice(seq_type),random.choice(seq_dt)])
rela = pd.DataFrame(s, columns = ['STARTID', 'ENDID', 'BANK_NAME', 'GUARANTEE', 'TYPE', 'DT'])
# 取出节点id
node = pd.DataFrame(pd.concat([pd.DataFrame(rela['STARTID']).rename(columns={'STARTID':'id'})['id'], pd.DataFrame(rela['ENDID']).rename(columns={'ENDID':'id'})['id']])).drop_duplicates().reset_index(drop = True)

# 生成节点属性表
loan_upper = 100000
s = []
for i in node['id']:
    s.append([i, 'name'+i, random.choice(seq_asset), random.choice(seq_bad_asset), random.randint(0, loan_upper), random.choice(seq_five), random.choice(seq_label),random.choice(seq_dt)])
node = pd.DataFrame(s, columns = ['ID', 'CUST_NAME', 'ASSET_SCALE', 'BAD_ASSET_SCALE', 'LOAN', 'FIVE_CLASS', 'LABEL', 'DT'])
# 保存数据文件
print('=====node infomation=====')
print(node.info())
print('=====rela infomation=====')
print(rela.info())
node.to_csv('node.csv', header = None, index = None)
rela.to_csv('rela.csv', header = None, index = None)
print('=====数据生成结束=====')