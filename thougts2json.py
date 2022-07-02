import csv
import sys
import codecs
import json
import uuid
import collections

AllThoughtLinks = collections.defaultdict(collections.defaultdict)

kk={1,2}
NoteFilePath = '.\\'

def getThoughtNote(thoughtid):
    Notetext=""
    
    try:
        
        NoteFilePath = globals()['NoteFilePath']+thoughtid+"\\Notes\\notes.html"
        NoteFile = codecs.open(NoteFilePath, encoding="utf-8")
        Notetext=NoteFile.read()
    except Exception as e:
        #print(NoteFilePath)
        print(e)
        
        pass

    return Notetext

def getAllLinks():
    csvfile = codecs.open(linksfilepath, encoding='utf-8')
    csvreader = csv.reader(csvfile, delimiter='|')
   # thoughttyddlers=[]
    '''get links in json string'''
    for row in csvreader:
        LinkID=row[16]
        LinkTo=row[1]
        LinkFrom=row[0]
        AllThoughtLinks[LinkFrom][LinkID]={"to":LinkTo,"type":"tmap:unknown"}
        #'''to json''' = .append(row[16]).append(row[1])
        #'''append json by key'''AllThoughtLinks[row[0]]
    pass


def getThoughtLinks(thoughtid):
    thoughtLinksText = json.dumps(AllThoughtLinks[thoughtid])
    return thoughtLinksText

def tcsv2tuple(filepath):
    csvfile = codecs.open(filepath, encoding='utf-8') #test
    csvreader = csv.reader(csvfile, delimiter='|')
    thoughttyddlers=[]
    TitleDict = collections.defaultdict(list)
    '''get links in json string'''
    for row in csvreader:
        #print(row[1],row[16])
        thoughtnote=getThoughtNote(row[18])
        thoughtlinks=getThoughtLinks(row[18])

        title=row[1]
        TitleDict[title].append(0)
        TitleCount = len(TitleDict[title])
        if TitleCount > 1:
            title=title+" " + str(TitleCount)

        thoughttyddler={"title":title, "tmap.id":row[18],"text":thoughtnote,"type": "text/html", "tmap.edges": thoughtlinks}
        thoughttyddlers.append(thoughttyddler)
        

    return thoughttyddlers

if __name__ == "__main__":
    fullpath = '.\\thoughts.txt'
    linksfilepath = '.\\links.txt'
    getAllLinks()
    tiddlers = tcsv2tuple(fullpath)
    jsonfile = codecs.open("thoughts.json", mode="w", encoding='utf-8')
    json.dump(tiddlers,jsonfile,indent=4)
