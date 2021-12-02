import codecs
import json
import markdownify

strSourcePath = 'd:\\工作\\b2t\\'
strMDPath = 'd:\\工作\\b2t\\markdown\\'


def readjson(strFileName):
    try:
        jsonfin = codecs.open('d:\\工作\\b2t\\thoughts.json', 'r', 'utf-8')
        objthoughts = json.load(jsonfin)
    except Exception as e:
        print(e)
        return None
    else:
        return objthoughts
    
    pass


def scanjson(listjson):
    '''
    return mapping:
    listTupleFileContents=[]
    listJsonLinks = []
#   dictID2Thought = {}

    '''

    dictTupleFileContents={}
    dictJsonLinks = {}
#    dictID2Thought = {}


    for jsonthought in listjson:
        strtitle = str(jsonthought['title'])
        strcontent = ''
        strtitle = strtitle.replace('\\',u'·').replace('/',u'、').replace('*','_').replace('?',u'？').replace('"',u'“').replace('<','《').replace('>','》').replace('|','_').replace(':',u'：')
        #invalid filename chars: ':\/?*"<>|'
        if jsonthought.__contains__('text'):
            strcontent = jsonthought['text']

        if jsonthought.__contains__('tmap.id'):
            strID = jsonthought['tmap.id']
        
            if not dictTupleFileContents.__contains__(strID):
                dictTupleFileContents[strID] = (strtitle, strcontent)
            if jsonthought.__contains__('tmap.edges') and jsonthought['tmap.edges'].__len__() > 2:
                dictEdges = json.loads(jsonthought['tmap.edges'])
                for edge in dict(dictEdges).items():
                    if dictJsonLinks.__contains__(strID):
                        dictJsonLinks[strID].append(dict(edge[1])['to'])
                    else:
                        dictJsonLinks[strID] = [dict(edge[1])['to']]
    

    return dictTupleFileContents, dictJsonLinks
    pass


def writeFileContent(strFileName, strContentHTML):

    strContentMD = markdownify.markdownify(strContentHTML, heading_style="ATX")
    mdout = codecs.open(strMDPath + strFileName + '.md', 'a', 'utf-8')
    mdout.write(strContentMD)
    mdout.close()
    
    pass


def insertlink(strFileName, listLinks):
    mdout = codecs.open(strMDPath + strFileName + '.md', 'a', 'utf-8')
    for strLink in listLinks:
        strLine = '''[[%s]]\n\r''' % strLink
        mdout.writelines(strLine)

    mdout.close()
    pass


strFileName = strSourcePath + 'thoughts.json'
if __name__ == "__main__":

    jsonThought = readjson(strFileName)
    dictTupleFileContents, dictJsonLinks = scanjson(jsonThought)

    
    for item in dict(dictTupleFileContents).items():
        strID = item[0]
        tupleContent = item[1]

        strFileName = tupleContent[0]
        strContent = tupleContent[1]

        listLinkIDs = []
        listLinks = []

        if  dict(dictJsonLinks).__contains__(strID):
            listLinkIDs = dict(dictJsonLinks)[strID]
            for strLinkID in listLinkIDs:
                strLink = dict(dictTupleFileContents)[strLinkID][0]
                listLinks.append(strLink)

        

        writeFileContent(strFileName, strContent)
        insertlink(strFileName, listLinks)


    pass
