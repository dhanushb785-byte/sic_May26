#print('This is my first program for git')

def linearSearch(elements, searchElement):
    for i in range(len(elements)):
        if elements[i] == searchElement:
            return i
    return -1


elements = []

listSize = int(input('Enter the size of the list: '))

print('Enter the elements:')

for i in range(listSize):
    element = int(input())
    elements.append(element)

searchElement = int(input('Enter the search element: '))

searchElementPosition = linearSearch(elements, searchElement)

if searchElementPosition != -1:
    print(f'The search element is found at index {searchElementPosition}')
else:
    print('Search element not found')