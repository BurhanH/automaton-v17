import unittest
from ddt import ddt, data, unpack
from source import bot


@ddt
class TestBotBow(unittest.TestCase):
    """Simple test suite to test bot bow responses. Should be data driven."""

    @data(
        ('Hi!', 'Hey!'),
        ('Hello!', 'Howdy.'),
    )
    @unpack
    def test_greeting(self, sentence: str, response: str) -> None:
        self.assertEqual(bot.chat_bow(sentence), response)

    @data(
        ('How are you?', 'Lovely, thanks.'),
        ('Could You Help Me?', 'I\'m glad to help. What can I do for you?'),
    )
    @unpack
    def test_question(self, question: str, response: str) -> None:
        self.assertEqual(bot.chat_bow(question), response)

    @data(('Bye!', 'Bye.'))
    @unpack
    def test_bye(self, sentence: str, response: str) -> None:
        self.assertEqual(bot.chat_bow(sentence), response)

    @data(
        ('', 'Just think of me as the ace up your sleeve.'),
        (4, 'Just think of me as the ace up your sleeve.'),
        ('-4', 'Just think of me as the ace up your sleeve.'),
        ('#$%^', 'Just think of me as the ace up your sleeve.'),
        ('Привет', 'Just think of me as the ace up your sleeve.'),
        ('Hola', 'Just think of me as the ace up your sleeve.'),
        ('你好', 'Just think of me as the ace up your sleeve.'),
    )
    @unpack
    def test_negative(self, sentence, response) -> None:
        self.assertEqual(bot.chat_bow(sentence), response)


@ddt
class TestBotTfidf(unittest.TestCase):
    """Simple test suite to test bot tfidf responses. Should be data driven."""

    @data(
        ('Hi!', 'Hey!'),
        ('Hello!', 'Howdy.'),
    )
    @unpack
    def test_greeting(self, sentence: str, response: str) -> None:
        self.assertEqual(bot.chat_tfidf(sentence), response)

    @data(
        ('How are you?', 'Lovely, thanks.'),
        ('Could You Help Me?', 'I\'m glad to help. What can I do for you?'),
    )
    @unpack
    def test_question(self, question: str, response: str) -> None:
        self.assertEqual(bot.chat_tfidf(question), response)

    @data(('Bye!', 'Bye.'))
    @unpack
    def test_bye(self, sentence: str, response: str) -> None:
        self.assertEqual(bot.chat_tfidf(sentence), response)

    @data(
        ('', 'Just think of me as the ace up your sleeve.'),
        (4, 'Just think of me as the ace up your sleeve.'),
        ('-4', 'Just think of me as the ace up your sleeve.'),
        ('#$%^', 'Just think of me as the ace up your sleeve.'),
        ('Привет', 'Just think of me as the ace up your sleeve.'),
        ('Hola', 'Just think of me as the ace up your sleeve.'),
        ('你好', 'Just think of me as the ace up your sleeve.'),
    )
    @unpack
    def test_negative(self, sentence, response) -> None:
        self.assertEqual(bot.chat_tfidf(sentence), response)


if __name__ == "__main__":
    unittest.main()
