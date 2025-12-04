import re
def sudification(txt:str)-> str:
    listwords = txt.split()
    processedlist = []
    for word in listwords:
        match = re.match(r"(.*[aeiou]n)([.,!?]*)", word)
        if match:
            raw_word, punct = match.groups()
            processedlist.append(raw_word + "g" + punct)
        else:
            processedlist.append(word)
    processedstring = ' '.join(processedlist)
    return processedstring




