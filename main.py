from collections import Counter
from jira import JIRA
import re
from jira.client import JIRA
import json

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

def main():
    print(__name__)
    login = dict()
    file_name = "login.json" # use login_example.json with your name/pass
    with open(file_name, "r") as read_file:
        login = json.load(read_file)



    jira = JIRA(options={'server': login["server"]},
                basic_auth=(login["username"], login["password"]))





    issues = get_all_issues(jira, 'TEST', ["comment"])
    """
    ''' find all comments in all projects '''
    
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
    #open_issues = jira.search_issues(
    #    'assignee=NikolayDupak', fields='comment')



    '''
    task_name - summary # имя задания 
    assignee - исполнитель(id, email)
                - displayName
    comment 
            - author 
                    - displayName
            - body - comment text
            
    project - name
    
    description - описание задания
    '''
    from Issue import Issue
    issues = Issue
    for i in issues.issues:

    print(open_issues)
    for i in open_issues:
        print(i.raw['fields'])
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


if __name__ == '__main__':
    main()