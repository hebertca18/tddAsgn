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

    def test_04(self):
        name = ["Jill", "Jane"]
        ex = 'Hello, Jill and Jane.'
        assert ex == greet(name)

    def test_05(self):
        name = ["Amy", "Brian", "Charlotte"]
        ex = "Hello, Amy, Brian, and Charlotte."
        assert ex == greet(name)

    def test_06(self):
        name = ["Amy", "BRIAN", "Charlotte"]
        ex = "Hello, Amy and Charlotte. AND HELLO BRIAN!"
        assert ex == greet(name)

    def test_07(self):
        name = ["Bob", "Charlie, Dianne"]
        ex = "Hello, Bob, Charlie, and Dianne."
        assert ex == greet(name)

    def test_08(self):
        name = ["Bob", "\"Charlie, Dianne\""]
        ex = "Hello, Bob and Charlie, Dianne."
        assert ex == greet(name)

