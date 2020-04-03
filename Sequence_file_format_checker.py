#usr/bin/python3

print(
    """
    This simple script checks and tells
    the file format of a sequence file fwd in
    
    """
    )
    
def __seq_file_feed(ref_seq):
    f = open(ref_seq, "r")
    if(f.readline[0] == ">"):
        print("File.is fasta format")
    else:
        print("File is not fasta")