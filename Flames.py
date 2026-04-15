# Input names
name1 = "masood"
name2 = "siri"

list1 = list(name1.lower())
list2 = list(name2.lower())


temp_list1 = list(list1)


# Removing Matching chars from both names.
for char in temp_list1:
    if char in list2:
        list1.remove(char)
        list2.remove(char)
flames_no = len(list1) + len(list2)


# Check if the result is not zero
if flames_no == 0:
    print("There is no Chararcters Left")

else:

    flames_list = ['F', 'L', 'A', 'M', 'E', 'S']

    current_position = 0

    # Main Algorithm
    while len(flames_list) > 1:
        flames_list_len = len(flames_list)

        index_to_remove = (current_position + flames_no - 1) % flames_list_len
    
        removed_char = flames_list.pop(index_to_remove)
    
        current_position = index_to_remove % len(flames_list)


    # Flames Meaning
    final_result_char = flames_list[0]
    flames_meaning = {
        'F': 'Friendship',
        'L': 'Love',
        'A': 'Attraction/Affection',
        'M': 'Marriage',
        'E': 'Enemy',
        'S': 'Sibling'
    }

    print(f'{flames_meaning[final_result_char]}!')


                              # Looks neat right? 