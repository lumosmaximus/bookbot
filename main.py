total_words = 0
counts = {}
file = "books/frankenstein.txt"
def count_letters(text):
    for i in text.lower():
        if  i >= 'a' and i <= 'z':
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

def print_report(filename):
    print(f"--- Begin report of {filename} ---")
    print(f"{total_words} words founbd in the document")
    print()
    report = []
    for i in counts:
        report.append((counts[i],i))
    report.sort(reverse=True)
    for i in report:
        print(f"The '{i[1]}' character was found {i[0]} times")
    print("--- End report ---")

with open(file) as f:
    file_conents = f.read() 
    #print (type(file_conents))
    words = file_conents.split()
    #print(words)
    total_words += len(words)
    count_letters(file_conents)
print_report(file)
