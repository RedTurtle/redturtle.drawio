# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from redturtle.drawio.testing import REDTURTLE_DRAWIO_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that redturtle.drawio is properly installed."""

    layer = REDTURTLE_DRAWIO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if redturtle.drawio is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'redturtle.drawio'))

    def test_browserlayer(self):
        """Test that IRedturtleDrawioLayer is registered."""
        from redturtle.drawio.interfaces import (
            IRedturtleDrawioLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IRedturtleDrawioLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = REDTURTLE_DRAWIO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['redturtle.drawio'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if redturtle.drawio is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'redturtle.drawio'))

    def test_browserlayer_removed(self):
        """Test that IRedturtleDrawioLayer is removed."""
        from redturtle.drawio.interfaces import \
            IRedturtleDrawioLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IRedturtleDrawioLayer,
            utils.registered_layers())
