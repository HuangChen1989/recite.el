import jieba
import random
import sys
import json
import logging


jieba.setLogLevel(logging.INFO)
signs = ["，", "。", "！", "？", "“", "”", "《", "》", "（", "）","、","；",",","."," ","-","!",";","?","'"," ","\n"]

# [[4, 7]]
# [[4, 7], [8, 12]]
def replaceWord(x, s):
    res = []
    for i in x:
        if i in signs:
            res.append(i)
        elif ord(i) > 126:
            res.append(s * 2)
        else:
            res.append(s)
    return "".join(res)

def get_overlay_start_end(words,word_index):
    word_len=len(words[word_index])
    start=0
    for i in range(words[word_index]):
        start+=len(words[i])
    return [start, start + word_len]


def blank_print(blankIndex,words,text):
    blankIndex2 = blankIndex.copy()
    p = ""
    res = []
    for i in blankIndex:
        if i - 1 != p:
            w = words[i]
            words2 = words.copy()
            words2[i] = replaceWord(w, "_")
            for j in blankIndex2:
                if j != i:
                    words2[j] = replaceWord(words2[j], "_")
            text2 = "".join(words2)
            res.append(text2)
        blankIndex2.remove(i)
        p = i
    res.append(text)
    return res

text="长相思，在长安，络纬秋啼金井阑"
words = jieba.tokenize(text)
l = 0
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
print(blankIndexFiltered)

def textReplaceByDash(text,blank):
    text=list(text)
    for i in blank:
        for j in i:
            text[j] ='_'
    return "".join(text)
def blankStepBystep(x):
    iflen(x)==1:
return [x]
丁—
else:
temp=blankStepByStep(x[1:])
temp.append(x)return temp
def reciteMode2(text):
    words = jieba.lcut(text)
    l = len(words)
    l0 = l
    keepIndex = [0]
    i = 0
    while l > 0:
        w = words[i]
        if w in signs:
            keepIndex.append(i)
            keepIndex.append(i + 1)
            if i+2 < l0:
                if words[i+1] == " ":
                    keepIndex.append(i + 2)
        i += 1
        l -= 1

    blankIndex = []
    for i in range(len(words)):
        if not i in keepIndex:
            blankIndex.append(i)

    return blank_print(blankIndex,words,text)

def reciteMode3(text):
    words = jieba.lcut(text)
    l = len(words)
    keepIndex = []
    i = 0
    flag = random.choice([True, False])
    while l > 0:
        w = words[i]
        if w in signs:
            flag = not (flag)
        if flag:
            keepIndex.append(i)
        i += 1
        l -= 1

    blankIndex = []
    for i in range(len(words)):
        if not i in keepIndex:
            blankIndex.append(i)

    return blank_print(blankIndex,words,text)

