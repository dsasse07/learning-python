new_list = []

# Add Item with .append
print(' Add item with .append')
new_list.append(10)
new_list.append(20)
new_list.append(30)
new_list.append(40)
print('new list', new_list)


# Remove item from end of list and return
print('Remove item from end of list and return with .pop()')
last_item = new_list.pop()
print('last item', last_item)
print(new_list)

# Remove two items from SPECIFIC INDEX
print('Remove two items from SPECIFIC INDEX with .pop(index)')
item_at_index_two = new_list.pop(2)
print('item at new_list[2]', item_at_index_two)
print(new_list)

# Does list contain item?
print('Does list contain item? (x in list)')
print("10 in the list?", 10 in new_list) #true
print('100 in the list?', 100 in new_list) #false 

#Find and remove the first occurence of an item in the list
print('Find and remove the first occurence of an item in the list with .remove()')
first_ten = new_list.remove(10)
print('first ten', first_ten) #NONE - Remove does not return value
print('new_list', new_list)

# Combine Lists (concat) using .extend
print('Combine Lists (concat) using .extend')
list_one = ['a','b','c']
list_two = ['d','e','f']
print('list_one', list_one)
print('list_two', list_two)
list_one.extend(list_two)
print('list one extended by list 2', list_one)

## Using + on a list functions like extend, but creates a new list
print('Using + on a list')
list_a = ['a','b','c']
list_b = ['d','e','f']
combined_list = list_a + list_b
print('combined lists', combined_list)
print('list_a unchanged', list_a)
print('list_b unchanged', list_b)

# Find the index of an element in a list
print('Find the index of an element in a list with .index()')
print('list_a', list_a)
print('Index of "a"', list_a.index('a'))
print('Unfound items throw error')

# Insert, inserts item into list at specific element
print('Insert element at index with .insert(index, el)')
print('list_a', list_a)
list_a.insert(1,'d')
print('list_a.insert(1,"d")', list_a)

# Duplicate a list with .copy()
list_a_copy = list_a.copy()
print('list_a_copy = list_a.copy()')
print('list_a.pop()', list_a.pop())
print('list_a', list_a)
print('list_a_copy', list_a_copy)

# Find min/max value in list
print(' use max() and min() to find extreme value sin list')
num_list = [1,100,-20,14]
print('num_list', num_list)
print('max(num_list)', max(num_list))
print('num_list', min(num_list))

#Find array sum with sum()
print(' use sum() to sum values in list')
num_list = [1,100,-20,14]
print('num_list', num_list)
print('sum(num_list)', sum(num_list))


