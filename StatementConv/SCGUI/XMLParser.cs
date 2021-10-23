using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;
namespace SCGUI
{
    class SCXMLParser
    {
        public static Dictionary<String, Data> Parse(string file)
        {
            Dictionary<String, Data> db = new Dictionary<String, Data>();
            int parseData = 0, parseName = 0, parseValue = 0, parseBankEntries = 0, parseBank = 0;
            string val;
            XmlTextReader reader = new XmlTextReader("db.xml");
            Data d = new Data();
            while (reader.Read())
            {
                switch (reader.NodeType)
                {
                    case XmlNodeType.Element:
                        switch (reader.Name)
                        {
                            case "Data":
                                parseData = 1;
                                break;
                            case "Name":
                                d = new Data();
                                parseName = 1;
                                break;
                            case "Value":
                                parseValue = 1;
                                break;
                            case "BankEntries":
                                d.bankAndMap = new Dictionary<string, KeyValuePair<string, string>>();
                                parseBankEntries = 1;
                                break;
                            case "Bank":
                                parseBank = 1;
                                break;
                        }
                        break;
                    case XmlNodeType.Text:
                        if (parseValue == 1)
                        {
                            d.name = reader.Value;
                        }
                        else if (parseBank == 1)
                        {
                            d.bankAndMap.Add(reader.Value, new KeyValuePair<string, string>("TTMap-" + reader.Value + "-" + d.name + ".txt", ""));
                        }
                        break;
                    case XmlNodeType.EndElement:
                        switch (reader.Name)
                        {
                            case "Data":
                                parseData = 0;
                                break;
                            case "Name":
                                parseName = 0;
                                d.bankAndMap.Add("MF", new KeyValuePair<string, string>("TTMap-MF-" + d.name + ".txt", "ATMap-MF-" + d.name + ".txt"));
                                db.Add(d.name, d);
                                break;
                            case "Value":
                                parseValue = 0;
                                break;
                            case "BankEntries":
                                parseBankEntries = 0;
                                break;
                            case "Bank":
                                parseBank = 0;
                                break;
                        }
                        break;
                }
            }
            return db;
        }
    }
}
