from .tradeinfo import TradeInfo


class User(object):
    name = ""
    identityId = ""
    tradeInfoDic = {}

    def __init__(self, name, id):
        self.name = name
        self.identityId = id
        self.tradeInfoDic = {}

    def addTradeByTime(self, time, tradeInfo):
        if time in self.tradeInfoDic:
            self.tradeInfoDic[time].append(tradeInfo)
        else:
            self.tradeInfoDic[time] = []
            self.tradeInfoDic[time].append(tradeInfo)
