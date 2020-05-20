# automaton-v17
Chatbot auto-testing - an examle. Used 2 diferent chatbot implementations from this arcticle ['A Chatbot in Python using nltk'](https://medium.com/swlh/a-chatbot-in-python-using-nltk-938a37a9eacc)

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/BurhanH/automaton-v17/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/BurhanH/automaton-v17.svg?branch=master)](https://travis-ci.org/BurhanH/automaton-v17)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a344de5afc2b424295c185167065f80d)](https://www.codacy.com/manual/BurhanH/automaton-v17?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BurhanH/automaton-v17&amp;utm_campaign=Badge_Grade)

## An idea and concept
I was asked about my experience to test (verify) a chatbot. Honestly, I didn't have that experience before, and I decided to cover this small 'mistake' in this example. <br>
The concept is simple we need a chatbot implementation and an approach to verify chatbot behavior. Note - this is just an experiment, the author did it by scratch for learning. <br>

I found a good sample of a chatbot (see the top sentence of this repository). <br>
Then we need somehow to prepare this code to work, which I did first in my local machine in [Jupiter Lab](https://jupyterlab.readthedocs.io/en/stable/) with [IPython kernel](https://ipython.org/). When I finished with 'raw' versions of chatbots I created a virtual environment and added necessary files and repository structure. After that, I added a few simple tests (used [unittest](https://docs.python.org/3/library/unittest.html) testing framework) for each chatbot implementation. Made first run. Then added 'boundary' tests and few negative tests to see how those implementations will behave for the same test data. Then I created necessary files to publish this repository in GitHub and made integration with Travis CI.

## Structure and approach
As you can see in the current repository I put the data file into an independent folder. In a real application, it should be a database or API for data. <br>
The source folder contains the actual code for chatbots. Definitely this code should be improved and refactored. Some ideas I will explain in the Analysis section. <br>
And third one its a folder which contains actual tests. Those autotests should be improved and refactored too. <br>
Two last files in the root of this repository, one file for Python to take care of external libraries and dependencies, and the second one config file for Travis CI to execute tests. That is all about structure. <br>

An approach is simple our chatbot is a simple app (or function) that gets a sentence (a parameter) and returns the response as a sentence (an answer, a question, etc.). As you know I used the [unittest](https://docs.python.org/3/library/unittest.html) library to create simple tests like request->response because our chatbots only have input as a sentence and output as a response. <br>
We may verify that our chatbots are working, they are answering to our requests but another big question is are these answers expected (are they correct?)?

## Analysis
After a few runs I realized, [first chatbot implementation](https://github.com/BurhanH/automaton-v17/blob/master/source/bot.py#L85) for some reasons has 2 failures. One is an Error - an exception for a negative test where I put integer number into chatbot (not a string value which is represent an integer), and the second one a Failure - by some reason a test gets a different response from chatbot then expected. <br>
The [second chatbot](https://github.com/BurhanH/automaton-v17/blob/master/source/bot.py#L50) passed all tests but it doesn't mean this implementation has no errors!

![alt text](https://github.com/BurhanH/automaton-v17/raw/master/screenshots/failed.png "Failures automation-v17") <br>


## Enhancement
Chatbots: Fix chatbot bow (all tests should pass!). Code refactoring. Use OOP approach. <br>
Tests: Make them data-driven. Use presets. Add more tests for better coverage.
