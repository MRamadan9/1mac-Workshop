
class MemberStore:
    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        for member in all_members:
          if member.id == id:
            return member

    def entity_exists(self, member):
        if member in self.members :
          return True
      
    def delete(self, id):
        member = self.get_by_id(id)
        self.members.remove(member)


class PostStore:
    posts = []
    last_id = 1

    def get_all(self):
        return PostStore.posts

    def add(self, post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_by_id(self, id):
        all_posts = self.get_all()
        for post in all_posts:
          if post.id == id:
            return post

    def entity_exists(self, post):
        if post in self.posts:
          return True
      
        

    def delete(self, id):
      	remove_post = self.get_by_id(id)
      	self.posts.remove(remove_post)
    

