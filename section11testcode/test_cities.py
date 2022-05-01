# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:test_cities.py
@CreateTime:2022/4/18 20:39
"""

import unittest
import city_functions


class CityTestCase(unittest.TestCase):
    """测试city_functions.py"""

    def test_city_country(self):
        """验证能够正确处理Bj, China 这样的case"""
        format_city = city_functions.get_city_country('bj', 'china')
        self.assertEqual(format_city, 'Bj, China')

    def test_city_country_population(self):
        """验证能够正确处理Bj,China,100000000这样的case"""
        format_city = city_functions.get_city_country('bj',
                                                      'china',
                                                      '100000000')
        self.assertEqual(format_city, 'Bj, China-Population=100000000')


if __name__ == '__main__':
    unittest.main()



