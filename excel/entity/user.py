
class User(object):
    def __init__(self, name, id, userNo):
        self.name = name
        self.identityId = id
        self.userNo = userNo
        self.saving_card_trade_info = {}
        self.credit_card_trade_info = {}

    def __addTradeByTime(self, time, tradeInfoDic, tradeInfo):
        if time in tradeInfoDic:
            tradeInfoDic[time].append(tradeInfo)
        else:
            tradeInfoDic[time] = []
            tradeInfoDic[time].append(tradeInfo)

    def addSavingCardTradeByTime(self, time, tradeInfo):
        self.__addTradeByTime(time, self.saving_card_trade_info, tradeInfo)

    def addCreditCardTradeInfo(self, time, tradeInfo):
        self.__addTradeByTime(time, self.credit_card_trade_info, tradeInfo)

