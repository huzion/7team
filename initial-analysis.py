# -*- coding: utf-8 -*- 
import config 

globalConfig = config.globalConfig
globalState = config.globalState
accountConfig = config.accountConfig

# 组队list，用于存放生成的7人组
teamList = []

# 是否需要新建组队
needNewTeam = None

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

    # 当前组队是否完成
    isFinished = False

    def __init__(self, nodeNum):

        if nodeNum > 0 and nodeNum <= 7:
            for num in range(1, nodeNum):
                _obj = User(0,0,0,0, 10000)
                setattr(self, 'node' + str(num), _obj)
            # 累计数据
            globalState['allUsers'] += 1
            globalState['allTeams'] += 1
            globalState['platformSales'] += 10000
            globalState['allOrderCount'] += 1

        else:
            print('组队数据过大，请输入1到7的数值')

    def addNode(self, balance, integral, consumerIntegral, withdrawIntegral, comsumeCount):
        global globalState, globalConfig

        _obj = User(balance, integral, consumerIntegral, withdrawIntegral, comsumeCount)
        
        i = 1
        for key in self.__dict__:
            i = i + 1

        if (i > 0 and i < 8):
            attrName = 'node' + str(i + 1)

            setattr(self, attrName, _obj)

            # 累计数据
            globalState['allUsers'] += 1
            globalState['platformSales'] += 10000
            globalState['allOrderCount'] += 1

            

            # 以下需更改配置为变量
            if (i > 0 and i < 3):
                # 返利
                _rewardIntergral = 10000 * 0.15 * 0.85

                # 增加支出统计
                globalState['platformExpend'] += _rewardIntergral
                print('23支出', _rewardIntergral)

            else:
                # 返利
                _rewardIntergral = ((10000 * 0.15) + (10000 * 0.3)) * 0.85

                # 增加支出统计
                globalState['platformExpend'] += _rewardIntergral

                print('4567支出', _rewardIntergral)

                if (i == 7):
                    globalState['allFinishedTeams'] += 1
                    self.isFinished = True
                    print('//////组队已满')

            return True
        else:
            print('.......当前组队完成！')

# 定义成长模拟器
class GrowSimulator(object):

    def __init__(self):
        pass

    def addUser(self, count):
        global teamList, globalState, globalConfig, needNewTeam

        # 此处种子用户已被注释掉
        # _userCount = globalConfig['angelUserCount']


        

        for num in range(count):

            #判断是否需要新建组队
            for key in teamList:
                if (key.isFinished == False):
                    needNewTeam = False
                    break
                else:
                    needNewTeam = True

            _count = count - num
            print('是否需要新建组队？：', needNewTeam)
            
            i = 0
            for key in teamList:
                i += 1
                if (key.isFinished == False):

                    needNewTeam = False
                    
                    key.addNode(0, 0, 0, 0, 10000)

                    _rewardIntergral = globalConfig['orderPrice'] * globalConfig['orderRebateBalanceLeve1']


            if needNewTeam:
                print('------------新建组队------------')
                _team = SevenTeamTree(1)
                teamList.append(_team)

                _rewardIntergral = globalConfig['orderPrice'] * globalConfig['orderRebateBalanceLeve1']

                # 用户积分记录
                #key.node1.integral += _rewardIntergral
                print('当前组队数~~~~~~~：', len(teamList))
                # 累计数据
                globalState['allTeams'] += 1
                globalState['allUsers'] += 1
                globalState['platformSales'] += 10000
                globalState['allOrderCount'] += 1


# 初始化组队
initTeam = SevenTeamTree(1)
teamList.append(initTeam)

growing = GrowSimulator()
growing.addUser(360)


print('--------------------------------------------------------------------------------')
print('累计用户：', globalState['allUsers'])
print('累计组队：', globalState['allTeams'])
print('累计平台总销售：', globalState['platformSales'])
print('累计下单量：', globalState['allOrderCount'])
print('累计组队成功次数：', globalState['allFinishedTeams'])
print('累计支出：', globalState['platformExpend'])
print('当前组队数~~~~~~~：', len(teamList))