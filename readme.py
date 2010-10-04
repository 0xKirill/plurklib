"""
This is a example of almost all uses Plurk API via plurklib 
Most Pythonic implementation of Plurk API for Python 3.x by Kurt Karakurt.

For more information see official plurklib page:    http://code.google.com/p/plurklib/
or official API website:                            http://www.plurk.com/API
"""

import plurklib

#Initialize api. Get the API key via Official API website, http://www.plurk.com/API
p = plurklib.PlurkAPI(<your_api_key>)

#Login
p.login('username', 'password')

#Update full name.
#In the same way you can full_name, update new_password, email, display_name, privacy, date_of_birth
p.update(current_password = 'password', full_name = 'Lila Steel')

#Update privacy and date_of_birth
#In the same way you can update full_name, new_password, email, display_name, privacy, date_of_birth
p.update(current_password = 'password12345', privacy = 'only_friends', date_of_birth = '1985-04-13')

#Register new user
p.register(nick_name = 'new_name', full_name = 'Full Name', password = 'password12345',
                 gender ='female', date_of_birth ='1985-05-13', email = 'new_name@new_name.com')

#Returns info about a user's karma
p.getKarmaStats()

#Returns data that's private for the currently logged in user.
p.getOwnProfile()

#Username to id
p.usernameToUid('Karakurt')

#Fetches public information such as a user's public plurks and basic information by uid
p.getPublicProfile(3852645)
#or using usernameToUid
p.getPublicProfile(p.usernameToUid('Karakurt'))

#If there any new plurks posted to the user's timeline. 
p.getPlurks('2010-9-29T21:55:34')

#Find out if there are unread plurks on a user's timeline.
p.getUnreadCount()

#Get plurk_id by link to plurk
p.linkToPlurkID('http://www.plurk.com/p/7ym3mf')

#Get link to plurk by plurk_id
p.plurkIDToLink(481401303)

#Get plurk and the owner info
p.getPlurk(475522950)
#or with linkToPlurkID
p.getPlurk(p.linkToPlurkID('http://www.plurk.com/p/7ym3mf'))

#Get filtered plurks
p.filterPlurks(filter="only_responded")

#Get unread plurk
p.getUnreadPlurks()

#Post plurk
p.plurkAdd("Post for edit.", limited_to = [3852645])

#Delete plurk
p.plurkDelete(478630692)

#Edit plurk
p.plurkEdit(478935227, "Edited plurk")

#Mute plurks by id
p.mutePlurks([478630692])

#Unmute plurks by id
p.unmutePlurks([478630692])

#Favorite plurks by id
p.favoritePlurks([478660853, 478630692])

#Unfavorite plurks by id
p.unfavoritePlurks([478660853, 478630692])

#Mark plurks as read by id
p.markAsRead([478660853, 478630692], True)

#Get plurk response
p.getResponses(478660853, 0)

#Add a response
p.responseAdd(478660853, ':)', ':')

#Delete response
p.responseDelete(2275447277, 478660853)

#Get Friends By Offset
p.getFriendsByOffset(3852645, 10)

#Get Fans By Offset
p.getFansByOffset(3852645, 5)

#getFollowingByOffset
p.getFollowingByOffset(3852645)

#Become a friend
p.becomeFriend(3852645)

#Remove as friend
p.removeAsFriend(3852645)

#Become a fun
p.becomeFan(3852645)

#Unfollow user
p.setFollowing(3852645, False)

#See logged in users friends (nick name and full name)
p.getCompletion()

#List of current active alerts
p.getActive()

#List of past 30 alerts.
p.getHistory()

#Accept user_id as fan.
p.addAsFan(3852645)

#Accept all friendship requests as fans.
p.addAllAsFan()

#Accept all friendship requests as friends.
p.addAllAsFriends()

#Accept user_id as friend.
p.addAsFriend(3852645)

#Deny user_id as friend.
p.denyFriendship(3852645)

#Remove notification to user with id user_id.
p.removeNotification(3852645)

#Returns the latest 20 plurks on a search term.
p.plurkSearch('Karakurt is good')

#Returns 10 users that match query, users are sorted by karma.
p.userSearch('Karakurt')

#Get list of emoticons
p.emoticonsGet()

#List of blocked users
p.getBlocks()

#Block user
p.block(3476548)

#Unblock user
p.unblock(3852645)

#Get list of cliques
p.getCliques()

#Get users in the clique
p.getClique('Coders')

#Get users in the clique
p.createClique('Developers')

#Rename clique
p.renameClique('Developers', 'Dev')

#Add user to the clique
p.addToClique('Dev', 3852645)

#Remove user to the clique
p.removeFromClique('Dev', 3852645)

#Delete clique
p.deleteClique('aaa')

#Requests to this unqiue channel in order to get notifications
#for additional information read: http://www.plurk.com/API#realtime
p.getUserChannel()

#Logout
p.logout()
