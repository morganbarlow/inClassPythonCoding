'''
remove_first_and_last(list_to_clean)

html = ['<h1>', 'Some Content', '</h1>']

remove_first_and_last (html)
=> ['some Content']

remove_first_and_last(list_to_clean)

html2 = ['<h1>', 'Some Content', 'More', '</h1>']

remove_first_and_last (html2)
=> ['some Content', 'More']
'''
# html = ['<h1>', 'Some Content', '</h1>']
# html2 = ['<h1>', 'Some Content', 'More', '</h1>']

# def first_and_last_remover (list_to_clean):
#   del list_to_clean[0]
#   del list_to_clean[-1]
#   return list_to_clean

# print (first_and_last_remover(html))
# print (first_and_last_remover(html2))



# html1 = ['<h1>', 'Some Content', '</h1>']
# html2 = ['<h1>', 'Some Content', 'More', '</h1>']

# def first_and_last_remover(list_to_clean):
#   cleaned_list = list_to_clean[1:-1]
#   return cleaned_list

# print(first_and_last_remover(html1))
# print(first_and_last_remover(html2))



# html1 = ['<h1>', 'Some Content', '</h1>']
# html2 = ['<h1>', 'Some Content', 'More', '</h1>']

# def first_and_last_remover(list_to_clean):
#   list_to_clean.pop()
#   list_to_clean.pop(0)
#   return list_to_clean

# print(first_and_last_remover(html1))
# print(first_and_last_remover(html2))