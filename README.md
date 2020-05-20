# automaton-v17
Chatbot testing - an examle.

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/BurhanH/automaton-v17/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/BurhanH/automaton-v17.svg?branch=master)](https://travis-ci.org/BurhanH/automaton-v17)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a344de5afc2b424295c185167065f80d)](https://www.codacy.com/manual/BurhanH/automaton-v17?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BurhanH/automaton-v17&amp;utm_campaign=Badge_Grade)

## The idea and concept
I was asked about my experience to test (verify) a chatbot. Honestly, I didn't have that experience before, and I decided to fix this small 'mistake'. <br>
The concept is simple we need a chatbot implementation and an approach to verify chatbot behavior. Note, this is just an experiment, the author did it by scratch for learning. <br>

I found a good sample of a chatbot (article ['A Chatbot in Python using nltk'](https://medium.com/swlh/a-chatbot-in-python-using-nltk-938a37a9eacc)). <br>
Then we need somehow to prepare this code to work, which I did first in my local machine in [Jupiter Lab](https://jupyterlab.readthedocs.io/en/stable/) with [IPython kernel](https://ipython.org/). When I finished with 'raw' versions of chatbots I created a virtual environment and added necessary files and the repository structure. After that, I added a few simple tests (used [unittest](https://docs.python.org/3/library/unittest.html) testing framework) for each chatbot implementation. Made first run. Then added 'boundary' tests, and few negative tests to see how those implementations will behave for the same test data. Then I created necessary files to publish this repository in [GitHub](https://github.com/) and made integration with [Travis CI](https://travis-ci.org/).

## The structure and approach
As you can see, in the current repository I put the data file into an independent folder. In a real application, it should be [a database](https://en.wikipedia.org/wiki/Database) or [API](https://en.wikipedia.org/wiki/Application_programming_interface) for data. <br>
The Source folder contains the actual code for chatbots. Definitely this code can be improved and refactored. Some ideas I will explain in the Analysis and Enhancement sections. <br>
And the third one is a folder that contains actual tests. Those autotests should be improved and refactored too. <br>
Two last files in the root of this repository are configurations, one file for [Python](https://www.python.org/) to take care of external libraries and dependencies, and the second one configuration for [Travis CI](https://travis-ci.org/) to execute tests. That is all about structure. <br>

The approach is pretty forward, our chatbot is a simple app (or function) that gets a sentence (a parameter) and returns the response as a sentence (an answer, a question, etc.). As you know I used the [unittest](https://docs.python.org/3/library/unittest.html) library to create simple tests like request->response because our chatbots only have input as a sentence and output as a response. Kind of 'black box testing', which is not true, we know implementation and how it works, but for this experiment it is ok. <br>
We may verify that our chatbots are working, they are answering to our requests, but there is a big question - are these answers correct?

## Analysis
After a few runs I realized, [first chatbot, BOW implementation](https://github.com/BurhanH/automaton-v17/blob/master/source/bot.py#L85), for some reasons has 2 failures. One is an Error - an exception for a negative test where I put integer number into chatbot (not a string value which represents an integer), and the second one a Failure - by some reason a test gets a different response from chatbot then expected. [Check live example in Travis CI here](https://travis-ci.org/github/BurhanH/automaton-v17/jobs/689282503) <br>
The [second chatbot, tfidf implementation](https://github.com/BurhanH/automaton-v17/blob/master/source/bot.py#L50), passes all tests but it doesn't mean this implementation has no errors!

![alt text](https://github.com/BurhanH/automaton-v17/raw/master/screenshots/failed.png "Failures automation-v17") <br>

## Enhancement (or TODOs)
Chatbots: Fix chatbot bow (all tests should pass!). [Code refactoring](https://en.wikipedia.org/wiki/Code_refactoring). Use the [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) approach. <br>
Tests: Make them [data-driven](https://en.wikipedia.org/wiki/Data-driven_testing). Use presets. Add more tests for better [coverage](https://en.wikipedia.org/wiki/Fault_coverage).

## Conclusion
In the first look, we may say - testing a chatbot is simple. <br>
But:
 - What if a chatbot a part of [UI](https://en.wikipedia.org/wiki/User_interface)?<br>
 - How can we test end-to-end scenarios?<br>
 - How can we verify chatbot responses properly for a decision tree in a complex scenario?<br>

Probably I missing some questions, but these three are major for me. [IMHO](https://www.merriam-webster.com/dictionary/IMHO) <br>

P/S: If you see an error or would like to ask any question feel free to reach out me ;)
