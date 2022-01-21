import os
import math
def has_more_vowels(word:str):
    #given a string of characters, return True if it contains more vowels than consonants,
    #None if they're equal in occurrence,
    #False if consonants occur more than vowels.
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q','r', 's', 't', 'v', 'w', 'x','z']
    word = word.lower()
    vowel_count = 0; # stores vowel count
    consonant_count = 0; # stores consonant count
    for character in word: # counts the occurrence of each vowel and consonants.
        if character in vowels: vowel_count+=1
        elif character in consonants: consonant_count +=1;
    if vowel_count > consonant_count: return True
    elif vowel_count == consonant_count: return None
    else: return False
print(has_more_vowels("Software"))


def calc_cylinder_volume(height:float, radius:float)->float: # compute the volume of a cylinder given height and radisu
    return round((math.pi*height*(radius**2)),2)
print(calc_cylinder_volume(9,8))


def join_list(words:list)->str: #join words from an input list with commas.
    return ','.join(words)
print(join_list(['alphabet', 'word', 'idea', 'sentence', 'proposition']))

#function to write to a file.

def write_to_file(words):
    file_ = "hw3.txt";
    current_path = os.path.abspath(os.getcwd())
    f = open(file_, mode = "w")
    for item in words:
        f.write(join_list(item))
        f.write("\n")
    f.close()
    return  os.path.join(current_path, file_)
a_path = (write_to_file([['we', 'are', 'the', 'champions',  'my friends'],
['we\'ll', 'keep', 'on', 'fighting'], ['to', 'the','end']]))

#function to read from a file 
def read_from_file(path_):
    f = open(path_)
    file_content = f.readlines()
    output = []
    for item in file_content:
        output.append(item.split(','))
    for item in output:
        temp = item[len(item)-1]
        item.remove(temp)
        item.append(temp[0:len(temp)-1])
    return output
read_from_file(a_path)

#function to perform divison
def divide(divisor, dividend):
    try:
        quotient = dividend/ divisor;
    except ZeroDivisionError:
        print("Zero-division isn't allowed. Change the dividend any other number but zero.")
    else:
        print(round(quotient,2))
divide(3,-7)

#function to remove duplicate elements from a list.
def remove_duplicates(arr: list):
    wo_duplicates = set()
    for item in arr:
        wo_duplicates.add(item)
    return list(wo_duplicates)

print(remove_duplicates([1,2,3,1,2,3,4,4,4,4,4]))
def create_folder(folder_name:str):
    try:
        os.mkdir(folder_name)
    except OSError:
        print("Failed to create",folder_name,"folder in", os.path.abspath(os.getcwd()))
    else:
        print(folder_name," has been created in ", os.path.abspath(os.getcwd()))
create_folder("hw3_problem8")