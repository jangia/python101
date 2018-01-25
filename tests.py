from functions import sum_num
from game import check_guess


def testing_numbers_sum():
    assert sum_num(2, 3) == 5
    return "testing_numbers_sum() passed successfully"


print(testing_numbers_sum())


def test_check_guess():
    assert check_guess("Ljubljana", "Ljubljana") == True
    return "test_check_guess() passed successfully."


print test_check_guess()
