class JProjects:
    def __init__(self):
        self.name = None
        self.issues = dict()


class JIssue:
    def __init__(self, project_name, issue_name):
        self.project_name = project_name
        self.issue_name = issue_name
        self.all_comments = dict()
        self.all_comments_id = set()
        self.new_comments = list()

    def get_issue_name(self):
        return self.issue_name

    def add_comments(self, comment: dict):
        # print(comment['id'])
        if comment['id'] not in self.all_comments_id:
            self.new_comments.append(comment)
            #self.all_comments_id.add(comment['id'])

    def get_new_comment(self):
        if self.have_new_comments():
            comment = self.new_comments[0]
            # id = comment['id']
            self.all_comments.update({id: comment})
            self.all_comments_id.add(comment['id'])
            #print(self.all_comments_id)
            #print(self.new_comments)
            self.new_comments.remove(comment)
            return comment
        return None

    def get_all_comments(self):
        return self.new_comments

    def have_new_comments(self) -> bool:
        if len(self.new_comments) != 0:
            return True
        return False
