# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from ploneconf.policy2019.testing import PLONECONF_POLICY2019_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ploneconf.policy2019 is properly installed."""

    layer = PLONECONF_POLICY2019_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneconf.policy2019 is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ploneconf.policy2019'))

    def test_browserlayer(self):
        """Test that IPloneconfPolicy2019Layer is registered."""
        from ploneconf.policy2019.interfaces import (
            IPloneconfPolicy2019Layer)
        from plone.browserlayer import utils
        self.assertIn(
            IPloneconfPolicy2019Layer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONECONF_POLICY2019_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['ploneconf.policy2019'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if ploneconf.policy2019 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ploneconf.policy2019'))

    def test_browserlayer_removed(self):
        """Test that IPloneconfPolicy2019Layer is removed."""
        from ploneconf.policy2019.interfaces import \
            IPloneconfPolicy2019Layer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPloneconfPolicy2019Layer,
            utils.registered_layers())
