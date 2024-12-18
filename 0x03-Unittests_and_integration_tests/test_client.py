#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json', return_value={"login": "google"})
    def test_org(self, org_name, expected, mock_get_json):
        """Test GithubOrgClient.org"""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url"""
        mock_org.return_value = {"repos_url": "http://example.com/repos"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, "http://example.com/repos")

    @patch('client.get_json', return_value=[
        {"name": "repo1"}, {"name": "repo2"}])
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos"""
        mock_public_repos_url.return_value = "http://example.com/repos"
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://example.com/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class([
    {
        "org_payload": {"login": "google"},
        "repos_payload": [{"name": "repo1"}, {"name": "repo2"}],
        "expected_repos": ["repo1", "repo2"],
        "apache2_repos": ["repo1"]
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class method"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
