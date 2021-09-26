import jieba
import random
import sys
import json
import logging

jieba.setLogLevel(logging.INFO)
text = sys.argv[1]
mode =sys.argv[2]
if mode == "word":
    reciteMode="1"
elif mode=="sentence":
    reciteMode="2"
else:
    reciteMode = random.choice(["1","2"])

signs = ["，", "。", "！", "？", "“", "”", "《", "》", "（", "）","、","；",",","."," ","-","!",";","?","'"," ","\n"]

def reciteMode1(text):
    words = jieba.tokenize(text)
    blankIndex = []
    for i in words:
        if (not i[0] in signs) and random.choice([True,False]):
            blankIndex.append([i[1],i[2]])
    blankIndexFiltered=[blankIndex[0]]
    listToProcess=blankIndex[1:]
    while listToProcess:
        if blankIndexFiltered[-1][1]==listToProcess[0][0]:
            blankIndexFiltered[-1][1]=listToProcess[0][1]
        else:
            blankIndexFiltered.append(listToProcess[0])
        del listToProcess[0]
    return blankIndexFiltered

def reciteMode2(text):
    words = jieba.tokenize(text)
    blankIndex= []
    flag =random.choice([True,False])
    for i in words:
        if i[0] in signs:
            if random.choice([True,False]):
                flag=not(flag)
        elif flag:
            blankIndex.append([i[1],i[2]])
    blankIndexFiltered=[blankIndex[0]]
    listToProcess=blankIndex[1:]
    while listToProcess:
        if blankIndexFiltered[-1][1]==listToProcess[0][0]:
            blankIndexFiltered[-1][1]=listToProcess[0][1]
        else:
            blankIndexFiltered.append(listToProcess[0])
        del listToProcess[0]
    return blankIndexFiltered

output=json.dumps(eval("reciteMode" + reciteMode + "(text)"))
sys.stdout.write(output)
