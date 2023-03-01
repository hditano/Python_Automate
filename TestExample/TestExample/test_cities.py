from city_functions import city_functions


def test_city_country():
    my_test = city_functions("Buenos Aires", 'Argentina')
    assert my_test == 'Buenos Aires Argentina'

def test_city_country_population():
    my_test = city_functions('Buenos Aires', 'Argentina', '500000')
    assert  my_test == 'Buenos Aires, Argentina - population 500000'