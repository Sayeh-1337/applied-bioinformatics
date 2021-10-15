

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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

def rev_complement(seq):
    trans = ""
    trans = trans.maketrans("ACGT", "TGCA")
    for seq1 in seq:
        seq1 = seq1.translate(trans)[::-1]
        print(seq1)
if __name__ == '__main__':
    #counter=0
    # while counter < 10:
    #     print("ATGCTT")
    #     print(counter)
    #     counter += 1
    #print_hi('My Name Muhammad ')
    seq = readfile()
    print("\n")
    complimant(seq)
    print("\n")
    complement2(seq)
    print("\n")
    rev_complement(seq)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
