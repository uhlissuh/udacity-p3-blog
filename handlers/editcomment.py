from handler import Handler
import models

#allows creator of comment to edit it
class EditComment(Handler):
    def get(self, blog_id, comment_id):
        comment = models.Comment.by_id(int(comment_id))
        if comment:
            commenter_id = comment.commenter_id
            content = comment.content
            cookie_id = int(self.read_secure_cookie("id"))
            if cookie_id:
                if cookie_id == commenter_id:
                    self.render("editcomment.html", content = content)
                else:
                    self.render_404()
            else:
                self.redirect('/login')
        else:
            self.render_404()

    def post(self, blog_id, comment_id):
        comment = models.Comment.by_id(int(comment_id))
        if comment:
            cookie_id = int(self.read_secure_cookie("id"))
            commenter_id = comment.commenter_id
            if cookie_id == commenter_id:
                content = self.request.get("content")
                comment.content = content
                comment.put()
                self.redirect("/post/" + blog_id)
            else:
                self.response.set_status(404, message="not permitted")
                self.render('404_error.html')
        else:
            render_404()
