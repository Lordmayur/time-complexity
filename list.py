# all about list

list=["apple","ball","cat"]
print(list)

#finding length of list
print(len(list))

#adding element to list
list.append("dog")
print(list)

#replacing element from list
list[1:3]="elephant","fish"
print(list)

#extending the list
mylist=["goat","house","ice"]
list.extend(mylist)
print(list)

#removing value from list
list.pop(0)
print(list)