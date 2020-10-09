# from bs4 import BeautifulSoup
# import requests
#
# handle = input('Input your account name on Twitter: ')
# ctr = int(input('Input number of tweets to scrape: '))
# res = requests.get('https://twitter.com/search?q='+ handle)
# bs = BeautifulSoup(res.content,'lxml')
#
# all_tweets = bs.find_all('div',{'class':'tweet'})
# if all_tweets:
#   for tweet in all_tweets[:ctr]:
#     context = tweet.find('div',{'class':'context'}).text.replace("\n"," ").strip()
#     content = tweet.find('div',{'class':'content'})
#     header = content.find('div',{'class':'stream-item-header'})
#     user = header.find('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
#     time = header.find('a',{'class':'tweet-timestamp js-permalink js-nav js-tooltip'}).find('span').text.replace("\n"," ").strip()
#     message = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
#     footer = content.find('div',{'class':'stream-item-footer'})
#     stat = footer.find('div',{'class':'ProfileTweet-actionCountList u-hiddenVisually'}).text.replace("\n"," ").strip()
#     if context:
#       print(context)
#     print(user,time)
#     print(message)
#     print(stat)
#     print()
# else:
#     print("List is empty/account name not found.")


import requests
res = requests.get('https://public.tableau.com/views/Membership-tableau-combinedMaps-v4/DB-V3?%3Aembed=y&%3AshowVizHome=no&%3Ahost_url=https%3A%2F%2Fpublic.tableau.com%2F&%3Aembed_code_version=3&%3Atabs=no&%3Atoolbar=yes&%3Aanimate_transition=yes&%3Adisplay_static_image=no&%3Adisplay_spinner=no&%3Adisplay_overlay=yes&%3Adisplay_count=yes&%3AloadOrderID=0').json()
#The XHR Response is Usually in Json format
#res = [{'name': 'Yoshua Bengio', 'id': '161269817', 'lat': 0.0, 'lon': 0.0}, {'name': 'Geoffrey E. Hinton', 'id': '563069026', 'lat': 0.0, 'lon': 0.0}, {'name': 'Andrew Zisserman', 'id': '2469405535', 'lat': 0.0, 'lon': 0.0}, {'name': 'Ilya Sutskever', 'id': '215131072', 'lat': 0.0, 'lon': 0.0}, {'name': 'Jian Sun', 'id': '2200192130', 'lat': 0.0, 'lon': 0.0}, {'name': 'Trevor Darrell', 'id': '2174985400', 'lat': 0.0, 'lon': 0.0}, {'name': 'Scott Shenker', 'id': '719828399', 'lat': 0.0, 'lon': 0.0}, {'name': 'Jiawei Han', 'id': '2121939561', 'lat': 0.0, 'lon': 0.0}, {'name': 'Kaiming He', 'id': '2164292938', 'lat': 0.0, 'lon': 0.0}, {'name': 'Ross Girshick', 'id': '2473549963', 'lat': 0.0, 'lon': 0.0}, {'name': 'Ion Stoica', 'id': '2161479384', 'lat': 0.0, 'lon': 0.0}, {'name': 'Hari Balakrishnan', 'id': '1998464616', 'lat': 0.0, 'lon': 0.0}, {'name': 'R Core Team', 'id': '2976715238', 'lat': 0.0, 'lon': 0.0}, {'name': 'Jitendra Malik', 'id': '2136556746', 'lat': 0.0, 'lon': 0.0}, {'name': 'Jeffrey Dean', 'id': '2429370538', 'lat': 0.0, 'lon': 0.0}]
# for author in res:
#     print(author)
