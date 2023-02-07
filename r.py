

menu_info = """
序号	菜品		价格		点赞  类型
1,	好吃土豆,	12.00,		61,     b    
2,	北邮凉面,	9.00,		60,     a    
3,	面包心语,	26.00,		14,     a   
4,	蟹黄豆腐,	23.00,		4,      b
5,	香草炸整鸡,	49.00,		3,      b
6,	香嘴牛肉丝,	42.00,		2,      b
7,	蓝莓山药,	18.00,		2,      c
8,	肥牛海鲜香锅,	56.00,		1,      b
"""
sorts=['好吃土豆',
       '北邮凉面','面包心语','蟹黄豆腐','香草炸整鸡','香嘴牛肉丝','蓝莓山药','肥牛海鲜香锅']
#新建一个菜名列表
data = {}#建立一个空的表
#ffffff
data22222=0
data111= []
for item in menu_info.split('\n')[2:-1]:
	pid, name, price, likes,types = item.split(',')#将菜单按序号进行分别拆分，其中按类型分为多个列表
	
	data[pid] = {
		'name' 	: name.strip(),#菜名
		'price' : float(price.strip()),#价格
		'likes' : int(likes.strip()),#点赞数
                'types':types.strip(),#类型
                }
key = ''
done = []   #用于存储每一次点菜的具体内容
cal=[None]*8#用于统计菜名出现次数
number=[None]*100#用于统计点菜的数量
money = 0.0#总金额
print('请问你们的人数是')
o=input()#输入人数
print('建议你们点',int(o)+1,'个菜')
while 1:
        print('___欢迎光临！___')
        print(menu_info.replace(',', ' ').strip())#打印菜单
        if done:  
            print('================已点菜品')
            for i in range(8):                #每次循环均要把所有菜名都统计一遍
                cal[i]=done.count(sorts[i])#从点菜数的列表中返回特定菜名出现的次数，计入统计列表中
                print(sorts[i],cal[i])#打印一次点菜的统计结果
        print('输入菜品序号点餐，按 9 结束')
        key = input()
        if key=='1' or key=='2':
            print('这是我们的招牌菜，希望您满意')
        if key =='9':
            if int(sum(cal))>=int(o)+1:     #如果点菜数量不少，则直接跳过
                break
            else:
                print('菜品数量可能不够，确定不要继续点了吗？')
                print('yes/no')
                u=input()
                if u=='yes':                #输入yes或者no
                      break
                else:
                      continue
                
        else:
                done.append(data[key]['name'])             #将菜名添加到用于存储每一次点菜的列表中
                number.append(data[key]['types'])          #统计点菜次数
                money += data[key]['price']                #计算总金额
        if number.count('a')==0:                           #判断是否有主食
                              print('=============您没有点主食')
        if number.count('b')==0:                           #判断是否有配菜
                              print('=============您没有点配菜')
        if number.count('c')==0:                           #判断是否有甜点
                              print('=============您没有点甜点')
print(' 总价:', money)                                      #打印总金额
