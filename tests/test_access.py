# coding:utf-8

import pytest
import threading
from perth import Perth


def test_counting():
    results = {'main': False, 'sub': False}
    pth = Perth()

    pth.set_seed('test', 0)

    def f():
        pth.test += 1
        results['sub'] = pth.test == 1

    thread = threading.Thread(target=f)

    thread.start()
    pth.test += 1
    thread.join()

    results['main'] = pth.test == 1
    assert all(results.values())


def test_del():
    pth = Perth()
    pth.set_seed('test', 100)
    pth.test += 10

    del pth.test
    assert pth.test == 100


def test_invalid():
    pth = Perth()
    pytest.raises(AttributeError, getattr, pth, 'test')
