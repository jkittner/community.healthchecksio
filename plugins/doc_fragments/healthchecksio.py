# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Mark Mercado <mamercad@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
options:
  api_token:
    aliases: ["api_key"]
    description:
      - Healthchecks.io API token for managing checks.
      - "There are several environment variables which can be used to provide this value:"
      - C(HEALTHCHECKSIO_MANAGEMENT_API_KEY), C(HC_MANAGEMENT_API_KEY), C(HC_MANAGEMENT_KEY)
    type: str
    required: true
notes:
  - This module uses the Healthchecks.io API v3.
  - The API base URL defaults to C(https://healthchecks.io/api/v3).
  - To use a self-hosted Healthchecks instance, set the C(management_api_base_url) parameter.
  - Slugs are unique identifiers within a project. They can be used as an alternative to UUIDs for identifying checks.
  - When both UUID and slug are provided, UUID takes precedence.
  - All timestamps in responses are in ISO 8601 format with UTC timezone.
  - Keyword filtering (start_kw, success_kw, failure_kw) is only applicable for email and HTTP-based checks.
"""
