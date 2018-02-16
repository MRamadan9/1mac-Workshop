
import models
import store

member1 = models.Member('Ahmed', 25)
member2 = models.Member('Mahmoud', 28)


post1 = models.Post('First Post', 'This is first post')
post2 = models.Post('Second Post', 'This is second post')
post3 = models.Post('Third Post', 'This is third post')


member_store = store.MemberStore()
member_store.add(member1)
member_store.add(member2)
member_store.get_all()


post_store = store.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
post_store.get_all()

sep =('-'*20)

print(member_store.get_by_id(1)) #>>> give member name
print(sep)

print(member_store.entity_exists(member1)) #>>> give True if found
print(sep)

member_store.delete(1)  #>>> delete member1 
print(member_store.get_by_id(1)) # >>> give None after delete
print(sep)


print(post_store.get_by_id(1)) #>>> give post name
print(sep)

print(post_store.entity_exists(post1)) #>>> give True if found
print(sep)

post_store.delete(1)        #>>> delete post1 
print(post_store.get_by_id(1)) # >>> give None after delete
