# -*- coding: utf-8 -*-
import pytest
from taskwiki import regexp
import re


class TestParsingSyntax(object):
    def test_header(self, test_syntax):
        markup, syntax = test_syntax
        header = syntax['header']
        print("Markup: %s,\nHeader syntax:\n%s\nRegex pattern:\n%s" % (
            markup, header, regexp.HEADER[markup].pattern))

        if re.match(regexp.HEADER[markup], syntax['header']):
            assert 1
        else:
            assert 0


    def test_viewport(self, test_syntax):
        markup, syntax = test_syntax
        viewport = syntax['viewport'] % "project:Home | +home #T $T"

        print("Markup: %s\nViewport syntax:\n%s\nRegex pattern:\n%s" % (
            markup, viewport, regexp.VIEWPORT[markup].pattern))

        match = re.search(regexp.VIEWPORT[markup], viewport)

        assert match != None

        assert match.group('name').strip() == "Test"
        assert match.group('filter').strip() == "project:Home"
        assert match.group('defaults').strip() == "+home"
        assert match.group('source').strip() == "T"
        assert match.group('sort').strip() == "T"

