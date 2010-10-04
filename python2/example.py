"""
Almost pythonic, full documented and ones Plurk API implementetion for Python 3.x
Some usefull uses
For more information see:
"""

import plurklib

api_key = '6VmQlPVvFK42KYAVrQrl3bbbPnr8ouSU'

#initialize api
p = plurklib.PlurkAPI(api_key)

#Login
p.login('Karakurt', 'terror11')#'new_name', 'password12345')

#Update full name.
#In the same way you can full_name, update new_password, email, display_name, privacy, date_of_birth
#p.update(current_password = 'password12345', full_name = 'Lila Steel')

#Update privacy and date_of_birth
#In the same way you can update full_name, new_password, email, display_name, privacy, date_of_birth
#p.update(current_password = 'password12345', privacy = 'only_friends', date_of_birth = '1985-04-13')

#Update avatar
#print(p.updatePicture('/home/kurt/Pictures/_ava_plurk.jpg'))

#Register new user
#print(p.register(nick_name = 'new_name', full_name = 'Full Name', password = 'password12345',
#                 gender ='female', date_of_birth ='1985-05-13', email = 'new_name@new_name.com'))

#Returns info about a user's karma
print('Karma:', p.getKarmaStats()['current_karma'])

#Returns data that's private for the currently logged in user.
#print(p.getOwnProfile())

#Username to id
#print(p.usernameToUid('Karakurt'))

#Fetches public information such as a user's public plurks and basic information by uid
#print(p.getPublicProfile(3852645))
#or using usernameToUid
#print(p.getPublicProfile(p.usernameToUid('Karakurt')))

#If there any new plurks posted to the user's timeline. 
#print(p.getPlurks('2010-9-29T21:55:34'))

#Find out if there are unread plurks on a user's timeline.
#print(p.getUnreadCount())

#Get plurk_id by link to plurk
#print(p.linkToPlurkID('http://www.plurk.com/p/7ym3mf'))

#Get link to plurk by plurk_id
#print(p.plurkIDToLink(481401303))

#Get plurk and the owner info
#print(p.getPlurk(475522950))
#or with permalinkToPlurkID
#print(p.getPlurk(p.linkToPlurkID('http://www.plurk.com/p/7ym3mf')))

#Get filtered plurks
#print(p.filterPlurks(filter="only_responded"))

#Get unread plurk
#print(p.getUnreadPlurks())

#Post plurk
#print(p.plurkAdd("Post for edit.", limited_to = [3852645]))

#Delete plurk
#print(p.plurkDelete(478630692))

#Edit plurk
#print(p.plurkEdit(478935227, "Edited plurk"))

#Mute plurks by id
#print(p.mutePlurks([478630692]))

#Unmute plurks by id
#print(p.unmutePlurks([478630692]))

#Favorite plurks by id
#print(p.favoritePlurks([478660853, 478630692]))

#Unfavorite plurks by id
#print(p.unfavoritePlurks([478660853, 478630692]))

#Mark plurks as read by id
#print(p.markAsRead([478660853, 478630692], True))

#Get plurk response
#print(p.getResponses(478660853, 0))

#Add a response
#print(p.responseAdd(478660853, ':)', ':'))

#Delete response
#print(p.responseDelete(2275447277, 478660853))

#Get Friends By Offset
#print(p.getFriendsByOffset(3852645, 10))

#Get Fans By Offset
#print(p.getFansByOffset(3852645))

#getFollowingByOffset
#print(p.getFollowingByOffset(3852645))

#Become a friend
#print(p.becomeFriend(3852645))

#Remove as friend
#print(p.removeAsFriend(3852645))

#Become a fun
#print(p.becomeFan(3852645))

#Unfollow user
#print(p.setFollowing(3852645, False))

#See logged in users friends (nick name and full name)
#print(p.getCompletion())

#List of current active alerts
#print(p.getActive())

#List of past 30 alerts.
#print(p.getHistory())

#Accept user_id as fan.
#print(p.addAsFan(3852645))

#Accept all friendship requests as fans.
#print(p.addAllAsFan())

#Accept all friendship requests as friends.
#print(p.addAllAsFriends())

#Accept user_id as friend.
#print(p.addAsFriend(3852645))

#Deny user_id as friend.
#print(p.denyFriendship(3852645))

#Remove notification to user with id user_id.
#print(p.removeNotification(3852645))

#Returns the latest 20 plurks on a search term.
#print(p.plurkSearch('Karakurt is good'))

#Returns 10 users that match query, users are sorted by karma.
#print(p.userSearch('Karakurt'))

#Get list of emoticons
#print(p.emoticonsGet())

#List of blocked users
#print(p.getBlocks())

#Block user
#print(p.block(3476548))

#Unblock user
#print(p.unblock(3852645))

#Get list of cliques
#print(p.getCliques())

#Get users in the clique
#print(p.getClique('Coders'))

#Get users in the clique
#print(p.createClique('Developers'))

#Rename clique
#print(p.renameClique('Developers', 'Dev'))

#Add user to the clique
#print(p.addToClique('Dev', 3852645))

#Remove user to the clique
#print(p.removeFromClique('Dev', 3852645))

#Requests to this unqiue channel in order to get notifications
#for additional information read: http://www.plurk.com/API#realtime
#print(p.getUserChannel())

#print(p.uploadPicture('/home/kurt/Pictures/_ava_plurk.jpg'))

#print(p.deleteClique('aaa'))

#Logout
p.logout()
