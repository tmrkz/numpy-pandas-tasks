import numpy as np


def double_this(arr):
    return arr * 2


def select_even(arr):
    return arr[arr % 2 == 0]


def wipe_even(arr, target_value=0, in_place=False):
    if in_place:
        arr[arr % 2 == 0] = target_value
        return arr
    edited_arr = arr
    edited_arr[edited_arr % 2 == 0] = target_value
    return edited_arr


def weighted_sum(weights, grades, normalize=False):
    if normalize and (x := np.sum(weights)) != 1:
        weights = np.dot(weights, (1 / x))
    return np.sum(weights * grades)


def mean_by_gender(grades, genders):
    return {
        "male": np.mean(grades, where=genders == "male"),
        "female": np.mean(grades, where=genders == "female")
    }


def calculate_tax(income):
    print(np.sum(income[np.cumsum(income) > 1000] * 0.2) + np.sum(income[np.cumsum(income) <= 1000] * 0.13))


if __name__ == "__main__":
    while True:
        tn = int(input("Введите номер задания: "))
        rand_arr = np.random.randint(1, 9, (1, 10))
        #match tn:
            #case 1:
        if tn == 1:
            print(double_this(rand_arr))
        #case 2:
        elif tn == 2:
            print(select_even(rand_arr))
        #case 3:
        elif tn == 3:
            print(wipe_even(rand_arr, 4))
        #case 4:
        elif tn == 4:
            print(weighted_sum(rand_arr / 10, rand_arr))
        #case 5:
        elif tn == 5:
            print(double_this(rand_arr, ))
        #case 6:
        elif tn == 6:
            print(double_this(rand_arr))
        else:
        #case _:
            exit(0)
