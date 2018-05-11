import re;
class CSV:
    @staticmethod
    def Tokenize(line):
        p=re.compile ('[^"]*("[^"^,]*,?[^"]*")*[^"]*');
        m=p.findall(line);
        for i in range(len(m)):
            if(m[i] != ''):
                m1=m[i].replace('"','').replace(',',' ');
                line = line.replace(m[i],m1);
        return line.split(",");