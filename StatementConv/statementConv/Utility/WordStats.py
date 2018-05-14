import re;
class StatementAnalyzer(object):
    def __init__(self):
        self.wordDict = {};
    def AddStatement(self, statement):
        p = re.compile('[\w\d]+');
        words = p.findall(statement);
        words = [e.lower() for e in words];
        for i in range(len(words)):
            if (words[i] in self.wordDict):
                self.wordDict[words[i]] = self.wordDict[words[i]]+1;
            else:
                self.wordDict[words[i]] = 1;
    def GetSortedWordList(self):
        sortedList = [];
        for key, value in sorted(self.wordDict.iteritems(), key=lambda (k,v): (v,k), reverse = True):
            sortedList.append([key, value]);
        return sortedList;

    def WriteSortedWordList(self, fileName):
        sortedList = self.GetSortedWordList();
        toWrite = [];
        for i in range(len(sortedList)):
            x = sortedList[i][0] + ',' + str(sortedList[i][1]);
            toWrite.append(x);
        fob = open(fileName, "w");
        fob.write('\n'.join(toWrite));
        fob.close();
        