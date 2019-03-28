# -*- coding: utf-8 -*- 
import config 

globalConfig = config.globalConfig
globalState = config.globalState
accountConfig = config.accountConfig

# 定义用户类
class User(object):
    
    # 下单次数
    orderCount: 0

    # 是否可下单
    orderSwitch: False

    def __init__(self, balance, integral, consumerIntegral, withdrawIntegral, comsumeCount):
        global accountConfig

        for (key, value) in accountConfig.items():
            setattr(self, key, value)

    # 充值
    def recharge(self, amount):
        pass
    
    # 下单
    def order(self, amount):
        pass

    # 提现
    def withdraw(self, amount):
        pass

# 定义7人组树模型
class SevenTeamTree(object):
    def __init__(self, nodeNum):
        for num in range(nodeNum):
            _obj = User(0,0,0,0, 10000)
            setattr(self, 'node' + str(num), _obj)

    def addNode(self, balance, integral, consumerIntegral, withdrawIntegral, comsumeCount):
        global globalState

        _obj = User(balance, integral, consumerIntegral, withdrawIntegral, comsumeCount)
        
        i = 0
        for key in self.__dict__:
            i = i + 1
            print(key)

        if (i<7):
            attrName = 'node' + str(i + 1)
            setattr(self, attrName, _obj)

            # 累计数据
            globalState['allUsers'] += 1
            globalState['allTeams'] += 1
            globalState['platformSales'] += 10000
            globalState['allOrderCount'] += 1

            if (i == 6):
                globalState['allFinishedTeams'] += 1

            return True
        else:
            return False

b = SevenTeamTree(4)
b.addNode(0, 0, 0, 0, 10000)

# 定义成长模拟器
class GrowSimulator(object):

    def __init__(self):
        pass

    def addUser(self, count):
        pass


print('累计用户：', globalState['allUsers'])
print('累计组队：', globalState['allTeams'])
print('累计平台总销售：', globalState['platformSales'])
print('累计下单量：', globalState['allOrderCount'])
print('累计组队成功次数：', globalState['allFinishedTeams'])
