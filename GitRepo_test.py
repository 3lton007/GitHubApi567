

import unittest

from GitRepo import repo

class TestRepo(unittest.TestCase):

    def test_commit(self):
        repos = [item for item in repo("3lton007")]

        result = ["Repo: MyWorld, Commits: 4", "Repo: SSW-567, Commits: 14", "Repo: SSW810, Commits: 11", "Repo: SSW_567, Commits: 4", "Repo: Triangle567, Commits: 8"]

        self.assertEqual(repos, result)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)