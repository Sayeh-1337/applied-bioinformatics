# Simple Python Script for First Day

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

def readfile():
    readMyfile = open("seq.txt", "r").readlines()
    seq = []
    for sequence in readMyfile:
        sequence = sequence.strip()
        if sequence.startswith("A") or sequence.startswith("T"):
            print(sequence)
            seq.append(sequence)
    return seq
def complimant(seq): # have issue in A and T as it sequenctial repalcment
    for seq1 in seq:
        #print("Seq=",seq1)
        seq1= seq1.replace("A","T")
        seq1= seq1.replace("T","A")
        seq1= seq1.replace("C","G")
        seq1= seq1.replace("G","C")
        print(seq1)
# Press the green button in the gutter to run the script.

#Right function for the for compliment
def complement2(seq):
    trans=""
    trans = trans.maketrans("ACGT", "TGCA")
    for seq1 in seq:
        seq1 = seq1.translate(trans)
        print(seq1)

# Reverse complement Funion
def rev_complement(seq):
    trans = ""
    trans = trans.maketrans("ACGT", "TGCA")
    for seq1 in seq:
        seq1 = seq1.translate(trans)[::-1]
        print(seq1)

#Main -> Starting point of the program
if __name__ == '__main__':
    #counter=0
    # while counter < 10:
    #     print("ATGCTT")
    #     print(counter)
    #     counter += 1
    #print_hi('My Name Muhammad ')
    seq = readfile() # Read sequence from file and print it
    print("\n")
    complimant(seq) #not the best complement function is totally wrong
    print("\n")
    complement2(seq) #best implementation with good performance
    print("\n")
    rev_complement(seq) #best reverse complement impelmentation with good performance

### End of file
