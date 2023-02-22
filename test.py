import random
import pyperclip
import re
from typing import Dict

def my_function():

    status = True
    myRandInt = random.randint(1, 10)

    while(status):
        print('Please choose a number')
        myInput = int(input())

        if(myRandInt == myInput):
            print(f'You guess the number: {myRandInt}')
            status = False


def my_List():
    myList = ['Hernan', 'Gimena']

    print('Please add another item to myList')
    myInput = input()

    myList.insert(len(myList) + 1, myInput)

    print(f'myList now has: {myList}')

def my_Grid():

    myGrid = [['.', '.', '.', '.', '.', '.'],
              ['.', 'O', 'O', '.', '.', '.'],
              ['O', 'O', 'O', 'O', '.', '.'],
              ['O', 'O', 'O', 'O', 'O', '.'],
              ['.', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', '.'],
              ['O', 'O', 'O', 'O', '.', '.'],
              ['.', 'O', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.']]

    for i in range(len(myGrid[0])):
        for j in range(len(myGrid)):
            print(myGrid[j][i], end='')
        print()

def Fantasy_Inventory():

    myInventory = {'rope': 1, "torch": 2, "pickaxe": 1, "cloth": 3}

    for key, value in myInventory.items():
        print(f'Item: {key} - Quantity: {value}')

def addToInventory(inventory, addItems):
    totalItems = 0
    for ele in addItems:
        if ele in inventory:
            inventory[ele] += 1
        else:
            inventory[ele] = 1
    print(f'Inventory:')
    for k, v in inventory.items():
        print(f'{v} {k}')
        totalItems += int(v)
    print('')
    print(f'Total Number of Items: {totalItems}')

myInv = {'Silver_Coin': 27, 'Cloth': 44}
addItems = ['Gold_Coin', 'Pickaxe', 'Silver_Coin', 'Silver_Coin', 'Silver_Coin', 'Gold_Coin']

def Open_File():
    print('Please enter your text: ')
    myInput = input()

    myFile = open('test.txt', 'a')
    myFile.write(f'{myInput}\n')
    myFile.close()
    myFile = open('text.txt', 'a')
    myOpenFile = open('test.txt')
    myContent = myOpenFile.read()
    print(myContent)

def Copy_Paster():
    myCopy = pyperclip.paste()
    print(myCopy)

def Search_Word():

    p = 'The NOUN panda walked to the ADJECTIVE and then VERB. A nearby NOUN was unaffected by these events'
    pattern = re.search(r'(\bNOUN\b).*(\bADJECTIVE\b).*(\bVERB\b)', p)
    if pattern:
        print('Enter a Noun: ', end='')
        new_noun = re.sub(r'NOUN', f'\1{input()}', p)
        print('Enter an Adjective: ', end='')
        new_adjective = re.sub(r'ADJECTIVE', f'\1{input()}', new_noun)
        print('Enter a Verb: ', end='')
        new_verb = re.sub(r'VERB', f'\1{input()}', new_adjective)
        print(new_verb)
        myFile = open('/media/DriverH/Python/test.txt', 'a')
        myFile.write(f'{new_verb}')
        myFile.close()
    else:
        print('It doesnt have.')

Search_Word()
