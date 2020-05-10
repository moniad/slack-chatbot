# -*- coding: utf-8 -*-
"""
In this file, we'll create a python Bot Class.
"""
import os

from slackclient import SlackClient


class MessageTypes:
    def __init__(self):
        self.greetings = ["hello", "hi", "good morning", "good afternoon", "good evening"]
        self.positive_vibes = ["fine", "cool", "great", "nice", "excellent", "couldn't be better",
                               "could not be better"]
        self.negative_vibes = ["bad", "sad", "depressed", "never felt worse", "lonely", "cry"]
        self.weather = ["sun", "wind", "cloudy", "rain", "snow", "storm"]
        self.ecology = ["natural", "environment", "resources", "garbage", "trash", "waste", "rubbish", "power plant", "nuclear",
                        "habitat", "forest"]
        self.planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    def is_msg_belongs_to_category(self, message, category):
        for text in category:
            if text in message:
                return True
        return False

    def get_msg_category_text(self, message, category):
        for text in category:
            if text in message:
                return text
        return None

    def is_greeting(self, message_text):
        return self.is_msg_belongs_to_category(message_text, self.greetings)

    def user_is_positive(self, message_text):
        return self.is_msg_belongs_to_category(message_text, self.positive_vibes)

    def user_is_negative(self, message_text):
        return self.is_msg_belongs_to_category(message_text, self.negative_vibes)

    def is_about_weather(self, message_text):
        return self.is_msg_belongs_to_category(message_text, self.weather)

    def get_todays_weather(self, message_text):
        return self.get_msg_category_text(message_text, self.weather)

    def is_about_ecology(self, message_text):
        return self.is_msg_belongs_to_category(message_text, self.ecology)

    def is_about_planets(self, message_text):
        return "planet" in message_text

    def get_all_planets_names(self):
        return str(self.planets)

    def is_easy(self, message_text):
        if "easy" in message_text:
            return True
        return False

    def get_is_easy_response(self):
        return "Nothing is easy until you - first, know how to do it. Second, have done it"

    def is_difficult(self, message_text):
        if "difficult" in message_text:
            return True
        return False

    def get_is_difficult_response(self):
        return "If you figure out the solution, you're gonna tell me it was easy :fist: :raised_hands:"


class Bot(object):
    """ Instanciates a Bot object to handle Slack interactions."""

    def __init__(self):
        super(Bot, self).__init__()
        self.BOT_USERNAME = 'Bot'
        self.oauth = {"client_id": os.environ.get("CLIENT_ID"),
                      "client_secret": os.environ.get("CLIENT_SECRET"),
                      "scope": "bot"}
        self.verification = os.environ.get("VERIFICATION_TOKEN")
        self.client = SlackClient("")
        self.messageTypes = MessageTypes()

    def auth(self, code):
        """
        A method to exchange the temporary auth code for an OAuth token
        which is then saved it in memory on our Bot object for easier access.
        """
        auth_response = self.client.api_call("oauth.access",
                                             client_id=self.oauth['client_id'],
                                             client_secret=self.oauth[
                                                 'client_secret'],
                                             code=code)
        self.user_id = auth_response["bot"]["bot_user_id"]
        self.client = SlackClient(auth_response["bot"]["bot_access_token"])

    def react_to_message(self, message):
        """
        A method to ask workshop attendees to build this bot. When a user
        clicks the button for their operating system, the bot should display
        the set-up instructions for that operating system.
        """

        print("MESSAGE: " + str(message))

        try:
            if message.get('username') == self.BOT_USERNAME:
                return  # bot cannot answer his own messages
        except KeyError:
            print("It wasn't the bot who wrote it")

        channel = message["channel"]
        message_text = message.get('text').lower()
        response = ""

        if self.messageTypes.is_greeting(message_text):
            response = "Hello! :smile: How are you?"
        elif self.messageTypes.user_is_positive(message_text):
            response = "I'm glad you are happy :smiley:"
        elif self.messageTypes.user_is_negative(message_text):
            response = "Oh no, poor you :unamused:"
        elif self.messageTypes.is_about_weather(message_text):
            response = "I like this weather!"
        elif self.messageTypes.is_about_ecology(message_text):
            response = "I hate people who destroy Earth!!!"
        elif self.messageTypes.is_about_planets(message_text):
            response = "Do you know all the names of planets' in Solar System? I'll tell you!\n" + \
                       self.messageTypes.get_all_planets_names()
        elif self.messageTypes.is_easy(message_text):
            response = self.messageTypes.get_is_easy_response()
        elif self.messageTypes.is_difficult(message_text):
            response = self.messageTypes.get_is_difficult_response()

        self.client.api_call("chat.postMessage",
                             channel=channel,
                             text=response)
