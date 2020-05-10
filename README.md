# Slack bot

In order to run this bot and install it in your Slack workspace, you need to do the following:
* clone this repo
* in activated venv (source venv/bin/activate) export necessary sensitive data such as CLIENT_ID (more about it below)
* run app.py
* run ./ngrok http 5000
* copy https link on which your ngrok server runs
* on slack api in Event Subscriptions tab alter your Request URL to **your_ngrok_link**/slack
(wait until it's verified) and in OAuth & Permissions tab change your Redirect URL to
**your_ngrok_link**/thanks. Don't forget to save changes!
* reinstall your app (just click on the message on the top of the page)
* give the bot permission to access your workspace (just click Allow)
* go to **your_ngrok_link**/install and click the Add to Slack button. You should choose
the channel for bot to post to - yep, it's just a direct message with bot channel and if everything goes to plan,
you should see Thanks for installing myBot! page.
* now head to your slack workspace and start your conversation with bot.
Enjoy!

Github repo from workshops on building bot has helped me a lot with Slack integration 
(https://github.com/slackapi/build-this-bot-workshop).