class Rules:
    def __init__(self):
        self.rules = {
            "cold": {
                "small": "small",
                "medium": "medium",
                "high": "high"
            },
            "cool": {
                "small": "small",
                "medium": "medium",
                "high": "high"
            },
            "moderate": {
                "small": "small",
                "medium": "small",
                "high": "small"
            },
            "hot": {
                "small": "small",
                "medium": "small",
                "high": "small"
            },
            "very hot": {
                "small": "small",
                "medium": "small",
                "high": "small"
            }
        }
    def evaluate(self, t, c):
        tempDict = t.toDiscrete()
        capDict = c.toDiscrete()
        
        print(tempDict)
        print(capDict)
        resDict = {}
        for tkey, tvalue in tempDict.items():
            for ckey, cvalue in capDict.items():
                result = self.rules[tkey][ckey]
                val = min(tvalue, cvalue)
                if result in resDict:
                    resDict[result] = max(resDict[result], val)
                else:
                    resDict[result] = val
        return resDict