# -*- coding: utf-8 -*-
"""
This file contains common used classes described in the EDIFACT syntax.

There are multiple versions (1-4) of the EDIFACT standard, and each differ slightly.
As one project will probably never use more than one syntax version simultaneously,
it is splitted into 4 different python files, each which could be imported using

    from pydifact.syntax.v[1..4] import ...

herby providing the same structure.
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
try:
    import builtins
except ImportError:
    import __builtin__ as builtins

import re

from .. import Segment, Characters

str = getattr(builtins, 'unicode', str)


def assert_a(s, length):
    """checks if s consists of only alphabetical characters, and has a given length."""
    assert str(s).isalpha()
    assert len(s) == length


def assert_a_max(s, length):
    """checks if s consists of only alphabetical characters, and has a given maximum length."""
    assert str(s).isalpha() or s == ""
    assert len(s) <= length


def assert_n(s, length):
    """checks if s is numeric and has a given length."""
    assert int(s)
    assert len(s) == length


def assert_n_max(s, length):
    """checks if s is numeric and has a given length."""
    assert int(s)
    assert len(s) <= length


def assert_an(s, length):
    """checks if s is alphanumeric and has a given length."""
    assert len(s) == length


def assert_an_max(s, length):
    """checks if s is alphanumeric and has a given length."""
    assert len(s) <= length


def assert_a(s, length):
    """checks if s only contains characters (no numbers) and has a given length."""
    assert len(s) == length
    # TODO only alpha


def assert_a_max(s, length):
    """checks if s only contains characters (no numbers) and has a given length."""
    assert len(s) <= length


def assert_format(s, fmt_str):
    assert re.match(fmt_str, s)


class UNASegment(Segment):
    """Service String Advice."""

    tag = "UNA"

    def __init__(self, characters=None):
        if not characters:
            characters = Characters()
        assert_an(str(characters), 6)
        super(UNASegment, self).__init__("UNA", characters)
