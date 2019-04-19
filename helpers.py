def get_classs(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


def getDictValue(dict, key, default=None):
    try:
        tempDict = dict
        keySplitted = key.split('.')
        for keyLevel in keySplitted:
            tempDict = tempDict[keyLevel]
        return tempDict
    except:
        return default
