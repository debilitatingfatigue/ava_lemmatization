from nltk.tokenize import RegexpTokenizer
import pandas as pd
import os
import sys

tokenizer = RegexpTokenizer(r'\w+')
text = tokenizer.tokenize(input().lower())

for word in text:
    cmd = f"echo '{word}' | hfst-lookup ava.analyzer.hfst"
    os.system(cmd)
    
df = pd.DataFrame(columns = ["wordform", "lemma"])

with open("file.txt", "r", encoding="utf-8") as f:
    file = f.read().split('\n')
    for line in file:
        line_split = line.split('\t')
        if len(line_split) >= 2:
            word, lemma = line_split[0], line_split[1]
            df.loc[len(df.index)] = [word, lemma]
    
df.to_csv("Lemmatization.csv", encoding="utf-8", index=False)
