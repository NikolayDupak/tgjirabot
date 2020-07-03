class Issue:
    issues = None
    comments = None
    def find_issue_by_id(self, account_id, fields='comment,summary,project,assignee'):
        issues = jira.search_issues(
            f'text ~ "accountid:{account_id}"', fields=fields)
        self.issues = issues

    def project_name(self, issue):
        return issue.raw['fields']['project']['name']

    def assignee_name(self, issue):
        if issue.raw['fields']['project']['assignee'] is not None:
            return issue.raw['fields']['project']['assignee']['displayName']


    def assignee_id(self):
        pass

    def assignee_email(self):
        pass

    def comment_body(self, issue):
        if len(issue.raw['fields']['comment']['comments']) != 0:
            self.comments = issue.raw['fields']['comment']['comments']


    def comment_author_name(self):
        if len(issue.raw['fields']['comment']['comments']) != 0:

    def description(self):
        pass
# new task
def send_task(project_name, issue_name, description):
    pass
# new comment
def send_comment(project_name, issue_name, comment, comment_author):
    pass

'''
вопросы 
что надо присылать?
 проект, коммент, автора
один коммент или несколько

или "у вас новая задача/", Вас упомянули в коментарии 

перевод задачи в новый статус(мониторить статус для определенной задачи)?
'''