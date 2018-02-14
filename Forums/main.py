
import models
import store

member1 = models.Member('Ahmed', '25')
member2 = models.Member('Mahmoud', '28')

post1 = models.Post('First Post', 'This is first post')
post2 = models.Post('Second Post', 'This is second post')
post3 = models.Post('Third Post', 'This is third post')

'''
members_list = [member1, member2] 
post_list = [post1, post2, post3]

for  member in members_list :
	for post in post_list :
		print('Member Name : ' + member.name) 
		print('Age : ' + member.age)
		print('Topic Name : '  + post.title) 
		print('Topic Content : '+ post.content) 
		print('-'*25)
'''

member_store = store.MemberStore()

member_store.add(member1)
member_store.add(member2)

print(member_store.get_all())

post_store = store.PostStore()

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

print(post_store.get_all())
