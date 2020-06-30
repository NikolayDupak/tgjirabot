from collections import Counter
from jira import JIRA
import re
from jira.client import JIRA
import json



def main():
    print(__name__)
    login = dict()
    file_name = "login.json" # use login_example.json with your name/pass
    with open(file_name, "r") as read_file:
        login = json.load(read_file)

    # By default, the client will connect to a Jira instance started from the Atlassian Plugin SDK.
    # See
    # https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK
    # for details.


    jira = JIRA(options={'server': login["server"]},
                basic_auth=(login["username"], login["password"]))

    projects = jira.projects()

    for v in projects:
        print(v)
    props = jira.application_properties()
    print(props)

    # Find all issues reported by the admin
    open_issues = jira.search_issues(
        'assignee=NikolayDupak',
        maxResults=100, expand='changelog', fields='comment')
    # issues = jira.search_issues("assignee=NikolayDupak")
    # jira.comments(issues)
    # jira.search_issues()
    # a = jira.search_users("NikolayDupak")
    print(open_issues)
    comm = ([issue.raw['fields']['comment']['comments'] for issue in open_issues])
    print(comm)
    for text in comm:
        if len(text) != 0:
            # info = json.loads(text[0])
            print(text[0]["body"])
    # print(a)

    # Find the top three projects containing issues reported by admin
    # top_three = Counter([issue.fields.project.key for issue in issues]).most_common(3)
    # print(top_three)


if __name__ == '__main__':
    main()