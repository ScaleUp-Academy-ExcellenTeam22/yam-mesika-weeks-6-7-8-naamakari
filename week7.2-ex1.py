from typing import List


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

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Parameters
        ----------
        sender : str
            The message sender's username.
        recipient : str
            The message recipient's username.
        message_body : str
            The body of the message.
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
        the recipient should have 1 messege in the
        inbox.

        >>> po_box = PostOffice(['a', 'b'])
        >>> message_id = po_box.send_message('a', 'b', 'Hello!')
        >>> len(po_box.boxes['b'])
        1
        >>> message_id
        1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'unread': True
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username: str, messages_number: int = -1) -> List:
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
        if messages_number == -1:
            messages_number = len(self.boxes[username])
        massages = [self.boxes[username][number] for number in range(messages_number) if
                    self.boxes[username][number]['unread']]
        for number in range(messages_number):
            if self.boxes[username][number]['unread']:
                self.boxes[username][number]['unread'] = False
        return massages

    def search_inbox(self, username: str, string_to_search: str) -> List:
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
        return [message for message in self.boxes[username] if string_to_search in message['body']]


def show_example():
    """Show example of using the PostOffice class."""
    users = ['Newman', 'Mr. Peanutbutter']
    post_office = PostOffice(users)
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    print(f"Successfuly sent message number {message_id}.")
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='How are you?',
    )
    print(f"Successfuly sent message number {message_id}.")
    print(post_office.boxes['Newman'])
    print(post_office.read_inbox('Mr. Peanutbutter'))
    print(post_office.read_inbox('Newman', 2))
    print(post_office.read_inbox('Newman'))
    print(post_office.search_inbox('Newman', 'are'))


if __name__ == '__main__':
    show_example()
