# theDameularity
Twitterbot workshop appropriated from lee2sman Replace Yourself with a Twitterbot workshop at ITPcamp 2015: (https://github.com/lee2sman/ITPCampSessionNotes/blob/master/ReplaceYourselfWithABot.md)

To cover:

- What is a TwitterBot
- How can they be made?
- Review Process for Simple Tweepy, Python Bot creation
- Break away/ into Groups and CREATE!

#What’s a twitterbot? Discussion

- Automated posts on the Twitter microblogging service.
- Yes - some are spam to entice clicks. Others post @replies or automatically retweet in response to tweets that include a certain word or phrase.
- 24% of tweets that are on Twitter? source: Mashable
- new art form
- internet as poetry
- experimental, weird, community

#Examples and how they can be made...

- Super Low tech IFTTT
- Finding tutorials on the internet for low coding skills Twitter bots

    - Googel Scripts and Google SpreadSheets

##Types of Twitterbot

Chatbot, datamining, markov chains, visual generation, text generation, mashup/text remixing, scheduled tweets, response bots…

Options to think about...

#Making a TwitterBot

##The Process:

- Create Twitter Handel
- Get access to Twitter App
- Install API (in this case tweepy)
- Get to writing a code to tweet for you

##What are API’s/difference with Libraries?

##Register a new twitter name/handle

- Note: You can make many accounts under same email address if you use YourEmail+NewTwitterHandle@gmail.com for example (you can do this while using private browser so you can have mulitple accounts open at once)
- Verify via email after making new account

##New Twitter apps and registering Authorization Codes

- Go to https://apps.twitter.com/

    - You need to register a phone number (arrrgh) if not already done. Must be unique!
- Create new app
- Go to Keys and Access Tokens tab
- Access Level should be: Read and write
- At bottom of page click the button to generate access tokens

###Getting Started with Tweepy https://github.com/tweepy/tweepy/blob/master/docs/getting_started.rst

- We'll be installing tweepy to access twitter in Python
- Open the command line/terminal shell and run this in Bash

##

Linux

`sudo apt-get install python-pip`

OR
Mac

`sudo easy_install pip #if not already installed`

`sudo pip install virtualenv`

`sudo pip install tweepy' 
(if on El-Capitan `sudo pip install tweepy --ignored-install`)


###Things we need to download:

- Text Editor: I use Sublime?

#PYTHON!

 NOW… The Guts of our application! 4 Files:

- Python Script *.py
- Beginning Segments *.txt
- End Segments *.txt
- TwitterKeys *.py

#Create your python bot
- Example script such as scriptname.py
- Add your access tokens and keys
- Test it in your terminal with python scriptname.py

#Sign up on digital ocean
- DigitalOcean is a virtual private server
- You create droplets aka virtual (cloud) servers
- Sign up for an Ubuntu server
- You will be emailed an ip address, etc, prompted to change emails

#Log in
##Login via ssh 
Steps are here https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04

##Connect to your server via ssh
Steps are here https://www.digitalocean.com/community/tutorials/how-to-connect-to-your-droplet-with-ssh

Upload Your Script
You can upload to your server with scp
`scp <path/to/file/on/your/computer> <username>@<hostname>:<destination path>`

for example

`scp /Users/2sman/Documents/code/github\ projects/Gamelan_Ebooks/gamelan* admin@45.55.87.237:~`

#Re-install what you need on remote
##Getting started With twitter in Python

- We'll be installing tweepy to access twitter in Python
- Install pip on digitalocean server to root
```apt-get update
sudo apt-get install python-pip
pip install tweepy```
