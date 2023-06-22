from mycroft import MycroftSkill, intent_file_handler


class Sobbing(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sobbing.intent')
    def handle_sobbing(self, message):
        self.speak_dialog('sobbing')


def create_skill():
    return Sobbing()

