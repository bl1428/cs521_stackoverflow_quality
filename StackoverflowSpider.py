from stackapi import StackAPI
import datetime
import pandas as pd

# params
startDate = '2020-01-01'
endDate = '2020-01-02'

# StackAPI start
SITE = StackAPI('stackoverflow')
fromDate = int(datetime.datetime.strptime(startDate, '%Y-%m-%d').timestamp())
toDate = int(datetime.datetime.strptime(endDate, '%Y-%m-%d').timestamp())
SITE.page_size = 5 # limit per api call is 100
SITE.max_pages = 1 # number of api call

questions = SITE.fetch('questions', fromdate=fromDate, todate=toDate, sort='votes', order='desc')

# save data to daataframe
pd.set_option('display.max_columns', None)
df = pd.DataFrame(questions['items'])
print(df)

# for item in questions['items']:
#     print(item['title'])

# example response for questions, there's no content included!!
# https://api.stackexchange.com/docs/questions#page=1&pagesize=5&fromdate=2020-01-01&todate=2020-01-02&order=desc&sort=votes&filter=default&site=stackoverflow&run=true
    # {
    #     "items": [
    #         {
    #             "tags": [
    #                 "c++",
    #                 "c++11",
    #                 "types",
    #                 "stdint",
    #                 "cstdint"
    #             ],
    #             "owner": {
    #                 "reputation": 1996,
    #                 "user_id": 2534689,
    #                 "user_type": "registered",
    #                 "accept_rate": 100,
    #                 "profile_image": "https://i.stack.imgur.com/GoNJo.png?s=128&g=1",
    #                 "display_name": "Rick de Water",
    #                 "link": "https://stackoverflow.com/users/2534689/rick-de-water"
    #             },
    #             "is_answered": true,
    #             "view_count": 1447,
    #             "accepted_answer_id": 59553656,
    #             "answer_count": 2,
    #             "score": 26,
    #             "last_activity_date": 1580421796,
    #             "creation_date": 1577882201,
    #             "last_edit_date": 1580421796,
    #             "question_id": 59552571,
    #             "content_license": "CC BY-SA 4.0",
    #             "link": "https://stackoverflow.com/questions/59552571/how-to-check-if-fixed-width-integers-are-defined",
    #             "title": "How to check if fixed width integers are defined"
    #         },
    #         {
    #             "tags": [
    #                 "go",
    #                 "jetbrains-ide",
    #                 "goland"
    #             ],
    #             "owner": {
    #                 "reputation": 261,
    #                 "user_id": 12637942,
    #                 "user_type": "registered",
    #                 "profile_image": "https://www.gravatar.com/avatar/64ae0a55e5096d8b4672f482be4b886d?s=128&d=identicon&r=PG&f=1",
    #                 "display_name": "David",
    #                 "link": "https://stackoverflow.com/users/12637942/david"
    #             },
    #             "is_answered": true,
    #             "view_count": 5252,
    #             "answer_count": 8,
    #             "score": 25,
    #             "last_activity_date": 1614861337,
    #             "creation_date": 1577915594,
    #             "last_edit_date": 1577917831,
    #             "question_id": 59556394,
    #             "content_license": "CC BY-SA 4.0",
    #             "link": "https://stackoverflow.com/questions/59556394/goland-jetbrains-shows-error-message-unresolved-reference-but-code-compiles",
    #             "title": "GoLand (JetBrains) shows error message &quot;Unresolved Reference&quot;. But Code compiles and runs"
    #         },
    #         {
    #             "tags": [
    #                 "java",
    #                 "java-8",
    #                 "comparator",
    #                 "java-11",
    #                 "treeset"
    #             ],
    #             "owner": {
    #                 "reputation": 27764,
    #                 "user_id": 3764965,
    #                 "user_type": "registered",
    #                 "accept_rate": 94,
    #                 "profile_image": "https://i.stack.imgur.com/5aIx2.jpg?s=128&g=1",
    #                 "display_name": "Nikolas Charalambidis",
    #                 "link": "https://stackoverflow.com/users/3764965/nikolas-charalambidis"
    #             },
    #             "is_answered": true,
    #             "view_count": 655,
    #             "accepted_answer_id": 59553083,
    #             "answer_count": 1,
    #             "score": 21,
    #             "last_activity_date": 1577927284,
    #             "creation_date": 1577886052,
    #             "last_edit_date": 1577927145,
    #             "question_id": 59553029,
    #             "content_license": "CC BY-SA 4.0",
    #             "link": "https://stackoverflow.com/questions/59553029/why-doesnt-removing-from-a-treeset-with-a-custom-comparator-remove-a-larger-set",
    #             "title": "Why doesn&#39;t removing from a TreeSet with a custom comparator remove a larger set of items?"
    #         },
    #         {
    #             "tags": [
    #                 "c++",
    #                 "set",
    #                 "stdset"
    #             ],
    #             "owner": {
    #                 "reputation": 2328,
    #                 "user_id": 5954825,
    #                 "user_type": "registered",
    #                 "profile_image": "https://www.gravatar.com/avatar/b46e345831a9b1beeb8bfee5cbf70b6f?s=128&d=identicon&r=PG&f=1",
    #                 "display_name": "mfnx",
    #                 "link": "https://stackoverflow.com/users/5954825/mfnx"
    #             },
    #             "is_answered": true,
    #             "view_count": 2180,
    #             "accepted_answer_id": 59555327,
    #             "answer_count": 2,
    #             "score": 16,
    #             "last_activity_date": 1577969124,
    #             "creation_date": 1577905155,
    #             "last_edit_date": 1577969124,
    #             "question_id": 59555257,
    #             "content_license": "CC BY-SA 4.0",
    #             "link": "https://stackoverflow.com/questions/59555257/does-stdset-store-objects-contiguously-in-memory",
    #             "title": "Does std::set store objects contiguously in memory?"
    #         },
    #         {
    #             "tags": [
    #                 "flutter",
    #                 "dart",
    #                 "navigation",
    #                 "uinavigationbar",
    #                 "drawer"
    #             ],
    #             "owner": {
    #                 "reputation": 1616,
    #                 "user_id": 11320345,
    #                 "user_type": "registered",
    #                 "profile_image": "https://i.stack.imgur.com/Z4D76.jpg?s=128&g=1",
    #                 "display_name": "lordvidex",
    #                 "link": "https://stackoverflow.com/users/11320345/lordvidex"
    #             },
    #             "is_answered": true,
    #             "view_count": 18793,
    #             "accepted_answer_id": 59554654,
    #             "answer_count": 4,
    #             "score": 15,
    #             "last_activity_date": 1615218326,
    #             "creation_date": 1577897655,
    #             "question_id": 59554348,
    #             "content_license": "CC BY-SA 4.0",
    #             "link": "https://stackoverflow.com/questions/59554348/how-can-i-change-drawer-icon-in-flutter",
    #             "title": "How can I change Drawer icon in flutter?"
    #         }
    #     ],
    #     "has_more": true,
    #     "backoff": 10,
    #     "quota_max": 10000,
    #     "quota_remaining": 9861
    # }