names_numbers = {'santosh': 9860777044, 'sakar': 9460777044, 'tsering': 9860722044, 'babita': 98612137044, 'ajay': 9860777022,
                 'akul': 9860777041,'atul': 9860771041,'Sachin': 9822777041,'Pritam Pani ko dai': 9860777042, 'tsering Topchen': 9860777041,
                 'ambay': 95656865654, 'sarita': 9220334432}
names_numbers_list = []

# count for searching
count = 0
# counts for three_list
counts = 0
# counting for counting_words
counting = 0

# main count list for main counts
main_count_list = []

# code between santosh and sontos
print("WELCOME")
print("SEARCH FOR CONTACT NAMES WITHOUT WORRYING ABOUT SPELLING")
input_name = input("Enter the name you wanna search for: ")

input_name_list = []
for letter in input_name.lower():
    input_name_list.append(letter)

# mid input length of input name//necessary to count for percentage
mid_input_name_list = len(input_name_list) / 2


def equallifying(names_number_list):
    """Equallifying the both list to comparison """

    while (len(input_name_list) != len(names_numbers_list)):

        if (len(input_name_list) > len(names_numbers_list)):
            names_numbers_list.append('|')
            continue

        elif (len(input_name_list) < len(names_numbers_list)):
            input_name_list.append('/')
            continue

        elif (len(input_name_list) == len(names_numbers_list)):
            break


def checking_three_list():
    """Checking three elements one after another for matching elements"""
    global counts
    x = 0
    y = 3
    while (y != x + 2):
        a = input_name_list[x:y]
        b = names_numbers_list[x:y]

        z = set(a).intersection(b)
        if (len(z) > 1):
            counts += 2

        x += 1

        if (y < len(input_name_list)):
            y += 1

    print(f"counts {counts}")


def counting_words():
    """Counting similar words in letters"""
    global counting
    for i in input_name_list:
        if i in names_numbers_list:
            counting += 0.5
    print(counting)


def searching():
    """Searching by matching index of elements"""
    global count
    equallifying(names_numbers_list)
    print(input_name_list)
    print(names_numbers_list)
    checking_three_list()
    counting_words()
    count = 0
    for i in range(0, len(input_name) - 1):
        if (input_name_list[i] == names_numbers_list[i]):
            count += 1
    print(f"count {count}")


def display_counts(count, counts, counting):
    """Displayinig main counts"""
    main_counts = 0
    main_counts = count + counts + counting
    print(f"main_counts :{main_counts}")
    main_count_list.append(main_counts)


# names_number
for keys in names_numbers:
    for letter in keys:
        names_numbers_list.append(letter)

    searching()
    display_counts(count, counts, counting)
    count = 0
    counts = 0
    counting = 0

    names_numbers_list = []

def phone_numbers(keys, value):
    """To display number"""
    each_person_numbers = {'santosh': 9860777044, 'sakar': 9460777044, 'tsering': 9860722044, 'babita': 98612137044,
                     'ajay': 9860777022,
                     'akul': 9860777041, 'atul': 9860771041, 'Sachin': 9822777041, 'Pritam Pani ko dai': 9860777042,
                     'tsering Topchen': 9860777041,
                     'ambay': 1234, 'sabita': 4500}

    for key, values in each_person_numbers.items():
        if(keys == key):
            value = values
            return value




def display_most_matched_words():
    """Displaying main points words"""
    print(main_count_list)
    i = 0
    for keys in names_numbers:
        names_numbers[keys] = main_count_list[i]
        i += 1
    print(names_numbers)

    # sort array in descending order
    main_count_list.sort(reverse=True)
    print(main_count_list)

    k = 0
    value = ""
    print("---------------------------")
    print("REMEMBER THE MOST TOP MATCHED WORDS ARE THE ON THE TOP IN PRECEDING ORDER")
    print("++++++++++++++++++++++++++++")


    print("Most matched word for: " +input_name)
    print("")
    while (k<3):
        for keys, values in names_numbers.items():
            if main_count_list[k] == values:

                print(f"Most matched words in list: {keys}, {phone_numbers(keys, value)}")
                k+=1



display_most_matched_words()

















