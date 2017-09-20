ABOUT:

Unconsciously, we all do things that we may not be proud of, like saying offensive things without realising it. 

Online harassment is a real thing. No one likes a person who says mean things, whether intentionally or not. Are you such a person? Most of us think that we aren't, but sometimes, we don;t realize that the words we say have a real effect on other's mental heath.

Harass-o-meter is an application that could help us understand that our words online might actually be hurtful. With just a few clicks, we will help you understand and quantify your online language. Don’t worry, the application is completely anonymous. No one will know but you. 

The Harass-o-meter utilizes fastText, a library for efficient learning of word representations and sentence classification, from Facebook research. This opensource platform is very lightweight and fast enough to analyze pages of messages in a reasonable amount of time. fastText is often on par with deep learning classifiers in terms of accuracy, and many orders of magnitude faster for training and evaluation. Therefore, we can detect online harassments with the lightweight functionality.

We have manually created dataset for the harassing sentences from the internet. Our data set consists of Okay vs Offensive/Harassing sentences, which was used to train fastText algorithm. 

INSTALLATION:

Make sure you've installed html2text library for python. html2text is available on pypi https://pypi.python.org/pypi/html2text or
$ pip install html2text

You will also need tkinter for the user interface we've created. To install, please refer to 
http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter or 
apt-get install python-tk

USAGE:

Our program provides two main functionalities in the UI format. To run the UI, do python GUI.py.

1. Web analysis: By typing the weblink in the entry and choosing web option, we could analyze a webpage for online harassment. Our script will parse normal sentences from the html and will use fastText to determine if there is any harassment phrases.

2. Manual analysis: We've provided the option to allow user to give input text file, and our program will read it line by line and will determine if it is a harassing sentence or not.

Once we analyze the text, listOkay.txt and listOffensive.txt will be created, and each of them will have a list of sentences/phrases that are considered okay and offensive/harassing respectively.

It will also display a list of offensive words in the rightmost window and the Offensive/Total ratio.

Do not run the same file twice in a row.


Future Work:
1. The data set can support up to a billion words efficiently, but currently our set is in the thousands.

2. This project is a demo, it should be expanded in order to support various platforms.

3. More categories (e.g. types of harassment) can be added to the program.

4. Integrate program into website for ease of use.


