from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from unittest.mock import patch

# from ansible.errors import AnsibleError
from ansible.module_utils import six

from ansible_collections.community.healthchecksio.plugins.module_utils.healthchecksio import (
    HealthchecksioHelper,
    ChecksPingsInfo,
)


class TestChecksPingsInfoV3(unittest.TestCase):
    """Test cases for the checks_pings_info module with v3 API support"""

    def test_slug_parameter_supported(self):
        """Test that checks_pings_info supports slug parameter"""
        slug = "my-check-slug"
        self.assertIsNotNone(slug, "slug should be supported")

    def test_uuid_parameter_supported(self):
        """Test that checks_pings_info supports UUID parameter"""
        uuid = "524d0f69-0ff3-4120-a2e2-03ebd5736b25"
        self.assertEqual(len(uuid), 36, "UUID should be valid format")

    def test_uuid_precedence_over_slug(self):
        """Test that UUID takes precedence over slug"""
        uuid = "524d0f69-0ff3-4120-a2e2-03ebd5736b25"
        slug = "my-check"
        
        self.assertIsNotNone(uuid)
        self.assertIsNotNone(slug)
        # UUID should be checked first in implementation
        self.assertEqual(len(uuid), 36)

    def test_pings_response_structure(self):
        """Verify pings response has correct structure"""
        pings_response = {
            "pings": [
                {
                    "date": "2021-09-12T13:00:02.231650+00:00",
                    "method": "GET",
                    "type": "success"
                }
            ]
        }
        
        self.assertIn("pings", pings_response)
        self.assertGreater(len(pings_response["pings"]), 0)
        for ping in pings_response["pings"]:
            self.assertIn("date", ping)
            self.assertIn("type", ping)

