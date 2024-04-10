# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext, MessageFactory
from botbuilder.schema import ChannelAccount, CardAction, ActionTypes, SuggestedActions

"""
DIRECTIONS:

The goal of this lab is to introduce you to the MS Bot Framework with some basic 
features. Everything, including examples, are provided to help you get started. 
Feel free to go beyond the starter code if you are more familar with the framework. 

Before starting, ensure you have the following pre-reqs:

    - Python 3.8 or Higher 
    - MS Bot Emulator downloaded 
    - Completed inital setup for the lab 

To run the bot:

    - cd into mbf_lab directory
    - use the command "python app.py" 
    - copy the link provided in the terminal 

ENSURE the requirements in requirements.txt are downloaded before running!!!

    - run the command "pip install -r requirements.txt"


Any questions at all, feel free to ask us! Best of luck :))))

Link to documentation:

https://learn.microsoft.com/en-us/dotnet/api/microsoft.bot.builder?view=botbuilder-dotnet-stable
"""


class MyBot(ActivityHandler):
    async def _send_suggested_actions(self, turn_context: TurnContext):
        """
        Creates and sends an activity with suggested actions to the user. When the user
        clicks one of the buttons the text value from the "CardAction" will be displayed
        in the channel just as if the user entered the text. There are multiple
        "ActionTypes" that may be used for different situations.

        Create at least two card action as a reponse to a user's input. Feel free to add 
        more options! Here's more on the card action class: 

        https://learn.microsoft.com/en-us/dotnet/api/microsoft.bot.schema.cardaction?view=botbuilder-dotnet-stable
        """

        reply = MessageFactory.text("What is your favorite color?")

        reply.suggested_actions = SuggestedActions(
            actions=[
                CardAction(
                    title=" ",
                    type=ActionTypes.im_back,
                    value=" ",
                    image=" ",
                    image_alt_text=" ",
                ), 
                 CardAction(
                    title=" ",
                    type=ActionTypes.im_back,
                    value=" ",
                    image=" ",
                    image_alt_text=" ",
                )

            ]
        )
        return await turn_context.send_activity(reply)



    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    async def on_message_activity(self, turn_context: TurnContext):
       """
       Create at least 5 bot responses in addition to the two that are provided. The first exaples is a
       normal text message while the other makes use of the suggested actions features. 

       See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
       """
       # User input is saved and compared to strings to decide how to respond 
        user_input =  turn_context.activity.text.lower()

        if "hello" in user_input:
            await turn_context.send_activity("Hey there!")
        else:
            #for any other response given, the bot will repond with the card actions
           await self._send_suggested_actions(turn_context)
        
        

    """
    Fill in the empty string with a special welcome message when a user joins a chat!
    """

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("    ")


