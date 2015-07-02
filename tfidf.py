# coding:utf-8

import codecs
import jieba
import math


def readFile():
	global lineCount
	dicIndex=1
	with codecs.open('baidu.article','r','utf-8') as f:
		for line in f.readlines(1000):
			if line != u'\r\n':
				lineCount += 1
				seglist = jieba.cut(line)
				for eachseg in set(seglist):
					if eachseg not in worddictionary:
						worddictionary[eachseg]=dicIndex
						wordcount[eachseg]=1
						dicIndex += 1
					else:
						wordcount[eachseg] += 1
				tfList.append(caltf(line))
	calidf()
			
def caltf(line):
	tfdic={}
	segs=jieba.cut(line)
	for word in segs:
		tfdic[worddictionary[word]] += 1
	return tfdic
		
		
	
def calidf():
	global lineCount
	idfdic={}
	for k,v in wordcount.items():
		idfValue = math.log(lineCount/v)
		idfdic[k]=idfValue
	return idfdic

if __name__=='__main__':
	worddictionary={}
	wordcount={}
	lineCount = 0
	tfList=[]
	readFile()
	
