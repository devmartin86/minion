import os
import requests
import json
from datetime import datetime, timedelta

class GithubActivity:
    _default_message = 'Populating activity grid...'

    def config(self, token):
        viewer = Github(token).viewer()
        user_id = viewer['databaseId']
        username = viewer['login']
        name = viewer['name']
        return f'git config user.email "{user_id}+{username}@users.noreply.github.com"\ngit config user.name "{name}"'

    def commit(self, date):
        return "git commit --allow-empty --date '%s' --message '%s'" %(date, self._default_message)

    def hire_me(self, today):
        pixel_dates = []
        current_week = today - timedelta(days=today.weekday())
        start = current_week - timedelta(weeks=45)
        # Letter H
        for i in range(5):
            pixel_dates.append(start + timedelta(days=i))
        wednesday = start + timedelta(days=2)
        pixel_dates.append(wednesday + timedelta(weeks=1))
        pixel_dates.append(wednesday + timedelta(weeks=2))
        for i in range(5):
            pixel_dates.append(start + timedelta(weeks=3, days=i))
        # Letter I
        for i in range(5):
            pixel_dates.append(start + timedelta(weeks=5, days=i))
        # Letter R
        for i in range(5):
            pixel_dates.append(start + timedelta(weeks=7, days=i))
        pixel_dates.append(start + timedelta(weeks=8, days=0))
        pixel_dates.append(start + timedelta(weeks=8, days=2))

        pixel_dates.append(start + timedelta(weeks=9, days=1))
        pixel_dates.append(start + timedelta(weeks=9, days=3))
        pixel_dates.append(start + timedelta(weeks=9, days=4))
        # Letter E
        for i in range(5):
            pixel_dates.append(start + timedelta(weeks=11, days=i))

        pixel_dates.append(start + timedelta(weeks=12, days=0))
        pixel_dates.append(start + timedelta(weeks=12, days=2))
        pixel_dates.append(start + timedelta(weeks=12, days=4))

        pixel_dates.append(start + timedelta(weeks=13, days=0))
        pixel_dates.append(start + timedelta(weeks=13, days=2))
        pixel_dates.append(start + timedelta(weeks=13, days=4))
        # Letter M
        for i in range(5):
            pixel_dates.append(start + timedelta(weeks=17, days=i))
        pixel_dates.append(start + timedelta(weeks=18, days=1))
        for i in range(5):
            pixel_dates.append(start + timedelta(weeks=19, days=i))
        # Letter E
        for i in range(5):
            pixel_dates.append(start + timedelta(weeks=21, days=i))

        pixel_dates.append(start + timedelta(weeks=22, days=0))
        pixel_dates.append(start + timedelta(weeks=22, days=2))
        pixel_dates.append(start + timedelta(weeks=22, days=4))

        pixel_dates.append(start + timedelta(weeks=23, days=0))
        pixel_dates.append(start + timedelta(weeks=23, days=2))
        pixel_dates.append(start + timedelta(weeks=23, days=4))

        # Exclamation mark !
        for i in range(3):
            pixel_dates.append(start + timedelta(weeks=26, days=i))
        pixel_dates.append(start + timedelta(weeks=26, days=4))

        return(pixel_dates)

    def work(self):
        token = os.environ['GITHUB_TOKEN']
        repo = os.environ['GITHUB_REPOSITORY']
        today = datetime.now()
        os.system(self.config(token))
        os.system(f'git remote set-url origin https://x-access-token:{token}@github.com/{repo}.git')
        os.system('git checkout master')
        # Remove old activity branch
        os.system('git push origin :activity')
        os.system('git checkout -b activity')
        for d in self.hire_me(today):
            for _i in range(3):
                os.system(self.commit(date=d))
        os.system('git push origin activity:activity')


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
