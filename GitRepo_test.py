

import unittest
from unittest import mock

from GitRepo import repo

class TestRepo(unittest.TestCase):

    @mock.patch("urllib.request.urlopen")

    def test_commit(self,other):
        repos = [item for item in repo("3lton007")]

        result = ["Repo: CS-546, Commits: 8", "Repo: GitHubApi567, Commits: 11", "Repo: MyWorld, Commits: 4", "Repo: SSW-567, Commits: 14", "Repo: SSW810, Commits: 11", "Repo: SSW_567, Commits: 4", "Repo: Triangle567, Commits: 8"]

        self.assertEqual(repos, result)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
