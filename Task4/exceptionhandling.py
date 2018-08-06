old_lst = [6, 'word', [2, 5], 0, 3]
new_lst = []

for i in range(6):
    try:
        tmp = 12 / old_lst[i]
        new_lst.append(tmp)
        print("List appended with", tmp)
    except TypeError:
        print("Cannot divide {0:d} by {1:}".format(12, type(old_lst[i])))
    except ZeroDivisionError:
        print("Cannot divide by 0")
    # Handling unexpected exceptions, by showing the associated error message
    except Exception as exception_object:
        print("Unexpected error: {0:}".format(exception_object))
        
print()
print("The new list is:", new_lst)