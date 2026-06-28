import requests

# Create request API & save response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url=url, headers=headers)
print(f"Status code: {r.status_code}")

# Save response API in variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Repositories info analysis
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# First repo analysis
repo_dict = repo_dicts[0]
print(
    "\nSelected information about first repository:"
    f"\nName: {repo_dict['name']}"
    f"\nOwner: {repo_dict['owner']['login']}"
    f"\nStars: {repo_dict['stargazers_count']}"
    f"\nRepository: {repo_dict['html_url']}"
    f"\nCreated: {repo_dict['created_at']}"
    f"\nUpdated: {repo_dict['updated_at']}"
    f"\nDescription: {repo_dict['description']}"
)
