import vcr
import sys
from datetime import datetime
from tasks.github_activity import GithubActivity

sys.path.append(".")
sys.path.append("..")


class TestGithubActivity:
    def test_commit(self):
        today = datetime.strptime('2020-06-16 12:08:35', '%Y-%m-%d %H:%M:%S')
        ga = GithubActivity()
        assert ga.commit(date=today) == "git commit --allow-empty --date '2020-06-16 12:08:35' --message 'Populating activity grid...'"

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/github_graphql_viewer.yaml')
    def test_config(self):
        token = '6f17da40b45b09a94b448cd0e0649304ce8f7364'
        ga = GithubActivity()
        assert ga.config(token) == """\
git config user.email \"65215668+devmartin86@users.noreply.github.com\"
git config user.name \"Martin Duksis\"\
"""

    def test_hire_me(self):
        today = datetime.strptime('2020-06-16 12:08:35', '%Y-%m-%d %H:%M:%S')
        pixel_dates = []
        # Letter H
        pixel_dates.append(datetime.strptime('2019-08-05 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-08-06 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-08-07 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-08-08 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-08-09 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2019-08-14 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-08-21 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2019-08-26 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-08-27 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-08-28 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-08-29 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-08-30 12:08:35', '%Y-%m-%d %H:%M:%S'))
        # Letter I
        pixel_dates.append(datetime.strptime('2019-09-09 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-09-10 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-09-11 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-09-12 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-09-13 12:08:35', '%Y-%m-%d %H:%M:%S'))
        # Letter R
        pixel_dates.append(datetime.strptime('2019-09-23 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-09-24 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-09-25 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-09-26 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-09-27 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2019-09-30 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-10-02 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2019-10-08 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-10-10 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-10-11 12:08:35', '%Y-%m-%d %H:%M:%S'))
        # Letter E
        pixel_dates.append(datetime.strptime('2019-10-21 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-10-22 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-10-23 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-10-24 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-10-25 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2019-10-28 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-10-30 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-11-01 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2019-11-04 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-11-06 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-11-08 12:08:35', '%Y-%m-%d %H:%M:%S'))
        # Letter M
        pixel_dates.append(datetime.strptime('2019-12-02 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-12-03 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-12-04 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-12-05 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-12-06 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2019-12-10 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2019-12-16 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-12-17 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-12-18 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-12-19 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-12-20 12:08:35', '%Y-%m-%d %H:%M:%S'))
        # Letter E
        pixel_dates.append(datetime.strptime('2019-12-30 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2019-12-31 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2020-01-01 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2020-01-02 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2020-01-03 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2020-01-06 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2020-01-08 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2020-01-10 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2020-01-13 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2020-01-15 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2020-01-17 12:08:35', '%Y-%m-%d %H:%M:%S'))
        # Exclamation mark
        pixel_dates.append(datetime.strptime('2020-02-03 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2020-02-04 12:08:35', '%Y-%m-%d %H:%M:%S'))
        pixel_dates.append(datetime.strptime('2020-02-05 12:08:35', '%Y-%m-%d %H:%M:%S'))

        pixel_dates.append(datetime.strptime('2020-02-07 12:08:35', '%Y-%m-%d %H:%M:%S'))

        ga = GithubActivity()
        assert ga.hire_me(today) == pixel_dates
