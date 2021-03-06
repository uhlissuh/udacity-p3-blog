from handler import Handler
import models

#allows creator of post to delete it
class DeletePost(Handler):
    def post(self, id):
        blog = models.BlogPost.by_id(int(id))
        if blog:
            blog_user_id = str(blog.author_id)
            cookie_id = str(self.read_secure_cookie("id"))
            if cookie_id:
                if blog_user_id == cookie_id:
                    models.BlogPost.by_id(int(id)).delete()
                    self.redirect('/')
                else:
                    self.response.set_status(404, message="not permitted")
                    self.render('404_error.html')
            else:
                self.redirect('/login')
        else:
            self.render_404()
