def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        print("Zero Division Error has occured.")
        return 0
    except Exception as e:
        print(f"The {e} exception has been thrown.")



fancy_divide()