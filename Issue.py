class Issue:
    issues = None
    comments = None
    from JProjects import JIssue
    from collections import Counter
    from jira import JIRA
    import re
    from jira.client import JIRA

    def __init__(self, server, username, password):
        self.all_issues = dict()
        self.jira = self.JIRA(options={'server': server},
                    basic_auth=(username, password))

        self.account_id = '5ef6468f1550750ab4f10541'

    def update(self):
        self.find_issue_by_id(self.account_id)
        for issue in self.issues:
            # print(issue.raw['fields']['project']['name'])
            new_issue = self.JIssue(issue.raw['fields']['project']['name'], issue.raw['fields']['summary'])
            if len(issue.raw['fields']['comment']['comments']) != 0:
                for comment in issue.raw['fields']['comment']['comments']:
                    # print(comment)
                    new_comment = {'author': comment['author']['displayName'],
                                   'text': comment['body'],
                                   'id': comment['id']}
                    new_issue.add_comments(new_comment)
            if issue.raw['fields']['summary'] in self.all_issues.keys():
                for comment in new_issue.get_all_comments():
                    self.all_issues[issue.raw['fields']['summary']].add_comments(comment)
            else:
                self.all_issues.update({issue.raw['fields']['summary']: new_issue})

    def print(self):
        for key, issue in self.all_issues.items():
            # print(f'Issue name - {issue.get_issue_name()}')
            while issue.have_new_comments():

                new_comm = issue.get_new_comment()
                if self.find_nickname(new_comm):
                    comm_text = new_comm['text']
                    comm_author = new_comm['author']
                    print(f'Issue name - {issue.get_issue_name()}')
                    print(f'New comment: {comm_text}\n'
                          f'from - {comm_author}')

    def find_nickname(self, comment):
        comment_text = str(comment['text'])
        if comment_text.find(self.account_id) != -1:
            return True
        return False

    def find_issue_by_id(self, account_id, fields='comment,author,summary,project,assignee,issuetype'):
        all_issues = self.jira.search_issues(
            f'text ~ "accountid:{account_id}"', fields=fields)
        self.issues = all_issues

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
            pass

    def description(self):
        pass


# new task
def send_task(project_name, issue_name, description):
    pass


# new comment
def send_comment(project_name, issue_name, comment, comment_author):
    pass


def get_all_project(jira):
    projects = jira.projects()

    for v in projects:
        print(v)
    return projects


def get_all_issues(jira_client, project_name, fields):
    issues = []
    i = 0
    chunk_size = 100
    while True:
        chunk = jira_client.search_issues(f'project = {project_name}', startAt=i, maxResults=chunk_size,
                                          fields=fields)
        i += chunk_size
        issues += chunk.iterable
        if i >= chunk.total:
            break
    return issues


def get_all_comments(jira_issue, issue):
    issue = jira_issue.issue(issue, fields='comment')
    # print(issue)
    comments = issue.fields.comment.comments
    # print(comments)
    # for comment in comments:
    #     print("Comment text : ", comment.body)
    return comments


'''jira = JIRA(options={'server': login["server"]},
            basic_auth=(login["username"], login["password"]))

issues = get_all_issues(jira, 'TEST', ["comment"])
"""
 find all comments in all projects 

projects = get_all_project(jira)
for project in projects:
    print(project)
    issues = get_all_issues(jira, project,  fields='comment')

    for issue in issues:
        print(issue)
        comments = get_all_comments(jira, issue)
        #print(comments)
        for comment in comments:
            print("Comment text : ", comment.body)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
# open_issues = jira.search_issues(
#    'assignee=NikolayDupak', fields='comment')



task_name - summary # имя задания 
assignee - исполнитель(id, email)
            - displayName
comment 
        - author 
                - displayName
        - body - comment text

project - name

description - описание задания

account_id = '5ef6468f1550750ab4f10541'
fields = 'comment,summary,project,assignee'
open_issues = jira.search_issues(
    f'text ~ "accountid:{account_id}"', fields=fields)

print(open_issues)
for i in open_issues:
    print(i.raw['fields']['assignee']['displayName'])
exit(0)

comm = ([issue.raw['fields']['comment']['comments'] for issue in open_issues])
print(comm)
for text in comm:
    if len(text) != 0:
        for message in text:
            print(message["body"])
# print(a)

# Find the top three projects containing issues reported by admin
# top_three = Counter([issue.fields.project.key for issue in issues]).most_common(3)
# print(top_three)
'''