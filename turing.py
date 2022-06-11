class TuringMachine:
    def __init__(self, file):
        f = open(file, "r")
        self.__alphabet__ = self.init_alphabet(f)
        self.__tape__ = self.init_tape(f)
        self.__states__ = self.init_states(f)
        f.close()
    
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
        return dic

    def execute(self):
        _finished = False
        index = 0
        c_state = None
        tape = self.__tape__
        dic = self.create_dic()
        if tape[0] in dic["qinit"].keys():
            c_state = dic["qinit"][tape[0]]
        while(_finished != True):
            #first check if machine didnt finish algorithm
            if c_state[0] != "fin":
                #overwrite value
                tape[index] = c_state[1]
                #move header
                if c_state[2] == ">":
                    if index + 1 >= len(tape):
                        tape.append("#")
                    index = index + 1
                else:
                    if index - 1 < 0:
                        tape.insert(0, "#")
                        index = 0
                    else: index = index-1
                #go to next state
                if c_state[0] in dic.keys():
                    if tape[index] in dic[c_state[0]].keys():
                        c_state = dic[c_state[0]][tape[index]]
                    else: raise NotImplementedError("Err14: Tried to reach state that doesn't exists!")
                else: raise NotImplementedError("Err13: Tried to reach state that doesn't exists!")
            else: _finished = True
        print(tape)
        return tape
            

class State:
    def __init__(self, name, input, state_to, output, dir):
        self.__name__ = name
        self.__in__ = input
        self.__nstate__ = state_to
        self.__out__ = output
        self.__d__  = dir

    def move(self):
        return self.__d__

class StateGenerator:
    def __init__(self, file):
        self.__file__ = file
    
    def gen_states(self, state1, state2, r ,dir, incr=1):
        f = open(self.__file__, "a")
        for i in range(r[0], r[1], incr):
            output = [state1, str(i), state2, str(i), dir]
            output = ", ".join(output)
            f.write(output + "\n")
        f.close()
if __name__ == "__main__":
    T = TuringMachine("binToDec.txt")
    a = T.execute()
    #x = StateGenerator("output.txt")
    #x.gen_states("back", "back", [1,10] , ">")


"""
Example input:
1. line - A B C D E F G - alphabet definition
2. qinit:
    - lista stanów inicjujących 
    fin
3. tape - 1293 - dec num 

"""       