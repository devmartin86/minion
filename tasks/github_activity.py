import os
import requests
import json


class GithubActivity:
    _default_message = 'Populating activity grid...'

    def config(self, token):
        viewer = Github(token).viewer()
        user_id = viewer['databaseId']
        username = viewer['login']
        name = viewer['name']
        return f'git config user.email "{user_id}+{username}@users.noreply.github.com"\ngit config user.name "{name}"'

    def commit(self):
        return "git commit --allow-empty --message '%s'" % self._default_message

    def draw(self):
        return("\n".join(["_" * 53] * 7))

    def work(self):
        token = os.environ['GITHUB_TOKEN']
        repo = os.environ['GITHUB_REPOSITORY']
        os.system(self.config(token))
        os.system(f'git remote set-url origin https://x-access-token:{token}@github.com/{repo}.git')
        # Checkout the branch so we can push back to it
        os.system('git checkout master')
        os.system(self.commit())
        os.system('git push origin master')


class Github:
    _api_base = 'https://api.github.com/graphql'

    def __init__(self, token):
        self.headers = {'Authorization': 'bearer %s' % token}

    def viewer(self):
        query = 'query { viewer { login name databaseId }}'
        return self._post(query).json()['data']['viewer']

    def _post(self, query):
        resp = requests.post(self._api_base,
                             data=json.dumps({'query': query}),
                             headers=self.headers)
        return resp
