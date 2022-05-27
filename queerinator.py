import math
from operator import truediv

class TuringMachine:
    def __init__(self, file):
        self.__alphabet__ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "#", "!"}
        self.__tape__ = self.init_tape(file, True)

    def init_tape(self, file, display_mode = False):
        f = open(file, "r")
        source = f.readline()
        dec = [str(i) for i in range(0,10)]
        new_tape = [source[i] for i in range(0, len(source))]
        for i in range(0, len(source)):
            if source[i] not in dec and source[i] != '#':
                raise NotImplementedError("Err1: Wrong input format!")
            if source[i] == "#":
                new_tape.pop(0)
            if source[i] in dec:
                break

        for i in range(0, len(new_tape)):
            if new_tape[i] not in dec and new_tape[i] != "#":
                raise NotImplementedError("Err1: Wrong input format!")
            if new_tape[i] == "#":
                new_tape = new_tape[:i+1] + ["#"]
                break   

        if display_mode == True:
            print("Succesfully initialised tape on Turing Machine!")
            print(new_tape)
        #init_type includes Beg function from scheme - exiting method causes the "head" to move to the first element of tape
        return new_tape
    
    def dec_bin(self):
        add = {str(i): str(i+5) for i in range(0,5)}
        divide = {str(i): str(math.floor(i/2)) for i in range(0,10)}
        odd = {str(i) for i in range(1, 10, 2)}
        even = {str(i) for i in range(0, 10, 2)}
        #bin_tape = []
        tape = self.__tape__
        fin_state = False
        tape[-2] = "0" 
        while(fin_state == False):
            ind = tape.index('#')
            tape[ind-1] = "0"
            for j in range(ind-2, -1, -1):
                if tape[j] in odd:
                    tape[j] = divide[tape[j]]
                    tape[j+1] = add[tape[j+1]]
                elif tape[j] in even:
                    tape[j] = divide[tape[j]]
            
            if tape[ind - 1] == "5":
                tape.append("1")
            elif tape[ind - 1] == "0":
                tape.append("0")
            if tape[0] == "0":
                tape.pop(0)

            if tape[1] == "#":
                fin_state = True
        self.__tape__ = tape[2:] + ["!"]
        print(tape)
        print(self.__tape__ )
            
if __name__ == "__main__":
    A = TuringMachine("69.txt")
    A.dec_bin()
"""
- zczytywanie z pliku DONE
    - znalezienie pierwszego znaku
    - walidacja (cyfry od 0 do 9)
- zmiana dziesiętnego na binarny - jedna taśma DONE
- zdefiniować stany
    - mam jedną pierdoloną...
    - 0-F + # + !
- zdefiniować stan - akcja 

 1 0 1 0 1 1 1 1 1 1 ! -> forma po dec -> binary (stan __tape__) [najmniej znaczacy bit, ..., najbardziej znaczacy bit]
## ! wynik ! ####
"""