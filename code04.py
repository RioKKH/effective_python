#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def formatted_string():
    key = 'my_var'
    value = 1.234

    f_string = f'{key:<10} = {value:.2f}'

    c_tuple = '%-10s = %.2f' % (key, value)

    str_args = '{:<10} = {:.2f}'.format(key, value)

    str_kw = '{key:<10} = {value:.2f}'.format(key=key, value=value)

    c_dict = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}

    assert c_tuple == c_dict == f_string
    assert str_args == str_kw == f_string


if __name__ == '__main__':
    formatted_string()
