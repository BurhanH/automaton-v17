import unittest
from source import bot


class TestBotBow(unittest.TestCase):
    """
    Simple test suite to test bot bow responses. Should be data driven.
    """
    def test_greeting(self) -> None:
        data = {
            'sentence': 'Hi!',
            'response': 'Hey!'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_greeting_2(self) -> None:
        data = {
            'sentence': 'Hello!',
            'response': 'Howdy.'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_question(self) -> None:
        data = {
            'sentence': 'How are you?',
            'response': 'Lovely, thanks.'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_question_2(self) -> None:
        data = {
            'sentence': 'Could You Help Me?',
            'response': 'I\'m glad to help. What can I do for you?'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_bye(self) -> None:
        data = {
            'sentence': 'Bye!',
            'response': 'Bye.'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_empty_request(self) -> None:
        data = {
            'sentence': '',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_negative(self) -> None:
        data = {
            'sentence': 4,
            'response': 'unknown'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_negative_2(self) -> None:
        data = {
            'sentence': '-4',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_negative_3(self) -> None:
        data = {
            'sentence': '#$%^',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_negative_4(self) -> None:
        data = {
            'sentence': 'Привет',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_negative_5(self) -> None:
        data = {
            'sentence': 'Hola',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])

    def test_negative_6(self) -> None:
        data = {
            'sentence': '你好',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_bow(data["sentence"]), data["response"])


class TestBotTfidf(unittest.TestCase):
    """
    Simple test suite to test bot tfidf responses. Should be data driven.
    """
    def test_greeting(self) -> None:
        data = {
            'sentence': 'Hi!',
            'response': 'Hey!'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_greeting_2(self) -> None:
        data = {
            'sentence': 'Hello!',
            'response': 'Howdy.'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_question(self) -> None:
        data = {
            'sentence': 'How are you?',
            'response': 'Lovely, thanks.'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_question_2(self) -> None:
        data = {
            'sentence': 'Could You Help Me?',
            'response': 'I\'m glad to help. What can I do for you?'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_bye(self) -> None:
        data = {
            'sentence': 'Bye!',
            'response': 'Bye.'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_empty_request(self) -> None:
        data = {
            'sentence': '',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_negative(self) -> None:
        data = {
            'sentence': 4,
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_negative_2(self) -> None:
        data = {
            'sentence': '-4',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_negative_3(self) -> None:
        data = {
            'sentence': '#$%^',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_negative_4(self) -> None:
        data = {
            'sentence': 'Привет',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_negative_5(self) -> None:
        data = {
            'sentence': 'Hola',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])

    def test_negative_6(self) -> None:
        data = {
            'sentence': '你好',
            'response': 'Just think of me as the ace up your sleeve.'
        }
        self.assertEqual(bot.chat_tfidf(data["sentence"]), data["response"])


if __name__ == "__main__":
    unittest.main()
