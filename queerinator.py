
class TuringMachine:
    def __init__(self, file):
        __alphabet__ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "#", "!"}
        __tape__ = self.init_tape(file)

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
                new_tape = new_tape[:i+1]
                break   

        if display_mode == True:
            print("Succesfully initialised tape on Turing Machine!")
            print(new_tape)
        #init_type includes Beg function from scheme - exiting method causes the "head" to move to the first element of tape
        return new_tape
            
if __name__ == "__main__":
    A = TuringMachine("69.txt")
    print("get pytonged")
"""
- zczytywanie z pliku DONE
    - znalezienie pierwszego znaku
    - walidacja (cyfry od 0 do 9)
- zmiana dziesiętnego na binarny - jedna taśma
- zdefiniować stany
    - mam jedną pierdoloną...
    - 0-F + # + !
- zdefiniować stan - akcja 

##### 1 0 1 0 1 1 1 1 1 1 ! ### -> forma po dec -> binary 
## ! wynik ! ####
"""