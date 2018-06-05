# -*- coding: utf-8 -*-
from redturtle.drawio.content.drawio_item import IDrawioItem
from redturtle.drawio.testing import REDTURTLE_DRAWIO_INTEGRATION_TESTING
from zope.interface.exceptions import Invalid

import unittest


class DrawioItemInvariantTest(unittest.TestCase):

    layer = REDTURTLE_DRAWIO_INTEGRATION_TESTING

    def test_formschemainvariants_empty_field(self):
        class Data(object):
            html_embed = None

        obj = Data()
        self.assertTrue(IDrawioItem.validateInvariants(obj) is None)

    def test_formschemainvariants_fail_string(self):
        class Data(object):
            html_embed = None
        obj = Data()
        obj.html_embed = 'foo'
        self.assertRaises(Invalid, IDrawioItem.validateInvariants, obj)

    def test_formschemainvariants_iframe_wrong_src(self):
        class Data(object):
            html_embed = None
        obj = Data()
        obj.html_embed = '<iframe src="https://www.foo.bar/"></iframe>'
        self.assertRaises(Invalid, IDrawioItem.validateInvariants, obj)

    def test_formschemainvariants_iframe_good_src(self):
        class Data(object):
            html_embed = None
        obj = Data()
        obj.html_embed = '<iframe src="https://www.draw.io/?foo"></iframe>'
        self.assertTrue(IDrawioItem.validateInvariants(obj) is None)
