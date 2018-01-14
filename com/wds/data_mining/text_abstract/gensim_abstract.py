# -*- coding: utf-8 -*-
"""
Created on 2018/1/14 13:04

Gensim方法的文本自动化

@author: wangdongsong1229@163.com
"""
import gensim.summarization

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

striptext = text.replace("\n\n", " ")
striptext = striptext.replace("\n", " ")

summary = gensim.summarization.summarize(striptext, word_count=20)
print(summary)

##关键字的选择并打印
keywords = gensim.summarization.keywords(striptext)
print(keywords)
