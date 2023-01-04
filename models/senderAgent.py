from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
import csv
import json
import pandas as pd
class SenderAgent(Agent):
    class InformBehav(OneShotBehaviour):
        async def run(self):
            # read the Data
            data = pd.read_csv("./data1.csv")
            # send message to this user
            msg = Message(to="resiver@xmpp-hosting.de")
            # Set the "inform" FIPA performative
            msg.set_metadata("performative", "inform")
            # Set the language of the message content
            # send data in json format
            msg.body = data.to_json()

            await self.send(msg)
            print(f"Message sent to {msg._to}")
            # set exit_code for the behaviour
            self.exit_code = "Job Finished!"

            # stop agent from behaviour
            await self.agent.stop()

    async def setup(self):
        print("SenderAgent started")
        self.b = self.InformBehav()
        self.add_behaviour(self.b)
