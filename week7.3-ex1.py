from typing import List


class Message:
    """A Message class. Represents communication between people.

    Parameters
    ----------
    sender : str
        The sender of the message.
    recipient : str
        The recipient of the message.
    title : str
        The title of the message.
    body : str
        The body of the message.

    Attributes
    ----------
     sender : str
        The sender of the message.
    recipient : str
        The recipient of the message.
    title : str
        The title of the message.
    body : str
        The body of the message.
    message_id : int
        Incremental id of the last message sent.
    is_read : bool
        If the message has been read already.
    """
    def __init__(self, sender: str, recipient: str, title: str, body: str):
        self.sender = sender
        self.recipient = recipient
        self.title = title
        self.body = body
        self.is_read = False
        self.message_id = 1

    def add_message_id(self, message_id: int):
        """
        Change the message id according the sending messages.
        :param message_id: The number to change to.
        """
        self.message_id = message_id

    def __str__(self) -> str:
        """Nice printing of the message."""
        return f"message number: {self.message_id}\nfrom: {self.sender}\nto: {self.recipient}\nsubject: {self.title}\n{self.body}"

    def len(self) -> int:
        """Return the len of the messages."""
        return len(self.body)


def example():
    message = Message("Cohen", "Levi", "Good morning", "Have a nice day!")
    print(message.__str__())


class PostOffice:
    """A Post Office class. Allows users to message each other.

    Parameters
    ----------
    usernames : list
        Users for which we should create PO Boxes.

    Attributes
    ----------
    message_id : int
        Incremental id of the last message sent.
    boxes : dict
        Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, message: Message, urgent=False):
        """Send a message to a recipient.

        Parameters
        ----------
        message : Message
            The message sends.
        urgent : bool, optional
            The urgency of the message.
            Urgent messages appear first.

        Returns
        -------
        int
            The message ID, auto incremented number.

        Raises
        ------
        KeyError
            If the recipient does not exist.

        Examples
        --------
        After creating a PO box and sending a letter,
        the recipient should have 1 message in the
        inbox.

        >>> po_box = PostOffice(['a', 'b'])
        >>> message_id = po_box.send_message('a', 'b', 'Hello!')
        >>> len(po_box.boxes['b'])
        1
        >>> message_id
        1
        """
        user_box = self.boxes[message.recipient]
        self.message_id += 1
        if urgent:
            user_box.insert(0, message)
        else:
            user_box.append(message)
        return self.message_id

    def read_inbox(self, username: str, messages_number: int = -1) -> List[Message]:
        """Read the unread messages in the inbox.

        Parameters
        ----------
        username : str
            The recipient's username.
        messages_number : int, optional
            The number of the messages to read.
            If no number are received, returns all unread messages in the inbox.

        Returns
        -------
        List
            The list of the unread messages of the recipient's inbox.

        Raises
        ------
        KeyError
            If the username does not exist.
        """
        if messages_number == -1 or messages_number > len(self.boxes[username]):
            messages_number = len(self.boxes[username])
        massages = [self.boxes[username][number] for number in range(messages_number) if
                    self.boxes[username][number].is_read is False]
        for number in range(messages_number):
            if not self.boxes[username][number].is_read:
                self.boxes[username][number].is_read = True
        return massages

    def search_inbox(self, username: str, string_to_search: str) -> List[Message]:
        """Return the messages that contain the received string in the message box of the received username.

          Parameters
          ----------
          username : str
              The username in his inbox we want to search for the received string.
          string_to_search : str
              The string you want to look for in messages.

          Returns
          -------
          List
              The list of messages that contain the received string.

          Raises
          ------
          KeyError
              If the username does not exist.
          """
        return [message for message in self.boxes[username] if string_to_search in message.body]


def show_example():
    """Show example of using the PostOffice class."""
    users = ['Newman', 'Mr. Peanutbutter', 'Cohen', 'Levi', 'Hertzel']
    post_office = PostOffice(users)
    message1 = Message('Levi', 'Cohen', 'Hii', 'Hello')
    message_id = post_office.send_message(message=message1)
    message1.add_message_id(message_id)
    print(f"Successfuly sent message number {message_id}.")
    message2 = Message('Levi', 'Hertzel', 'Hanny', 'Benny')
    message_id = post_office.send_message(message=message2)
    message1.add_message_id(message_id)
    print(f"Successfuly sent message number {message_id}.")
    print(post_office.boxes['Hertzel'][0].__str__())
    print(post_office.read_inbox('Mr. Peanutbutter'))
    print(post_office.read_inbox('Cohen', 2)[0].__str__())
    print(post_office.read_inbox('Newman'))
    print(post_office.search_inbox('Cohen', 'H')[0].__str__())


if __name__ == '__main__':
    show_example()
    example()
