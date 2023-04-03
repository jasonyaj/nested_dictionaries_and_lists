# 1
x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# a
x[1][0] = 15
print(x)

# b
students[0]['last_name'] = 'Bryant'
print(students)

# c
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# d
z[0]['y'] = 30
print(z)

# 2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
    for i in range(0, len(some_list)):
        name1 = ''
        name2 = ''
        for j in students[i]:
            # print(j)
            # print(students[i][j])
            # print(j + '-' + students[i][j])
            if name1 == '':
                name1 = j + ' - ' + students[i][j]
            elif name2 == '':
                name2 = j + ' - ' + students[i][j]
                print(name1 + ', ' + name2)
iterateDictionary(students)

# 3
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print('# output:')
    for j in some_dict:
        length = len(some_dict[j])
        print(length, j.upper())
        for k in some_dict[j]:
            print(k)
        print('    ')
printInfo(dojo)