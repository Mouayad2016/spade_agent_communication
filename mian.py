from models.senderAgent import SenderAgent
from models.resiverAgent import ReceiverAgent

import time

# ! Not reviver agent is not receiving if I use VSCode instead it works on pycharm.

if __name__ == "__main__":

    # resiver@xmpp-hosting.de pass 000000  # ? TO CREATE AN ACCOUNT VISIT https://jabber.hot-chilli.net/forms/create/
    # sender@xmpp-hosting.de pass 000000
    receiveragent = ReceiverAgent("resiver@xmpp-hosting.de", "000000")
    future = receiveragent.start()
    # ! future.wait() is original in the official documentation, but not working. the solution future.result().
    future.result()
    senderagent = SenderAgent("sender@xmpp-hosting.de", "000000")
    senderagent.start()
    # future.result()
    while receiveragent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            senderagent.stop()
            receiveragent.stop()
            break
    print("Agents finished")
