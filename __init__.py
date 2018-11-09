# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger
from mycroft.audio import wait_while_speaking

import requests

__author__ = 'Vianne'
LOGGER = getLogger(__name__)

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

class TestSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    # def __init__(self):
    #     super(TemplateSkill, self).__init__(name="TemplateSkill")

    @intent_handler(IntentBuilder("TestIntent").require("TestKeyword"))
    def handle_blue_intent(self):
        self.speak_dialog("TestDialog")

    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return TestSkill()
