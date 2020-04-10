import pytest
from Greeting_Kata import *

class TestList:

        def test(self):
                name='Bob'
                ex='Hello, Bob.'
                assert ex == greet(name)
