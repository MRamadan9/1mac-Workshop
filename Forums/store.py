
class MemberStore:
    members = []
    last_id = 1

    def get_all(self):
        return(MemberStore.members)

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        result = None
        
        for member in all_members:
         if member.id == id:
             result = member
             break
        return result

    def entity_exists(self, member):
        if member in self.get_all() :
            return True
       
    def get_by_name(self, search_name):
        return [member for member in self.get_all() if member.name == search_name]

    def update(self, member):
        result = member
        all_members = self.get_all()
        
        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member
                break
        
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

    def get_by_name(self, search_name):
        return [post for post in self.get_all() if post.title == search_name]

    def update(self, post):
        result = post
        all_posts = self.get_all()

        for index, current_post in enumerate(all_posts):
            if current_post.id == post.id:
                all_posts[index] = post
                break
        
    def delete(self, id):
      remove_post = self.get_by_id(id)
      self.posts.remove(remove_post)
    