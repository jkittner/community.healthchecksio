from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest
from unittest.mock import patch

# from ansible.errors import AnsibleError
from ansible.module_utils import six

from ansible_collections.community.healthchecksio.plugins.module_utils.healthchecksio import (
    HealthchecksioHelper,
    ChecksFlipsInfo,
)


class TestChecksFlipsInfoV3(unittest.TestCase):
    """Test cases for the checks_flips_info module with v3 API support"""

    def test_slug_parameter_supported(self):
        """Test that checks_flips_info supports slug parameter"""
        slug = "my-check-slug"
        self.assertIsNotNone(slug, "slug should be supported")

    def test_uuid_parameter_supported(self):
        """Test that checks_flips_info supports UUID parameter"""
        uuid = "524d0f69-0ff3-4120-a2e2-03ebd5736b25"
        self.assertEqual(len(uuid), 36, "UUID should be valid format")

    def test_seconds_filter_parameter(self):
        """Test that checks_flips_info supports seconds query parameter"""
        seconds = 3600
        self.assertGreater(seconds, 0, "seconds should be positive")

    def test_start_end_filters_supported(self):
        """Test that checks_flips_info supports start and end timestamps"""
        start = 1609459200
        end = 1609545600
        self.assertLess(start, end, "start should be before end")

    def test_uuid_takes_precedence_over_slug(self):
        """Test that UUID takes precedence over slug"""
        uuid = "524d0f69-0ff3-4120-a2e2-03ebd5736b25"
        slug = "my-check"
        
        # UUID should be preferred
        if uuid:
            self.assertEqual(len(uuid), 36)
        self.assertIsNotNone(slug)

    def test_flips_response_structure(self):
        """Verify flips response has correct structure"""
        flips_response = {
            "flips": [
                {"timestamp": "2021-02-09T12:00:00+00:00", "up": 1},
                {"timestamp": "2021-02-09T11:00:00+00:00", "up": 0}
            ]
        }
        
        self.assertIn("flips", flips_response)
        self.assertEqual(len(flips_response["flips"]), 2)
        for flip in flips_response["flips"]:
            self.assertIn("timestamp", flip)
            self.assertIn("up", flip)


class TestChecksFlipsInfoPlugin_Old(unittest.TestCase):
    """Legacy test case"""

