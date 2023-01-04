from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.template import Template
import pandas as pd
import json
import matplotlib.pyplot as plt
class ReceiverAgent(Agent):
    class RecvBehav(OneShotBehaviour):
        async def run(self):
            print("RecvBehav running")
            # wait for a message for 10 seconds
            msg = await self.receive(timeout=10)
            if msg:
                print("Message received with content")
                # json decode the data.
                data = json.loads(msg.body)
                # This function convert data from json to Dataframe.
                df = onMessageRecived(data)
                # Getting the top and worst by pandas.
                top_10 = df.nsmallest(n=10, columns=['Rank'])
                print("Top 10")
                print(top_10)
                data_2022 = df.loc[df["Year"] == 2022]
                worst_10_2022 = data_2022.nlargest(n=10, columns=['Rank'])
                top_10_2022 = data_2022.nsmallest(n=10, columns=['Rank'])
                print("The top 10 2022")
                print(top_10_2022)
                print("The worst 10 2022")
                print(worst_10_2022)

            else:
                print("Did not received any message after 10 seconds")
            # Stop agent from behaviour.
            await self.agent.stop()

    async def setup(self):
        print("ReceiverAgent started")
        b = self.RecvBehav()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)



def onMessageRecived(data):
    year = []
    point = []
    place = []
    name = []
    rank = []
    # We are going to get data in map format, we loop throw the map and extract the values.
    for key, value in data['Year'].items():
        year.append(value)
    for key, value in data['Point'].items():
        point.append(value)
    for key, value in data['Country'].items():
        place.append(value)
    for key, value in data['Name'].items():
        name.append(value)
    for key, value in data['Rank'].items():
        rank.append(value)
    # Assign new columns' data manually.
    clean_data = {'Year': year, 'Point': point, 'place': place, 'name': name, 'Rank': rank}
    df = pd.DataFrame.from_dict(clean_data)
    # Delete duplicates values in three columns.
    df = df.drop_duplicates(['Year', 'name', 'Rank'], keep='first')
    return df
