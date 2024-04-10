# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext, MessageFactory
from botbuilder.schema import ChannelAccount, CardAction, ActionTypes, SuggestedActions




class MyBot(ActivityHandler):
    async def _send_suggested_actions(self, turn_context: TurnContext):
        """
        Creates and sends an activity with suggested actions to the user. When the user
        clicks one of the buttons the text value from the "CardAction" will be displayed
        in the channel just as if the user entered the text. There are multiple
        "ActionTypes" that may be used for different situations.
        """

        reply = MessageFactory.text("What is your favorite color?")

        reply.suggested_actions = SuggestedActions(
            actions=[
                CardAction(
                    title="Red",
                    type=ActionTypes.im_back,
                    value="Red",
                    image="https://via.placeholder.com/20/FF0000?text=R",
                    image_alt_text="R",
                ),
                CardAction(
                    title="Yellow",
                    type=ActionTypes.im_back,
                    value="Yellow",
                    image="https://via.placeholder.com/20/FFFF00?text=Y",
                    image_alt_text="Y",
                ),
                CardAction(
                    title="Blue",
                    type=ActionTypes.im_back,
                    value="Blue",
                    image="https://via.placeholder.com/20/0000FF?text=B",
                    image_alt_text="B",
                ),
            ]
        )
        return await turn_context.send_activity(reply)



    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    async def on_message_activity(self, turn_context: TurnContext):
        #await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
        user_input =  turn_context.activity.text.lower()

        if "hello" in user_input:
            message = MessageFactory.text('HELLO!')
            await turn_context.send_activity(message)
        elif "goodbye" in user_input:
            await turn_context.send_activity("Goodbye!")
        elif "information" in user_input:
            await turn_context.send_activity("Here is some information...")
            # Add more code here to provide specific information to the user based on their request
        else:
           await self._send_suggested_actions(turn_context)
        
        
       

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")


