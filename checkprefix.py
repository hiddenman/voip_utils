

def addOne(foundPrefix, prefix, name, price):
    prefixList = foundPrefix.setdefault((name, price), [])
    prefixList.append(prefix)

def addAll(priceList):
    foundPrefix = {}
    for price in priceList:
        addOne(foundPrefix, price[0], price[1], price[2])
        
    return foundPrefix
        

def checkPrefix(prefixList):
    differentPrefixMap = {}
    for prefix in prefixList:
        prefixPattern = str(prefix)[:-1]
        lastPrefixDigit = int(str(prefix)[-1])
        differentPrefixMap.setdefault(prefixPattern, set()).update((lastPrefixDigit,))
        
    for prefix, lastDigitSet in differentPrefixMap.items():
        if len(lastDigitSet) == 10:
            return True
    return False

def check(priceList):
    foundPrefix = addAll(priceList)
    wrongPrefix = []
    for key, prefixList in foundPrefix.items():
        # Optimization: if less then 10 prefix was found there are no all last 0-9 digits
        if len(prefixList) >= 10:
            if checkPrefix(prefixList):
                wrongPrefix.append(key)
                
    return wrongPrefix

if __name__ == '__main__':
    prefixList = [
    ('37060', 'Country test name', '0.5'),
    ('37167', 'Country test name', '0.5'),
    ('37061', 'Country test name', '0.5'),
    ('37062', 'Country test name', '0.5'),
    ('37063', 'Country test name', '0.5'),
    ('37064', 'Country test name', '0.5'),
    ('37065', 'Country test name', '0.5'),
    ('37066', 'Country test name', '0.5'),
    ('37068', 'Country test name', '0.5'),
    ('37069', 'Country test name', '0.5'),
     ]
    print check(prefixList)
