one = 'ZHm0gzfw8F7d8fs7rdh8NP928'
two = 'ry7jVm0gbI6SpdWO7GCxqotaRHRv6epZ8qvh6ecGixJbgNiASo'
three = '2563658590-cjywafNUl1bImY1TBgvZoEnuM0PKyZbAJKpBiCh'
four = 'Pxbg6piNW7VlAJZxJlSHsWxvDiszSBzCiTmcLZb1SEcDn'

from twython import Twython

following = []
verified_followers = []

twitter = Twython(one,two,three,four)
next_cursor = -1
while next_cursor != 0:
	string = "screen_name = 'narendramodi', " + "cursor = '" + str(next_cursor) + "'"
	followers = twitter.get_followers_list(string)
	next_cursor = followers['next_cursor']
	if followers['next_cursor'] != 0:
		for x in range(20):
			following.append(followers['users'][x]['name'])
			if followers['users'][x]['verified']:
				verified_followers.append(followers['users'][x]['name'])
		print len(following) , "completed"
		print "============================"
	else:
		for x in range(len(followers2['users'])):
			following.append(followers['users'][x]['name'])
			if followers['users'][x]['verified']:
				verified_followers.append(followers['users'][x]['name'])	
		print len(following) , "completed"
		print "============================"
	
print "PROCESS COMPLETE"
print "Narendra Modi has" , len(following), "followers"
print len(verified_followers) , "of them are verified accounts"