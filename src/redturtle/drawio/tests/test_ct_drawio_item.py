# -*- coding: utf-8 -*-
from redturtle.drawio.content.drawio_item import IDrawioItem  # NOQA E501
from redturtle.drawio.testing import REDTURTLE_DRAWIO_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class DrawioItemIntegrationTest(unittest.TestCase):

    layer = REDTURTLE_DRAWIO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_drawio_item_schema(self):
        fti = queryUtility(IDexterityFTI, name='DrawioItem')
        schema = fti.lookupSchema()
        self.assertEqual(IDrawioItem, schema)

    def test_ct_drawio_item_fti(self):
        fti = queryUtility(IDexterityFTI, name='DrawioItem')
        self.assertTrue(fti)

    def test_ct_drawio_item_factory(self):
        fti = queryUtility(IDexterityFTI, name='DrawioItem')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IDrawioItem.providedBy(obj),
            u'IDrawioItem not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_drawio_item_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='DrawioItem',
            id='drawio_item',
        )
        self.assertTrue(
            IDrawioItem.providedBy(obj),
            u'IDrawioItem not provided by {0}!'.format(
                obj.id,
            ),
        )
