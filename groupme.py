import requests
import json
import groupy

CACHE_F = 'cache.txt'

try:
    cache_file = open(CACHE_F, 'r')
    cache_str = cache_file.read()
    cache_file.close()
    CACHE_DICT = json.loads(cache_str)

except:
    CACHE_DICT = {}

groups = groupy.Group.list()
group = groups[2]
members = group.members()
messages = group.messages()
epsi_groupid = 25481406

while messages.iolder():
    pass

likes_d = {}
messages_d = {}
top_messages_d = {}
for a in messages:
    user_id = a.user_id
    likes = a.likes()
    if user_id == '21513239':
        name = 'Mike Johnson'
    elif user_id == '37587576':
        name = 'Will Godley'
    elif user_id == '18656119':
        name = 'Ryan Byrd'
    elif user_id == '31611864':
        name = 'Phill Brown'
    elif user_id == '21352311':
        name = 'Trevor Woods'
    elif user_id == '13692877':
        name = 'Chase Fanning'
    elif user_id == '40238415':
        name = 'Ted Root'
    elif user_id == '39795776':
        name = 'Fred Eder'
    elif user_id == '22274513':
        name = 'Sam Rollenhagen'
    elif user_id == '34987912':
        name = 'Adam Branch'
    elif user_id == '14724620':
        name = 'Toe Bautista'
    elif user_id == '16592814':
        name = 'Ryan Clappison'
    elif user_id == '14514023':
        name = 'Matt Allen'
    elif user_id == '20278321':
        name = 'Will Minck'
    elif user_id == '23673062':
        name = 'Judd Linscott'
    elif user_id == '17197296':
        name = 'Joe Kalas'
    elif user_id == '21650456':
        name = 'CJ Ramsdell'
    elif user_id == '19389613':
        name = 'Lucas Fioretti'
    elif user_id == '9664230':
        name = 'Luke Soenen'
    elif user_id == '29707917':
        name = 'Colton Cornwell'
    elif user_id == '23190062':
        name = 'Jack Van Dalsem'
    elif user_id == '25732098':
        name = 'Jack Williamson'
    elif user_id == '11501960':
        name = 'Zach Walljasper'
    elif user_id == '42216496':
        name = 'Jon Theros'
    else:
        name = 'GroupMe'
    if name not in messages_d:
        messages_d[name] = 1
    else:
        messages_d[name] += 1
    if len(likes) != 0 and name != 'GroupMe':
        if name not in likes_d:
            likes_d[name] = 0
        likes_d[name] += len(likes)
    m = str(a)
    if name not in top_messages_d:
        top_messages_d[name] = []
    top_messages_d[name].append((m.split('+')[0], len(likes)))

print ('\nTotal likes per user in ' + str(group).split(',')[0] + ' \n')
sorted_likes_d = sorted(likes_d.items(), key = lambda x: x[1], reverse = True)
for b in sorted_likes_d:
    print(str(b[0]) + '\n' + 'Total Likes: ' + str(b[1]) + '\n')

print('\n\nTotal messages per user in ' + str(group).split(',')[0] + ' \n')
sorted_total_messages = sorted(messages_d.items(), key = lambda x: x[1], reverse = True)
for a in sorted_total_messages:
    print(str(a[0]) + '\n' + 'Total Messages: ' + str(a[1]) + '\n')

print('\n\nAverage likes per user in ' + str(group).split(',')[0] + ' \n')

avg_likes_pp = {}
avg_likes_per_user = 0

for (a, b), (c, d) in zip(messages_d.items(), likes_d.items()):
    avg_likes_per_user = float(d) / float(b)
    avg_likes_pp[a] = avg_likes_per_user

sorted_avg_likes = sorted(avg_likes_pp.items(), key = lambda x: x[1], reverse = True)

for a in sorted_avg_likes:
    print(str(a[0]) + '\n' + 'Avergage Likes Per Message: ' + str(a[1]) + '\n')

print('\n\nTop 3 messages per user in' + str(group).split(',')[0] + '\n')

for a in top_messages_d:
    if 'like this'.upper() in top_messages_d[a][1][0].upper():
        del (top_messages_d[a])
# Gotta talk to someone about these strings

for a in top_messages_d.items():
    sorted_top_m = sorted(a[1], key = lambda x: x[1], reverse = True)[:5]
    print(a[0] + '\'s' + ' Top Messages: ' + '\n')
    for b in sorted_top_m:
        print('Message: ' + '\'' + b[0].split(':')[1][1:] + '\'' + ' ---> Likes: ' + str(b[1]))
    print('\n')
