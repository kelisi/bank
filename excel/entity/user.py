from .tradeinfo import TradeInfo


class User(object):
    name = ""
    identityId = ""
    tradeInfoDic = {}

    def __init__(self, name, id):
        self.name = name
        self.identityId = id

    @property
    def name(self):
        return self.name

    @property
    def identityId(self):
        return self.identityId

    def addTradeByTime(self, time, tradeInfo):
        if tradeInfoDic.has_key(time):
            tradeInfoDic[time].append(tradeInfo)
        else:
            tradeInfoDic[time] = []
            tradeInfoDic[time].append(tradeInfo)
