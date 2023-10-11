#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
p_s_d = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
new_dict = update_dictionary(a_dictionary, 'language', "Python")
p_s_d(new_dict)
print("--")
p_s_d(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
p_s_d(new_dict)
print("--")
p_s_d(a_dictionary)
