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
        viewport = syntax['viewport'] % "project:Home"

        print("Markup: %s\nViewport syntax:\n%s\nRegex pattern:\n%s" % (
            markup, viewport, regexp.VIEWPORT[markup].pattern))

        match = re.search(regexp.VIEWPORT[markup], viewport)

        assert match != None

        filterstring = match.group('filter').strip()
        name = match.group('name').strip()

        assert filterstring == "project:Home"
        assert name == "Test"

