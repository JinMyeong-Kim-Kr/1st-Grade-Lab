class Codechecker(object):

    def __init__(self):
        self.operator_Character = ['<', '>', '+', '-', '/', '%', '=', '*', '!']
        self.special_Character = [':', ',']
        self.bracket_Character = ['[', ']', '(', ')', '{', '}']
        self.import_Character = ['from', 'import', 'as']
        self.class_Character = 'class'
        self.def_Character = 'def'
        self.return_Character = 'return'

    def semiclone(self, line):
        line = line.rstrip()
        if line[-1] == ';':  # 세미콜론제거
            line = line[:-1]
        try:
            if line.find(';') != -1:
                if line[line.find(';')+1].isalpha() or line[line.find(';')+1] == ' ':
                    if line[line.find(';')+1] == ' ':
                        line = line[:line.find(';')] + '\n' + line[line.find(';') + 2:]
                    else:
                        line = line[:line.find(';')] + '\n' + line[line.find(';') + 1:]
        except:
            return line

        return line

    def operator_check(self,line): #연산자
        string = ""
        for i in line:
            if i not in self.operator_Character:
                string += i
            else:
                string += '@'

        for i in line:
            if i in self.operator_Character:
                while line.find(i) != -1:
                    index = line.find(i)
                    string = string[:index].rstrip() + " " + i + " " + string[index+1:].lstrip()
                    line = line[:index].rstrip() + " " + '@' + " " + line[index + 1:].lstrip()

        try:
            for i in range(len(string)): #a<=b<=c
                if string[i] in self.operator_Character:
                    if string[i+2] in self.operator_Character:
                        string = string[:i+1] + string[i+2:]
            return string
        except:
            return string

    def special_check(self,line): #special2
        string = ""
        for i in line:
            if i not in self.special_Character:
                string += i
            else:
                string += '@'

        for i in line:
            if i in self.special_Character:
                while line.find(i) != -1:
                    index = line.find(i)
                    string = string[:index].rstrip() + i + " " + string[index + 1:].lstrip()
                    line = line[:index].rstrip() + '@' + " " + line[index + 1:].lstrip()
        return string

    def bracket_check(self, line): #special3
        string = ""
        for i in line:
            if i not in self.bracket_Character:
                string += i
            else:
                string += '@'

        for i in line:
            if i in self.bracket_Character:
                while line.find(i) != -1:
                    index = line.find(i)
                    string = string[:index].rstrip() + i + string[index+1:].lstrip()
                    line = line[:index].rstrip() + '@' + line[index + 1:].lstrip()

        return self.operator_check(self.special_check(string))

    def import_check(self,line): #special4
        line = self.special_check(line)
        tmp = line.split()
        string = ""
        string1 = ""
        if line[0] == ' ': #들 #import a, b [import , a, b] index = 0, for i in range(1): string = import ' '여쓰기 되있는 import
            return line
        if tmp[0] == self.import_Character[0]:
            index = tmp.index(self.import_Character[1])
            for i in range(index + 1):
                string = string + tmp[i] + ' '
            for i in range(index + 1, len(tmp)):
                string1 += string + tmp[i] + '\n'
                string1 = string1.replace(',', '')

        elif tmp[0] == self.import_Character[1]:
            string += tmp[0] + ' '
            if line.find('as') != -1:
                return line
            else:
                for i in range(1, len(tmp)):
                    string1 += string + tmp[i] + '\n'
                    string1 = string1.replace(',', '')

        return string1

    def class_check(self, line): #special5
        tmp = line.split()
        if '(' not in tmp[1] and ')' not in tmp[1]:
            index = line.find(':')
            string = line[:index] + '(object)' + line[index:]
        else:
            string = line

        return string

    def def_check(self, line): #special6
        openindex = line.index('(')
        closeindex = line.index(')')
        string = line[openindex:closeindex + 1]
        if string != '':
            for i in string:
                if i in self.operator_Character:
                    characterindex = string.index(i)
                    string = string[:characterindex].rstrip() + i + string[characterindex + 1:].lstrip()
                else:
                    continue
            line = line[:openindex] + string + line[closeindex + 1:]
        else:
            line = line

        return line

    def return_check(self, line): #special7
        tmp = line.split()
        try:
            if tmp[1].find('(') == 0:
                firstindex = line.index('(')
                line = line[:firstindex] + line[firstindex + 1:-1]
            string = ""
            for i in line:
                if i not in self.operator_Character:
                    string += i
                else:
                    string += '@'
        except:
            return line

        for i in line:
            if i in self.operator_Character:
                while line.find(i) != -1:
                    index = line.find(i)
                    string = string[:index].rstrip() + i + string[index + 1:].lstrip()
                    line = line[:index].rstrip() + '@' + line[index + 1:].lstrip()
        return string

if __name__ == "__main__":
    code = Codechecker()
    ex1 = "abc;"
    print(code.semiclone(ex1))
    ex2 = "a=[  ]"
    print(code.bracket_check(ex2))
    ex3 = "from a import a,b,c"
    print(code.import_check(ex3))
    ex4 = "return (abc)"
    print(code.return_check(ex4))
    ex5 = "class abc:"
    print(code.class_check(ex5))
    ex6 = "a=3"
    print(code.operator_check(ex6))
    ex7 = "def abc(x = 0):"
    print(code.def_check(ex7))