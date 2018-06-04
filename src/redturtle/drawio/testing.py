# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import redturtle.drawio


class RedturtleDrawioLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=redturtle.drawio)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'redturtle.drawio:default')


REDTURTLE_DRAWIO_FIXTURE = RedturtleDrawioLayer()


REDTURTLE_DRAWIO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(REDTURTLE_DRAWIO_FIXTURE,),
    name='RedturtleDrawioLayer:IntegrationTesting',
)


REDTURTLE_DRAWIO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(REDTURTLE_DRAWIO_FIXTURE,),
    name='RedturtleDrawioLayer:FunctionalTesting',
)


REDTURTLE_DRAWIO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        REDTURTLE_DRAWIO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RedturtleDrawioLayer:AcceptanceTesting',
)
