def filter_short_names(names, max_length):
    filtered_names = filter(lambda name: len(name) < max_length, names)
    filtered_names_list = list(filtered_names)
    return filtered_names_list

product_names = ["Apple", "Banana", "Orange", "Grapes", "Pineapple"]

short_names = filter_short_names(product_names, 6)
print("Product names shorter than 6 characters:", short_names)
