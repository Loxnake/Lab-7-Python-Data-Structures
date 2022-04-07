def main():
    #initializing data structure
    student_info = {
        'name': 'Braden',
        'student_id':'10270829',
        'pizza_toppings':[
            'pepperoni',
            'olives',
            'pineapples'
        ],
        'movies':[
            {'title':[
                'Guardiens of the Galaxy',
                '6 underground']
            },
            {'genre':[
                'comedy',
                'action']
            }
        ]
    }

    #adding new movie to the list
    student_info['movies'][0]['title'].append('Guardians of the Galaxy 2')
    student_info['movies'][1]['genre'].append('action-comedy')

    #adding new toppings to the list
    moreToppings = ('mushrooms', 'sardines', 'peppers')
    new_toppings(student_info,moreToppings)

    #printing my sentance
    print_sentances(student_info)




def new_toppings(student_info, toppings):#adding new toppings to the list
    for i in toppings:
        student_info['pizza_toppings'].append(i)
    student_info['pizza_toppings'] = sorted(student_info['pizza_toppings'])

def print_sentances(student_info):#making the sentance
    print('Hi Joe, my name is ',student_info['name'],', and my student ID is ',student_info['student_id'],'.',sep = '')#line 1

    print('My ideal pizza has ',end='')#line 2
    for i in range(len(student_info['pizza_toppings'])):
        if i == len(student_info['pizza_toppings']) - 1:
            print('and',student_info['pizza_toppings'][i], end=('.\n'))
        else:
            print(student_info['pizza_toppings'][i],end=', ')
    
    print('I like to watch ',end='')#line 3
    for i in range(len(student_info['movies'][1]['genre'])):
        if i == len(student_info['movies'][1]['genre']) - 1:
            print('and',student_info['movies'][1]['genre'][i],'movies.')
        else:
            print(student_info['movies'][1]['genre'][i],end=', ')
    
    print('Some of my favourites are ',end='')#line 4
    for i in range(len(student_info['movies'][0]['title'])):
        if i == len(student_info['movies'][0]['title']) - 1:
            print('and',student_info['movies'][0]['title'][i],end='!\n')
        else:
            print(student_info['movies'][0]['title'][i],end=', ')



main()