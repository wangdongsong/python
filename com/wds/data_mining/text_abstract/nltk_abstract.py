# -*- coding: utf-8 -*-
"""
Created on 2018/1/14 11:44

基于NLTK的文本摘要

方法：为文本样本中的每个句子分词，然后选择出现最频繁的词语，排除不需要的词语（停顿词），最后
找出包含重要词语的句子。

@author: wangdongsong1229@163.com
"""

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from collections import OrderedDict
import pprint

text = "All invoices are up-to-date, " \
       "although it turns out that Virtual were still under the impression that one " \
       "of our previous sponsors who have indicated they are unable to renew was still invoiced. "\
       " I'm not sure how this happened or at what point in the process the sponsor was invoiced. " \
        " Hopefully the process improvements will minimize such errors in the future."\
        " We are currently $64k behind sponsorship income projections for 2016 (though our overall budget"\
        " remains in good shape since we have spent less than projected as well as received less than projected - current worst case puts us at -$138k by financial year end against a budgeted $161k)."\
        " It's time for the November 2015-January 2016 quarterly report. All those officers who have not yet submitted their report for Sally"\
        " should do so in the next couple of days (it's quick and simple, just review your board reports for this period, select the key pieces and send to Sally who can add any necessary colour)."\
        " New visual identity is live - I am still shocked at how easy this was from my perspective, and that of our members. "\
        " A testament to the sensitive handling of a potentially sensitive topic."

summary_sentences = []
candidate_sentences = {}
candidate_sentence_counts = {}

#去掉文本中的回车符
striptext = text.replace("\n\n", " ")
striptext = striptext.replace("\n", " ")

#获取文件中最频繁出现的20个单词的列表，将文件样本转换为单词，转换成小写，确保删除通用的词和标点符号
words = word_tokenize(striptext)
lowercase_words = [word.lower() for word in words if word not in stopwords.words() and word.isalpha()]

#用FreeDist程序包寻找其余单词的频度分布，用most_common()函数从这个列表中找出前20个单词。
word_frequencies = FreqDist(lowercase_words)
most_frequent_words = FreqDist(lowercase_words).most_common(5)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(most_frequent_words)

#获取剥离后的文本样本，并将其侵害为一个句子列表，对于每个句子，我们将创建一个扁，以句子本身为键码，以其小写等价句子为值
sentences = sent_tokenize(striptext)
for sentence in sentences:
    candidate_sentences[sentence] = sentence.lower()

#确定重要的句子

for long, short in candidate_sentences.items():
    count = 0
    for freq_word, frequency_score in most_frequent_words:
        if freq_word in short:
            count += frequency_score
            candidate_sentence_counts[long] = count

#排序句子
sorted_sentences = OrderedDict(sorted(candidate_sentence_counts.items(), key = lambda  x: x[1], reverse = True)[:4])
pp.pprint(sorted_sentences)

