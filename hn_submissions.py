from operator import itemgetter

import requests


# Create request API & save response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url=url)
print(f"Status code: {r.status_code}")

# Processing call API & save response
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Create separate call API for each article
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts,
    key=itemgetter('comments'),
    reverse=True
)

for submission_dict in submission_dicts:
    print(
        f"\nTitle: {submission_dict['title']}"
        f"\nDiscussion link: {submission_dict['hn_link']}"
        f"\nComments: {submission_dict['comments']}"
    )
