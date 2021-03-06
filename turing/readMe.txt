Welcome to Turing Machine manual!

Table of contents:
    1. Input form
    2. Alphabet definition rules
    3. Tape definition rules
    4. State definition rules
    5. Working algorithm
    6. Additional information about input
    7. UI 

    
=================================================================================
1. Expected input has a short form of:
    First line: Alphabet 
    Second line: Tape (input for algorithm)
    (N + 2)th line: State definiton 
=================================================================================
2. Rules about alphabet: 
    - Can't include # symbol as it's synonymous for blank space
    - Can't include / symbol as it's a comment sign for definition file
    - All other symbols are legal and must be separated by " " (space)

Ex. alphabet:

    0 1 2 3

=================================================================================
3. Rules about tape:
    - Can't include spaces 
    - Must include alphabet symbols
    - Can include # 
=================================================================================
4. General rules about states:
    - There must be at least one defined qinit state
    - Can't define fin state
    - There must be at least one state that leads to fin state
    - There can't be two states that have same start_state name and input symbol
    - All next_states besides fin must have definitions

Form of state:

    start_state, read_symbol, next_state, write_symbol, dir

Rules about the form of state input:
    - data must be separated by ", " - colon and space
    - read_symbol and write_symbol must be in the scope of the alphabet
    - dir symbol can only be in form of:
            > - meaning move to the right
            < - meaning move to the left 

=================================================================================
5. Example working algorithm - binary negation:

1 0
1000100101
qinit, 1, qinit, 1, >
qinit, 0, qinit, 0, >
qinit, #, pass, #, <
pass, 1, pass, 1, <
pass, 0, pass, 0, <
pass, #, neg, #, >
neg, 1, neg, 0, >
neg, 0, neg, 1, >
neg, #, fin, #, >

=================================================================================
6. There are two symbols ignored by translator in definition file:
    - "/" - can be used for commenting inside file
    - "\n" - enter will be ignored 

=================================================================================
7. UI manual:
        #creating TuringMachine class object
        Turing = TuringMachine("definition_file.txt")

        #Let's user show readMe inside terminal, by default uses current folder directory
        Turing.readMe()
        Turing.readme("file_directory/readMe.txt")

        #Shows output on tape generated by algorithm, optionally can show output without defined symbols
        T.show_output()
        T.show_output(["#", "!"])