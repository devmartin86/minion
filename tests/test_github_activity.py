import vcr
import sys
from tasks.github_activity import GithubActivity

sys.path.append(".")
sys.path.append("..")


class TestGithubActivity:
    def test_commit(self):
        ga = GithubActivity()
        assert ga.commit() == "git commit --allow-empty --message 'Populating activity grid...'"

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/github_graphql_viewer.yaml')
    def test_config(self):
        token = '6f17da40b45b09a94b448cd0e0649304ce8f7364'
        ga = GithubActivity()
        assert ga.config(token) == """\
git config user.email \"65215668+devmartin86@users.noreply.github.com\"
git config user.name \"Martin Duksis\"\
"""

    def test_draw(self):
        ga = GithubActivity()
        assert ga.draw() == """\
_____________________________________________________
_____________________________________________________
_____________________________________________________
_____________________________________________________
_____________________________________________________
_____________________________________________________
_____________________________________________________"""
