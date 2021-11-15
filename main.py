def get_banknotes(dict_bank, sum):
    list_of_banknotes = []

    def function(banknote):
        nonlocal sum
        nonlocal list_of_banknotes
        nonlocal dict_bank
        banknotes = sum // banknote
        amount = dict_bank.get(f'{banknote}$')
        dict_bank.update({f'{banknote}$': amount - banknotes})
        list_of_banknotes.append(f'{banknote}$ x {banknotes}')
        sum -= banknotes * banknote
        return None

    for i in (3, 2, 1):
        while len(str(sum)) >= i:
            if i == 3:
                function(100)
            elif i == 2:
                while len(str(sum)) == i:
                    for j in (50, 20, 10):
                        if sum >= j:
                            if len(str(sum)) == 1:
                                break
                            function(j)
                        else:
                            continue

            elif i == 1:
                while len(str(sum)) == i:
                    for j in (5, 2, 1):
                        if sum == 0:
                            return list_of_banknotes
                        elif sum >= j:
                            function(j)
                        else:
                            continue


dict_bank = {f'{i}$': 100 for i in (
    1, 2, 5, 10, 20, 50, 100
)}

sum = int(input('введите сумму, которую хотите вывести: '))
my_list = get_banknotes(dict_bank, sum)
print(my_list)
print(dict_bank)
