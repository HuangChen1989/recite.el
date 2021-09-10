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
elif mode=="sentence2":
    reciteMode="3"
else:
    reciteMode = random.choice(["1","2","3"])


signs = ["，", "。", "！", "？", "“", "”", "《", "》", "（", "）","、","；",",","."," ","-","!",";","?","'"," ","\n"]

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

def reciteMode1(text):
    words = jieba.lcut(text)
    l = 0
    for i in words:
        if not i in signs:
            l += 1
    l = l / 2
    blankIndex = []
    while l > 0:
        randomIndex = random.choice(range(len(words)))
        w = words[randomIndex]
        if (not w in signs) and (not randomIndex in blankIndex):
            blankIndex.append(randomIndex)
            l -= 1

    blankIndex.sort()
    return blank_print(blankIndex,words,text)

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


output=json.dumps(eval("reciteMode" + reciteMode + "(text)"))
sys.stdout.write(output)
