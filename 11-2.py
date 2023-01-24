import string

def main ():

    file = input("Ввести імя файлу для заміни : ")
    infile = open(file, 'r')

    otherFile = input("Ввести імя файлу для збереження заміни: ")
    outfile = open(otherFile, 'w')

    for line in infile:
        words = line.split( )
        for word in words:
            counter = 0
            for letter in word:
                if not letter in string.punctuation:
                    counter += 1
            if counter == 4:
                if "." in word:
                    word = "****."
                elif "," in word:
                    word = "****,"
                elif "?" in word:
                    word = "****?"
                elif "!" in word:
                    word = "****!"
                else:
                    word = "****"


            print (word + " ", file = outfile, end = "")

    infile.close()
    outfile.close()

if __name__=='__main__':
    main ()