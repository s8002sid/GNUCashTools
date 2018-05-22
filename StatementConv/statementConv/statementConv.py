from Statement import Statement;
from ExportStatement import *;
from StatementParser import *;
from UserSettings import *;
import re;
from Utility.Utility import Utility;
from TransactionReader import *;

#sidSet = SiddharthSetting('SBI', r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\Statement\Bank\Sid\SBI_2017-2018.xls');
#sidSet = SiddharthSetting('MF', r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\Statement\MutualFund\Sid\NOB_201712.xls');
#sidSet = ShreyanshSetting('BOB', r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\Statement\Bank\Bro\BOB_2017-2018.xls');

#ssidSet = GNUCashSetting('GNU', r'C:\Users\siddjain\Documents\allTransaction.csv');
#transactions = sidSet.reader.Read(sidSet.inputFile);
#statement=Statement(transactions, sidSet.statementParser, sidSet.fullAccountPath, sidSet.ttMapFName, sidSet.atMapFName);
#simpleStatementExporter = SimpleStatementExporter(statement);
#nonUpdatedStatementExporter = NonUpdatedStatement(statement);
#gnucashFormat = GNUCashStatement(statement);

#Utility.WriteStatement(simpleStatementExporter, sidSet.outputSimpleTransaction);
#Utility.WriteStatement(nonUpdatedStatementExporter, sidSet.outputMissedTransaction);
#Utility.WriteStatement(gnucashFormat, sidSet.outputGNUCashFormat);

#statement.WriteWordStat(r"output\WordStat.txt");

sidSet = GNUCashSetting('GNU', r'C:\Users\siddjain\Documents\excludingDipti.csv');
transactions = sidSet.reader.Read(sidSet.inputFile);
statement=Statement(transactions, sidSet.statementParser, sidSet.fullAccountPath, sidSet.ttMapFName, sidSet.atMapFName);
statement.WriteWordStat(r"output\WordStat.txt");
vrStatementExporter = ValueResearchStatement(statement);
Utility.WriteStatement(vrStatementExporter, r'output\vrStatement.csv');

nonUpdatedStatementExporter = NonUpdatedStatement(statement);
Utility.WriteStatement(nonUpdatedStatementExporter, sidSet.outputMissedTransaction);