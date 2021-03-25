from instapy import InstaPy

session=InstaPy(username ="<YOUR REGISTERED EMAIL ID>", password="<YOUR PASSWORD>", 
headless_browser=True)                                                                    #With headless browser you won't need browser to interact
session.login()                                                                           #session login

session.set_relationship_bounds(enabled= True, max_followers= 30)                         #Checking users with max 30 followers
session.set_do_follow(True,percentage=40)                                                 #Following 40% of followers 
session.like_by_tags(["art","friends","cars","travel","wanderer","coder"], amount = 3)    #Liking 9+amount per tag
session.set_dont_like(["naked", "nsfw"])                                                  #Ignoring if these tags are found
session.set_do_comment(True, percentage=40)                                               #Comment on 40% of stuff I come accross
session.set_comments(["Awesome!", "Sweet!", "Nice one","Beautiful :heart_eyes:"])         #comments like this
session.follow_user_following(["<friend1>", "<friend2>", "<friend3>"], amount=10, 
                randomize=True)                                                           #following people who are being followed by your followers
session.set_quota_supervisor(enabled=True, sleep_after=['likes', 'comments_d', 
'follows', 'unfollows', 'server_calls_h'],sleepyhead=True, stochastic_flow=True, 
notify_me=True,peak_likes=(57, 585),peak_comments=(21, 182),peak_follows=(48, None),
peak_unfollows=(35, 402),peak_server_calls=(None, 4700))                                  #Set quotas so Instagram wont ban you
session.end()                                                                             #End session

#There is an entire documentation for instapy which you can follow and do your thing from here
#https://instapy.org/
