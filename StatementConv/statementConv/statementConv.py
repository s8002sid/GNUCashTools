from Statement import Statement;
from ExportStatement import *;
from StatementParser import *;
from UserSettings import *;
import re;
from Utility.Utility import Utility;
from TransactionReader import *;

def WriteGNUCTransaction(wordStatFile, set):
    transactions = set.reader.Read(set.inputFile);
    statement=Statement(transactions, set.statementParser, set.fullAccountPath, set.ttMapFName, set.atMapFName);
    nonUpdatedStatementExporter = NonUpdatedStatement(statement);
    simpleStatementExporter = SimpleStatementExporter(statement);
    gnucashFormat = GNUCashStatement(statement);
    Utility.WriteStatement(simpleStatementExporter, set.outputSimpleTransaction);
    Utility.WriteStatement(nonUpdatedStatementExporter, set.outputMissedTransaction);
    Utility.WriteStatement(gnucashFormat, set.outputGNUCashFormat);
    statement.WriteWordStat(wordStatFile);

#Dipti SBI Account Generator
#set = DiptiSetting('SBI', r'C:\Users\siddjain\Google Drive\Home\Share\Dipti-Share\Document\Account\Statement\Bank\SBI_2017-2018.xls');

#Mom BOB Account Generator
#set = MomSetting('BOB', r'C:\Users\siddjain\Google Drive\Home\Share\Chandra-Share\Document\Account\Statement\BOB_2017-2018.xls');

#Mom HDFC Account Generator
#set = MomSetting('HDFC', r'C:\Users\siddjain\Google Drive\Home\Share\Chandra-Share\Document\Account\Statement\2017-2018.xls');

#Shweta HDFC Account Generator
#set = ShwetaSetting('HDFC', r'C:\Users\siddjain\Google Drive\Home\Share\Shweta-Share\Document\Account\Statement\Bank\2017-2018.xls');

#Dad AllahabadBank Setting
#set = DadSetting('AllahabadBank', r'C:\Users\siddjain\Google Drive\Home\Share\Dilip-Share\Document\Account\Statement\Bank\2017-2018-04-08.xls');
#set = DadSetting('AllahabadBank', r'C:\Users\siddjain\Google Drive\Home\Share\Dilip-Share\Document\Account\Statement\Bank\2017-2018-09-01.xls');
#set = DadSetting('AllahabadBank', r'C:\Users\siddjain\Google Drive\Home\Share\Dilip-Share\Document\Account\Statement\Bank\2017-2018-02-03.xls');
set = DadSetting('IDBI', r'C:\Users\siddjain\Google Drive\Home\Share\Dilip-Share\Document\Account\Statement\Bank\IDBI_2017-2018.xls');
WriteGNUCTransaction(r"output\WordStat.txt", set);

#set = DiptiSetting('HDFC', r'C:\Users\siddjain\Google Drive\Home\Share\Dipti-Share\Document\Account\Statement\Bank\2017-2018.xls');


#sidSet = SiddharthSetting('SBI', r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\Statement\Bank\Sid\SBI_2017-2018.xls');
#sidSet = SiddharthSetting('MF', r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\Statement\MutualFund\Sid\NOB_201712.xls');
#sidSet = ShreyanshSetting('BOB', r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\Statement\Bank\Bro\BOB_2017-2018.xls');


#transactions = sidSet.reader.Read(sidSet.inputFile);
#statement=Statement(transactions, sidSet.statementParser, sidSet.fullAccountPath, sidSet.ttMapFName, sidSet.atMapFName);
#simpleStatementExporter = SimpleStatementExporter(statement);
#nonUpdatedStatementExporter = NonUpdatedStatement(statement);
#gnucashFormat = GNUCashStatement(statement);

#Utility.WriteStatement(simpleStatementExporter, sidSet.outputSimpleTransaction);
#Utility.WriteStatement(nonUpdatedStatementExporter, sidSet.outputMissedTransaction);
#Utility.WriteStatement(gnucashFormat, sidSet.outputGNUCashFormat);

#statement.WriteWordStat(r"output\WordStat.txt");

#sidSet = DiptiSetting('GNU', r'C:\Users\siddjain\Documents\excludingDipti.csv');
#transactions = sidSet.reader.Read(sidSet.inputFile);
#statement=Statement(transactions, sidSet.statementParser, sidSet.fullAccountPath, sidSet.ttMapFName, sidSet.atMapFName);
#statement.WriteWordStat(r"output\WordStat.txt");
#vrStatementExporter = ValueResearchStatement(statement);
#Utility.WriteStatement(vrStatementExporter, r'output\vrStatement.csv');

#nonUpdatedStatementExporter = NonUpdatedStatement(statement);
#Utility.WriteStatement(nonUpdatedStatementExporter, sidSet.outputMissedTransaction);