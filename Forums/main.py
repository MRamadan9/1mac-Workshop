
import models
import store

member1 = models.Member('Ahmed', 25)
member2 = models.Member('Mahmoud', 28)
member3 = models.Member('Mahmoud', 28)



post1 = models.Post('First Post', 'This is first post')
post2 = models.Post('First Post', 'This is first post copy "to check get by name"')
post3 = models.Post('Second Post', 'This is second post')
post4 = models.Post('Third Post', 'This is third post')


member_store = store.MemberStore()
member_store.add(member1)
member_store.add(member2)
member_store.add(member3)



post_store = store.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
post_store.add(post4)
post_store.get_all()


def sep(a):
    print('='*30)
    print('{:^30}'.format(a))
    #print('-'*20)
    print('{:^30}'.format('----------'))


print('Member functions')
    
sep('get by id')
print(member_store.get_by_id(1)) #>>> give member name

sep('entity_exists')
print(member_store.entity_exists(member1)) #>>> give True if found

sep('get by name')
print(member_store.get_by_name('Mahmoud')) #give same member 

sep('update')
new_member = models.Member("Ali", 35)
new_member.id = 1
member_store.update(new_member) #updating member
print(member_store.get_by_id(1)) #print new member data 

sep('delete')
member_store.delete(1)  #>>> delete member1 
print(member_store.get_by_id(1)) # >>> give None after delete


#---------------Post--------------------
sep('Post functions')

sep('get by id')
print(post_store.get_by_id(2)) #>>> give post name

sep('entity_exists')
print(post_store.entity_exists(post1)) #>>> give True if found

sep('get by name')
print(post_store.get_by_name('First Post')) #give same post 

sep('update')
new_post = models.Post("First Post", 'This is First post after update')
new_post.id = 1
post_store.update(new_post) #updating post
print(post_store.get_by_id(1)) #print new post data 

sep('delete')
post_store.delete(1)        #>>> delete post1 
print(post_store.get_by_id(1)) # >>> give None after delete
