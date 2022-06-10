
class TuringMachine:
    def __init__(self, file):
        f = open(file, "r")
        self.__alphabet__ = self.init_alphabet(f)
        self.__tape__ = self.init_tape(f)
        self.__states__ = self.init_states(f)
    
    def init_alphabet(self, f):
        alphabet = list(f.readline())
        while " " in alphabet:
            alphabet.pop(alphabet.index(" "))
        alphabet = set(alphabet)
        if "#" in alphabet:
            raise NotImplementedError("Err7: Predefined symbol as part of the alphabet!")
        return alphabet.union({'#'})

    def init_tape(self, f):
        tape = f.readline()
        tape = tape.replace('\n', "")
        symbols = set(tape)
        if symbols | self.__alphabet__ != self.__alphabet__:
            raise NotImplementedError("Err8: Tape consists of symbols outside of defined alphabet")
        return list(tape)

    def init_states(self, f):
        new_states = list()
        for i in f:
            i = i.replace('\n', "")
            s = i.split(", ")
            for j in range(0, len(s)):
                if s[j] == ' ': raise NotImplementedError("Err6: Used space symbol as part of input!")
                if '\n' in set(s[j]): s[j] = s[j][0] 
            if len(s) != 5:
                raise NotImplementedError("Err2: Wrong number of inputs")
            defs = [[i.__name__, i.__in__] for i in new_states]
            if [s[0], s[1]] in defs:
                raise NotImplementedError("Err3: State with given definition already exists")
            if (s[1] in self.__alphabet__ and s[3] in self.__alphabet__) == False:
                raise NotImplementedError("Err4: Given symbols not in alphabet!")
            if s[4] != '<' and s[4] != '>':
                raise NotImplementedError("Err5: Undefined symbol indicating move!")
            new_states.append(State(s[0], s[1], s[2], s[3], s[4]))
        
        names = [i.__name__ for i in new_states]
        names_to = [i.__nstate__ for i in new_states]
        if "fin" in names:
            raise NotImplementedError("Err10: Used predefined named of state: fin")
        if "qinit" not in names:
            raise NotImplementedError("Err11: Didnt define initialising state(s)")
        if "fin" not in names_to:
          
            raise NotImplementedError("Err12: Didnt define final state(s)")
        return new_states
    
    def create_dic(self):
        dic = {}
        for i in self.__states__:
            if dic.get(i.__name__) == None:
                dic[i.__name__] = {i.__in__: [i.__nstate__, i.__out__, i.__d__]}
            else: 
                dic[i.__name__][i.__in__] = [i.__nstate__, i.__out__, i.__d__]
        print(dic.keys())
        for i in dic.keys():
            for j in dic[i].keys():
                print("Key: " + str(i) + " has value of " + str(j) + " " + str(dic[i][j]) )
        return dic

    def execute(self):
        _finished = False 
        index = 0
         
        while(_finished != True):
            print("Nice cock")





class State:
    def __init__(self, name, input, state_to, output, dir):
        self.__name__ = name
        self.__in__ = input
        self.__nstate__ = state_to
        self.__out__ = output
        self.__d__  = dir

    def move(self):
        return self.__d__

if __name__ == "__main__":
    T = TuringMachine("69.txt")
    d = { "A": 1, "B": 2 }

    #print(T.__alphabet__)
    T.create_dic()


"""
Example input:
1. line - A B C D E F G - alphabet definition
2. qinit:
    - lista stanów inicjujących 
    fin
3. tape - 1293 - dec num 

"""       