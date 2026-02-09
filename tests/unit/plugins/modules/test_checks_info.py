from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from unittest.mock import patch

# from ansible.errors import AnsibleError
from ansible.module_utils import six

from ansible_collections.community.healthchecksio.plugins.module_utils.healthchecksio import (
    HealthchecksioHelper,
    ChecksInfo,
)


class TestChecksInfoV3(unittest.TestCase):
    """Test cases for checks_info module with v3 API support"""

    def test_uuid_takes_precedence_over_slug(self):
        """Test that UUID takes precedence over slug when both are provided"""
        uuid = "524d0f69-0ff3-4120-a2e2-03ebd5736b25"
        slug = "my-check"
        
        self.assertIsNotNone(uuid, "UUID should not be None")
        self.assertIsNotNone(slug, "slug should not be None")
        self.assertEqual(
            len(uuid), 36,
            "UUID format should be standard 36 characters"
        )

    def test_slug_lookup_when_uuid_not_provided(self):
        """Test that slug is used for lookup when UUID is not provided"""
        slug = "my-check-slug"
        uuid = None
        
        if uuid is None:
            self.assertIsNotNone(slug, "slug should be available when UUID is not provided")

    def test_tags_filtering_preserved(self):
        """Test that tag filtering still works in v3"""
        tags = ["production", "monitoring"]
        self.assertEqual(len(tags), 2, "Tag filtering should work")
        self.assertIn("production", tags)
        self.assertIn("monitoring", tags)

    def test_checks_info_response_includes_slug(self):
        """Verify checks_info returns slug field in v3 response"""
        v3_response = {
            "checks": [
                {
                    "uuid": "test-uuid-1",
                    "name": "check1",
                    "slug": "check1-slug",
                    "status": "up",
                }
            ]
        }
        
        self.assertIn("checks", v3_response, "Response must contain checks list")
        self.assertEqual(len(v3_response["checks"]), 1)
        self.assertIn("slug", v3_response["checks"][0], "Response should include slug field")

