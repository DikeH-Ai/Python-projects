#!/usr/bin/env python
import sys, requests, json

def main():
    # helper
    print("""
# inlcude helper text here
""")

    # program loop
    while True:
        # accept user input
        if len(sys.argv) > 1:
            username = sys.argv[1]
        else:
            username = input("(username)>>>").strip()
        # call get_event function
        get_event(argument=username)

# get event function
def get_event(argument):
    # handle exit
    if argument == "quit":
        print("Exiting program.......")
        sys.exit()
    api_url = f"https://api.github.com/{argument}/events/public"
    try:
        # get json data
        response = requests.get(api_url)

        # dict function for possible response
        dict_func = {
            "WatchEvent": watch_event,
            "PushEvent": PushEvent,
            "ForkEvent": ForkEvent,
            "PullRequestEvent": PullRequestEvent,
            "IssueEvent": IssueEvent,
            "IssueCommentEvent": IssueCommentEvent,
        }

        # check the response
        if response.status_code == 200:
            py_object = response.json()
            # based on event type call a function
            for event in py_object:
                if event in dict_func:
                    dict_func[event["type"]](event)
        else:
            print(response.status_code)
            print(response.json()["message"])
    except Exception as e:
        print(f"error(get_event): {str(e)}")

"""
    Output for each event
"""
# watch_event
def watch_event(event):
    try:
        repo = event["repo"]["name"]
        print(f"Starred {repo}")
    except Exception as e:
        print(f"Error(watchevent): {str(e)}")

# PushEvent
def PushEvent(event):
    try:
        repo = event["repo"]["name"]
        number_of_commits = len(event["payload"]["commits"])
        print(f"Pushed {number_of_commits} commits to {repo}")
    except Exception as e:
        print(f"Pushed 0 commit to {repo}")

# ForkEvent
def ForkEvent(event):
    try:
        repo = event["repo"]["name"]
        print(f"Fork {repo}")
    except Exception as e:
        print(f"Error(fork event): {str(e)}")

# PullRequestEvent
def PullRequestEvent(event):
    try:
        repo = event["repo"]["name"]
        action = event["payload"]["action"]
        print(f"{action} a pull request on {repo}")
    except Exception as e:
        print(f"Error(pullrequestevent): {str(e)}")
# IssueEvent
def IssueEvent(event):
    try:
        repo = event["repo"]["name"]
        action = event["payload"]["action"]
        print(f"{action} a new issue in {repo}")
    except Exception as e:
        print(f"Error(Issueevent): {str(e)}")
# IssueCommentEvent
def IssueCommentEvent(event):
    try:
        repo = event["repo"]["name"]
        action = event["payload"]["action"]
        print(f"{action} a new issue comment in {repo}")
    except Exception as e:
        print(f"Error(Issuecommentevent): {str(e)}")
if __name__ == "__main__":
    main()