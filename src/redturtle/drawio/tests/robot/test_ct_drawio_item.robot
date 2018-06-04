# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s redturtle.drawio -t test_drawio_item.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src redturtle.drawio.testing.REDTURTLE_DRAWIO_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_drawio_item.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Drawio Item
  Given a logged-in site administrator
    and an add Drawio Item form
   When I type 'My Drawio Item' into the title field
    and I submit the form
   Then a Drawio Item with the title 'My Drawio Item' has been created

Scenario: As a site administrator I can view a Drawio Item
  Given a logged-in site administrator
    and a Drawio Item 'My Drawio Item'
   When I go to the Drawio Item view
   Then I can see the Drawio Item title 'My Drawio Item'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Drawio Item form
  Go To  ${PLONE_URL}/++add++Drawio Item

a Drawio Item 'My Drawio Item'
  Create content  type=Drawio Item  id=my-drawio_item  title=My Drawio Item


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form-widgets-IBasic-title  ${title}

I submit the form
  Click Button  Save

I go to the Drawio Item view
  Go To  ${PLONE_URL}/my-drawio_item
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Drawio Item with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Drawio Item title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
