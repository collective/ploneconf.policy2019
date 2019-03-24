# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ploneconf.policy2019


class PloneconfPolicy2019Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ploneconf.policy2019)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneconf.policy2019:default')


PLONECONF_POLICY2019_FIXTURE = PloneconfPolicy2019Layer()


PLONECONF_POLICY2019_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONECONF_POLICY2019_FIXTURE,),
    name='PloneconfPolicy2019Layer:IntegrationTesting',
)


PLONECONF_POLICY2019_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONECONF_POLICY2019_FIXTURE,),
    name='PloneconfPolicy2019Layer:FunctionalTesting',
)


PLONECONF_POLICY2019_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONECONF_POLICY2019_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PloneconfPolicy2019Layer:AcceptanceTesting',
)
