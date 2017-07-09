# -*- coding: utf-8 -*-
import pytest

syntax = {
    'default': {
        'header': "== Test ==",
        'viewport': "== Test | %s ==",
    },
    'markdown': {
        "header": "## Test",
        "viewport": "## Test | %s",
    },
    'restructuredtext': {
        "header": "Test\n================",
        "viewport": "Test | %s\n================",
    },
}


@pytest.fixture(params=syntax)
def test_syntax(request):
    key = request.param
    return (key, syntax[key])

