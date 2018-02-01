# lista dict
# dict in dict
#
# my_dict = {
#     'key1': {
#         'a_key1': {'a_key1': 'a_value1'},
#         'a_key2': {'a_key1': 'a_value1'},
#         'a_key3': {'a_key1': 'a_value1'}
#     },
#     'key2': {
#         'a_key1': {'a_key1': 'a_value1'},
#         'a_key2': {'a_key1': 'a_value1'},
#         'a_key3': {'a_key1': 'a_value1'}
#     },
#     'key3': {
#         'a_key1': {'a_key1': 'a_value1'},
#         'a_key2': {'a_key1': 'a_value1'},
#         'a_key3': {'a_key1': 'a_value1'}
#     },
# }
#
# for k, v in my_dict.iteritems():
#     for j, i in v.iteritems():
#         for m, n in i.iteritems():
#             print m, n
import time

my_list = [
    {'key': 'value1'},
    {'key': 'value2'},
    {'key': 'value3'},
]

persons = [
    {
        'name': 'Jan',
        'mail': 'jan@email.si'
    },
    {
        'name': 'Jakob',
        'mail': 'jakob@email.si'
    },
    {
        'name': 'Sanja',
        'mail': 'sanja@gmail.si'
    }
]
print persons
persons.sort(key=lambda x: x['name'], reverse=False)
print persons
filtered = list(filter(lambda x: x['key'] == 'value2', my_list))
start = time.time()
filtered = list(filter(lambda x: 'gmail' in x['mail'], persons))
stop = time.time()
print 'lambda', filtered, stop - start


filt = []
start = time.time()
for person in persons:
    if 'gmail' in person['mail']:
        filt.append(person)
stop = time.time()
print 'for', filt, stop - start

new_list = [

]
# print new_list.index(2)
# for d in my_list:
#     print d