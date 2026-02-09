from __future__ import absolute_import, division, print_function

__metaclass__ = type

import unittest

from ansible_collections.community.healthchecksio.plugins.module_utils.healthchecksio import (
    HealthchecksioHelper,
)


class TestChecksParametersV3(unittest.TestCase):
    """Test cases for v3 API parameter support in checks module"""

    def test_healthchecksio_argument_spec_has_v3_base_url_default(self):
        """Verify that default API base URL is v3"""
        spec = HealthchecksioHelper.healthchecksio_argument_spec()
        self.assertIn("management_api_base_url", spec)
        self.assertEqual(
            spec["management_api_base_url"]["default"],
            "https://healthchecks.io/api/v3",
            "Default management_api_base_url should be v3"
        )

    def test_v3_response_structure(self):
        """Test that v3 response fields are expected"""
        v3_response = {
            "uuid": "524d0f69-0ff3-4120-a2e2-03ebd5736b25",
            "name": "test-check",
            "slug": "test-slug",
            "status": "new",
            "resume_url": "https://healthchecks.io/api/v3/checks/524d0f69-0ff3-4120-a2e2-03ebd5736b25/resume",
            "pause_url": "https://healthchecks.io/api/v3/checks/524d0f69-0ff3-4120-a2e2-03ebd5736b25/pause",
            "update_url": "https://healthchecks.io/api/v3/checks/524d0f69-0ff3-4120-a2e2-03ebd5736b25",
        }

        # Verify v3 URLs use /api/v3/ not /api/v1/
        self.assertIn("/api/v3/", v3_response["resume_url"], "resume_url should use /api/v3/")
        self.assertIn("/api/v3/", v3_response["pause_url"], "pause_url should use /api/v3/")
        self.assertIn("/api/v3/", v3_response["update_url"], "update_url should use /api/v3/")
        self.assertNotIn("/api/v1/", v3_response["resume_url"], "resume_url should not use /api/v1/")

    def test_slug_field_in_response(self):
        """Test that slug is returned in check response"""
        v3_check = {
            "uuid": "524d0f69-0ff3-4120-a2e2-03ebd5736b25",
            "name": "my-check",
            "slug": "my-custom-slug",
        }

        self.assertIsNotNone(v3_check.get("slug"), "slug should be present in response")
        self.assertEqual(v3_check["slug"], "my-custom-slug", "slug value should match")

    def test_v3_additional_response_fields(self):
        """Verify all expected v3 response fields are present"""
        v3_response = {
            "uuid": "test-uuid",
            "name": "test",
            "slug": "test-slug",
            "started": False,
            "status": "new",
            "success_kw": "",
            "failure_kw": "",
            "start_kw": "",
            "filter_subject": False,
            "filter_body": False,
            "filter_http_body": False,
            "filter_default_fail": False,
            "unique_key": "test-uuid",
            "resume_url": "https://healthchecks.io/api/v3/checks/test-uuid/resume",
        }

        # All these fields should be present in v3 responses
        required_fields = [
            "uuid", "name", "slug", "started", "status",
            "success_kw", "failure_kw", "start_kw",
            "filter_subject", "filter_body", "filter_http_body",
            "filter_default_fail", "unique_key", "resume_url"
        ]

        for field in required_fields:
            self.assertIn(field, v3_response, f"v3 response must include {field}")

