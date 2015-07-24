# coding:utf-8

import pytest
from perth import Perth


def test_get():
    pth = Perth()
    pth.set_seed('test', 1)
    assert pth.get_seed('test') == 1


def test_get_f():
    pth = Perth()

    @pth.set_seed_f
    def test():
        return 100

    assert pth.get_seed('test') == 100


def test_remove():
    pth = Perth()
    pth.set_seed('test', 10)

    pth.remove_seed('test')
    pytest.raises(KeyError, pth.get_seed, 'test')
