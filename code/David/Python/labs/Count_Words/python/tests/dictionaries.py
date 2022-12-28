# Create Contact ===============================================================
# Write a function that returns a dictionary representing a contact given their name and age.

def create_contact(name, age):
    return {'name': name, 'age': age}


def test_create_contact():
    assert create_contact('Bob', 67) == {'name': 'Bob', 'age': 67}
    assert create_contact('Linda', 34) == {'name': 'Linda', 'age': 34}

# Has Key ======================================================================
# Write a function that returns `True` if the given dictionary has the given key, `False` otherwise.


def has_key(d, key):
    return bool(key in d.keys())


def test_has_key():
    assert has_key({'a': 1, 'b': 2}, 'a') == True
    assert has_key({'a': 1, 'b': 2}, 'c') == False

# Is Empty =====================================================================
# Write a function that returns `True` if the given dictionary is empty, `False` otherwise.


def is_empty(d):
    return bool(len(d.keys()) == 0)


def test_is_empty():
    assert is_empty({}) == True
    assert is_empty({'a': 1, 'b': 2}) == False

# Find Key =====================================================================
# Write a function that finds and returns the **key** for the given **value**, if the value is not in the dictionary, it should return `None`.


def find_key(d, value):
    found = None
    for pair in list(d.items()):
        if value == pair[1]:
            found = pair[0]
            break

    return found            


def test_find_key():

    assert find_key({'a': 1, 'b': 2}, 1) == 'a'
    assert find_key({'a': 1, 'b': 2}, 3) == None

# Merge ========================================================================
# Write a function that mergest two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.


def merge(list1, list2):
    if not list1 or not list2:
        return None
    elif len(list1) == len(list2):
        md = {}
        for key_ind in range(len(list1)):
            md[list1[key_ind]] = list2[key_ind]

        return md


def test_merge():
    assert merge(['a', 'b'], [1, 2]) == {'a': 1, 'b': 2}

# Reverse Dict =================================================================
# Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.


def reverse_dict(d):
    rd = {}
    rdk = list(d.keys())
    rdv = list(d.values())
    rd = merge(rdv, rdk)
    return rd


def test_reverse_dict():
    assert reverse_dict({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}

# Remove Less Than 10 =========================================================
# Write a function that takes a dictionary and returns a new dictionary without values less than 10.

def remove_less_than_10(d):
    new_dict = {}
    for key in list(d.keys()):
        if d[key] >= 10:
            new_dict[key] = d[key]
    return new_dict


def test_remove_less_than_10():
    assert remove_less_than_10({'a': 5, 'b': 15, 'c': 12}) == {
        'b': 15, 'c': 12}

# Average ======================================================================
# Write a function to calculate the average of the lists in a dictionary.

def find_average(numbers):
    result = 0
    for number in numbers:
        result += number
    return result / len(numbers)

def average_values(d):
    all_avgs = {}
    for key in list(d.keys()):
        all_avgs[key] = find_average(d[key])
    return all_avgs


def test_average_values():
    assert average_values({'a': [1, 5, 6], 'b': [2, 8], 'c': [3]}) == {
        'a': 4, 'b': 5, 'c': 3}

# Merge Dictionaries ===========================================================
# Write a function that takes two dictionaries and returns a new dictionary with the values from each added together if they have the same key


def merge_dictionaries(d1, d2):
    new_dict = d1
    for key in list(d2.keys()):
        if key in list(d1.keys()):
            new_dict[key] += d2[key]
        else:
            new_dict[key] = d2[key]
    return new_dict


def test_merge_dictionaries():
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    assert merge_dictionaries(d1, d2) == {
        'a': 400, 'b': 400, 'c': 300, 'd': 400}

# Count Votes ==================================================================
# Write a function that takes a list of strings and counts of the number of occurances.


def count_votes(votes):
    total_votes = {}
    for vote in votes:
        if vote in total_votes:
            total_votes[vote] += 1
        else:
            total_votes[vote] = 1
    return total_votes


def test_count_votes():
    votes = ['john', 'johnny', 'john', 'jackie', 'jamie', 'jackie',
             'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
    assert count_votes(votes) == {'john': 4,
                                  'johnny': 3, 'jackie': 2, 'jamie': 4}

# Problem 6 ====================================================================
# Write a function `cart_total` to calculate the total of a shopping cart given a list of dictionaries representing a cart and a dictionary representing prices.


def cart_total(prices, cart):
    total_cost = 0
    for item_dict in cart:
        total_cost += prices[item_dict['item']] * item_dict['quantity']
    return total_cost



def test_cart_total():
    prices = {'apples': 1.0, 'bananas': 0.5, 'kiwis': 2.0}
    cart = [{'item': 'apples', 'quantity': 3},
            {'item': 'kiwis', 'quantity': 4}]
    assert cart_total(prices, cart) == 11.0