from handler import Handler
import models

#allows a user to unlike a post they had previously liked
class Unlike(Handler):
    def post(self, id):
        blog = models.BlogPost.by_id(int(id))
        if blog:
            author_id = blog.author_id
            user_id = self.read_secure_cookie("id")
            if user_id != author_id:
                like =  models.Like.all().filter("blog_id =", int(id)).filter("user_id =", int(user_id)).get()
                if like:
                    like.delete()
                    self.redirect('/post/'+ id)
                else:
                    self.response.set_status(404)
                    self.render('/404_error.html')
            else:
                self.response.set_status(404)
                self.render('/404_error.html')
        else:
            self.response.set_status(404)
            self.render('/404_error.html')
