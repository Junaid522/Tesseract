import os.path
import tweepy
import json
import time

# slack shit
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# twitter shit
api_key = "uoIKSGtcbRYH3WRSMyrYAsJ5s"
secret = "JRIPMd85yRCDIYlXnkg36QKUapE9gfawsWBve8GGg9iDvvy7go"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAEtrOQEAAAAA6HqDh7tGR73EYdzgYUaShq%2BpE3M%3DyCbKk2YAxAnYe8cVG8QVkMcLC8YYugZB5sl6F6Ky918HQfYnlJ"

access_token = "540815735-56eEsYJzhxiDRR7V33jWwZDdS50UnSVrOZ48llKz"
access_token_secret = "EKbZzP1Jl6OAc2EwmSeuFal6Bv7OoR39Us2mkiUBU6qGJ"

# user accounts to check
# user_accounts = ['CryptoWizardd']
user_accounts = ['linkpadvc', 'cryptospider1', 'CryptoWizardd', 'IAMLLUCIANA', 'CryptoGodJohn', 'CryptoMessiah',
                 'sheldonevans', 'JohnnyZcash', 'AdamHODL',
                 'fomosaurus', 'TheGemHunters', 'crypto_thai', 'ScruFFuR', 'trader1sz', 'CL207', 'LSDinmycoffee',
                 'CryptoWarlordd', 'CryptoExpert101', 'razoreth', 'Darrenlautf', 'Coin_Shark', 'CryptoNekoZ',
                 'n2ckchong', 'WhalePanda', 'SPECTREGRP']

# slack shit
slack_bot_token = "xoxb-12186908928-1873604681587-JiAbQ4l8nVoh5QhcEZP0o9oa"
signing_secret = "3e79d3600a54acadf13a9b956c149ca6"

bagger_slack_bot_token = "xoxb-1908307959301-1917656621140-dlzw9py48kZJ2g9CVNiHzPlZ"
bagger_signing_secret = "ed1d1b0951b62c40b521444eefb267a4"


class FollowerChecker:
    def __init__(self):
        auth = tweepy.OAuthHandler(api_key, secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        # user_ids we've looked up
        self.user_lookup = {}
        self.users_to_lookup = set()
        # map of user -> list of new followers
        self.user_new_followers = {}
        # setup slack
        self.slack_client = WebClient(token=slack_bot_token)
        self.bagger_slack_client = WebClient(token=bagger_slack_bot_token)

    def _sleep(self):
        sleep_time = 71
        print("sleeping for " + str(sleep_time) + " seconds...")
        time.sleep(sleep_time)

    def _fetch_friend_names(self, king):

        all_friend_names = []
        for page in tweepy.Cursor(self.api.friends, screen_name=king, count=200, include_user_entities=False,
                                  skip_status=True).pages():
            # page is a list of statuses
            all_friend_names.extend([user.screen_name for user in page])
        self._sleep()
        return all_friend_names

    def _check_user(self, user):
        user_file = user + '.json'
        if os.path.isfile(user_file):
            with open(user_file) as json_file:
                # current follower list
                old_follower_list = json.load(json_file)
                # now check against new fetch
                # this is the new 2.0 api
                # current_friend_ids = self.api.friends_ids(user)
                # this is the 1.1 api
        fetched_friend_names = self._fetch_friend_names(user)
        self._sleep()
        new_found_friend_names = []
        for new_friend_name in fetched_friend_names:
            if new_friend_name not in old_follower_list:
                new_found_friend_names.append(new_friend_name)
            if len(new_found_friend_names) > 0:
                self._send_new_followers(user, new_found_friend_names)
                # now write out the new file
                with open(user_file, 'w') as outfile:
                    json.dump(fetched_friend_names, outfile)
            else:
                # get follower list and save to file (initial load)
                # friend_ids = self.api.friends_ids(user)
                fetched_friend_names = self._fetch_friend_names(user)
            self._sleep()
            print('writing initial follower file for ' + user)
            # use this if using the 1.1 api
            # friend_ids = [user.id for user in friend_ids]
            with open(user_file, 'w') as outfile:
                json.dump(fetched_friend_names, outfile)

    def _send_slack(self, message):
        print("sending message to slack: " + message)
        try:
            response = self.slack_client.chat_postMessage(channel='#twitter-updates', text=message)
            self.bagger_slack_client.chat_postMessage(channel='#twitterbot', text=message)
        # print("got back response: " + str(response))
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["ok"] is False
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            print(f"Got an error: {e.response['error']}")

    def _lookup_new_followers(self):

        if len(self.users_to_lookup) > 0:
            # first split into chunks (max page size = 100)
            userlist = list(self.users_to_lookup)
            pages = [userlist[i:i
                                + 80] for i in range(0, len(userlist), 80)]
            for page in pages:
                print("looking up users: " + str(page))
            new_follower_users = self.api.lookup_users(user_ids=page)
            # print("got back new_follower_users: " + str(new_follower_users))
            self._sleep()
            # stick everybody in a map by user id
            self.new_follower_map = {follower.id: follower for follower in new_follower_users}
        else:
            print("no new followers found")

    def _send_new_followers(self, king, new_follower_names):
        new_followers_list = []
        for username in new_follower_names:
            new_followers_list.append("https://twitter.com/" + username)
        self._send_slack(king + " has new friend(s): " + ", ".join(new_followers_list))

    def check_followers(self):
        for user in user_accounts:
            self._check_user(user)

    # now lookup users
    # self._lookup_new_followers()
    # now spit out the results
    # self._send_new_followers()

    def check_slack(self):
        self._send_slack("test message")


checker = FollowerChecker()
checker.check_followers()
# checker.check_slack()
