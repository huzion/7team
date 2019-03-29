# ------ 全局配置 ------
globalConfig = {
    # 订单1级返利积分比例
    "orderRebateBalanceLeve1": 0.15,

    # 订单2级返利积分比例
    "orderRebateBalanceLeve2": 0.3,

    # 订单返消费积分比例
    "orderRebateconsumerIntegral": 0.1,

    # 种子用户人数
    "angelUserCount": 1000,

    # 用户周增长系数
    "userWeekIncreas": 1.5,

    # 兑换现金手续费
    "exchangeCashTax": 0.03,

    # 提现手续费
    "exchangeCashTax": 0.03,

    # 组队成功率
    "teamRate": 0.3,

    # 订单价格
    "orderPrice": 10000
}

# ------ 用户账户配置 ------
accountConfig = {
    # 余额
    "balance": 0,
    
    # 积分
    "integral": 0,
    
    # 消费积分
    "consumerIntegral": 0,
    
    # 可提现金额
    "withdrawIntegral": 0,

    # 历史消费金额
    "comsumeCount": 0
}

# ------ 数据统计 ------
globalState = {
    # 总人数
    "allUsers" : 0,

    # 总组数
    "allTeams" : 0,

    # 总组队成功次数
    "allFinishedTeams" : 0,

    # 平台总收益
    "platformIncome" : 0,

    # 平台总销售额度
    "platformSales" : 0,

    # 平台总支出额度
    "platformExpend" : 0,

    # 产生的兑换手续费总数
    "allExchangeTax" : 0,

    # 产生的提现手续费总数
    "allWithdrawTax" : 0,

    # 经历时间（周）
    "weekSpent" : 0,

    # 总下单次数
    "allOrderCount" : 0

}
