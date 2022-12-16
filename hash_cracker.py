import hashlib
from posixpath import split
import pyfiglet

ascii_banner = pyfiglet.figlet_format("No-Link \n Python 4 Pentesters \n HASH CRACKER for MD 5")
print(ascii_banner)


print("Note: This script is for ethical use only..")
print("MD5 Hash Cracker! version:1.0.0")
print("                                             ")
print(" +=========================================+ ")
print(" |..........MD5 Hash Cracker v 1...........| ")
print(" +-----------------------------------------+ ")
print(" |#Author: samSep1ol                       | ")
print(" |#Contact: www.facebook.com/   | ")
print(" |#This tool is made for pentesting.       | ")
print(" |#Website: www.nowebsite.com              | ")
print(" +=========================================+ ")
print(" |.........Thank You From samSep1ol .......| ")
print(" +-----------------------------------------+ ")
print("                                             ")
print("                                             ")

type_of_hash = input("Enter type of hash (md5 or sha256): ")
hash_object = None

while(type_of_hash.lower() != 'md5' and type_of_hash.lower() != 'sha256'):
    print("Unrecognized hash format, please try again")
    type_of_hash = input("Enter type of hash (md5 or sha256): ")

wordlist_location = input("Enter the location of the wordlist that you would like to use")
hash_input = str(input('Enter hash to be cracked: '))
print("\n")

try:
    reading_dic = open(wordlist_location, "r")
    pass_list = reading_dic.readlines()

except: 
    print(" ")
    print("No wordlist was found")



def cracker():
    try:
        for line in pass_list:
            split_line = line.split("\n")
            print("Trying current passworad: ", split_line[0])

            if type_of_hash.lower() == 'md5':
                hash_object = hashlib.md5(split_line[0].encode())
            elif type_of_hash.lower() == 'sha256':
                hash_object = hashlib.sha256(split_line[0].encode())

            x = hash_object.hexdigest()
            if hash_input == x:
                print(" ")
                print("--------- Congratulations! password cracked successfully ---------")
                print("----------Your password is: ",split_line[0])
                break
            else:
                print(f"{split_line[0]} is incorrect password")
                print(" ")
                continue
    except Exception as e:
        print("Encountered an error", e)
    


if __name__ == '__main__':
    cracker()