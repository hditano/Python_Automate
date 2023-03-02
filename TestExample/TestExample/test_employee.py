def test_give_default_raise(my_test):
    my_test.give_raise()
    assert my_test.show_employee() == 'Hernan Di Tano | 10000'

def  test_give_raise(my_test):
    my_test.give_raise(5000)
    assert my_test.show_employee() == 'Hernan Di Tano | 15000'