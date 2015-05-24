Classic Twitter Sentiment Analysis:
==================================
<h2>How to Use</h2>
-Make sure data.txt is empty<br>
-Create a python file named loginDet.py in which you store variables that contain your twitter API credentials: consumer_key, consumer_secret, access_token, access_token_secret<br>
-Now open up two windows of terminal and run this command in the first one,: <br>
```
$python main.py
```
-and in the other window, run: <br>
```
$python livePlot.py
```
-This should give you a live updating graph of the twitter sentiment on the keyword 'life'<br>
-To use your own keyword, all you have to do is change the track parameter on line 48 of main.py <br>
-Honestly, the main thing I learnt from messing around with this is that people on twitter are super negative :) have fun though!<br>

<h2>Dependencies</h2>
-Matplotlib <br>
-Tweepy <br>
Tested using anaconda distribution of python 2.7, do a pip install for both of the above. Very likely there will be issues with getting matplotlib, it is recommended that you install anaconda python or some other distribution that comes with the scipy stack.
<h4>List of words with sentiment courtesy of AFINN sentiment list</h4>
