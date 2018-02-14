
class MemberStore:
    members = []


    def get_all(self):
        print self.members

    def add(self, member):
        print self.members.append(member)


class PostStore:
    posts = []

    def get_all(self):
        print self.posts

    def add(self, post):
        print self.posts.append(post)

    

