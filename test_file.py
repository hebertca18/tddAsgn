import pytest
from Greeting_Kata import *


class TestList:

    def test_01(self):
        name = 'Bob'
        ex = 'Hello, Bob.'
        assert ex == greet(name)

    def test_02(self):
        name = None
        ex = 'Hello, my friend.'
        assert ex == greet(name)

    def test_03(self):
        name = 'JERRY'
        ex = 'HELLO JERRY!'
        assert ex == greet(name)