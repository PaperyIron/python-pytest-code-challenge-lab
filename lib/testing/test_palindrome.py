import pytest
from palindrome import longest_palindromic_substring

def test_palindromes():
    assert longest_palindromic_substring('banana') == 'anana'
    assert longest_palindromic_substring('xxxx yy zzzzzz') == 'zzzzzz'
    assert longest_palindromic_substring('ababbbccccccaabababababa') == 'abababababa'
    assert longest_palindromic_substring('a man a plan a canal panama racecar') == 'racecar'

def test_edge_cases():
    assert longest_palindromic_substring('a') == 'a'
    assert longest_palindromic_substring('') == ''
    assert longest_palindromic_substring('abcdefg') == 'a'
    assert longest_palindromic_substring(5) == 'must be a string'
    assert longest_palindromic_substring('abaxyzzyxfghracecarqwertyytrewqmadamimadamnoonlevelcivicrotator') == 'qwertyytrewq'


