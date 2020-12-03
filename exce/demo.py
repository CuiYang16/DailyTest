# !/usr/bin/python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         demo
# Description:  异常处理
# Author:       cuiyang
# Date:         2020/12/1 14:09
# -------------------------------------------------------------------------------

import logging


def chu(i):
    n = int(i)
    if i == 0:
        raise ValueError('invalid value: %i' % i)
    try:
        10 / n
    except ZeroDivisionError as e:
        logging.exception(e)


def bar():
    try:
        chu('0')
    except ValueError as e:
        print('ValueError!')
        raise


bar()
