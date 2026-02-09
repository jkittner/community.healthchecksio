#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Mark Mercado <mamercad@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: checks_info
short_description: Get a list of checks
description:
  - Returns a list of checks belonging to the user, optionally filtered by one or more tags or a specific check by UUID or slug.
  - When filtering by UUID or slug, exactly one check will be returned (if it exists).
author: "Mark Mercado (@mamercad)"
version_added: 0.1.0
options:
  state:
    description:
      - C(present) will return the check(s).
    type: str
    choices: ["present"]
    default: present
  tags:
    description:
      - Filters the checks and returns only the checks that are tagged with the specified value.
      - Mutually exclusive with C(uuid) and C(slug).
    type: list
    elements: str
    required: false
  uuid:
    description:
      - If specified, returns this specific check by its UUID.
      - UUID takes precedence over slug if both are provided.
      - Mutually exclusive with C(tags).
    type: str
    required: false
  slug:
    description:
      - If specified, returns this specific check by its slug.
      - The slug is a unique identifier within the project, set when creating or updating the check.
      - UUID takes precedence if both UUID and slug are provided.
      - Mutually exclusive with C(tags).
    type: str
    required: false
extends_documentation_fragment:
  - community.healthchecksio.healthchecksio.documentation
"""

EXAMPLES = r"""
- name: Get all checks
  community.healthchecksio.checks_info:
  register: result

- name: Get checks with specific tags
  community.healthchecksio.checks_info:
    tags: ["production", "monitoring"]
  register: result

- name: Get a specific check by UUID
  community.healthchecksio.checks_info:
    uuid: "524d0f69-0ff3-4120-a2e2-03ebd5736b25"
  register: result

- name: Get a specific check by slug
  community.healthchecksio.checks_info:
    slug: "my-app-prod"
  register: result
"""

RETURN = r"""
data:
  description: Check or checks information
  returned: always
  type: dict or list of dict
  sample:
    - channels: ''
      desc: ''
      failure_kw: ''
      filter_body: false
      filter_default_fail: false
      filter_http_body: false
      filter_subject: false
      grace: 3600
      last_ping: null
      manual_resume: false
      methods: ''
      n_pings: 0
      name: test
      next_ping: null
      pause_url: https://healthchecks.io/api/v3/checks/524d0f69-0ff3-4120-a2e2-03ebd5736b25/pause
      ping_url: https://hc-ping.com/524d0f69-0ff3-4120-a2e2-03ebd5736b25
      resume_url: https://healthchecks.io/api/v3/checks/524d0f69-0ff3-4120-a2e2-03ebd5736b25/resume
      schedule: '* * * * *'
      slug: test
      started: false
      start_kw: ''
      status: new
      success_kw: ''
      tags: ''
      tz: UTC
      unique_key: 524d0f69-0ff3-4120-a2e2-03ebd5736b25
      update_url: https://healthchecks.io/api/v3/checks/524d0f69-0ff3-4120-a2e2-03ebd5736b25
      uuid: 524d0f69-0ff3-4120-a2e2-03ebd5736b25
"""


from ansible_collections.community.healthchecksio.plugins.module_utils.healthchecksio import (
    HealthchecksioHelper,
    ChecksInfo,
)
from ansible.module_utils.basic import AnsibleModule, env_fallback


def run(module):
    state = module.params.pop("state")
    checks = ChecksInfo(module)
    if state == "present":
        checks.get()


def main():
    argument_spec = HealthchecksioHelper.healthchecksio_argument_spec()
    argument_spec.update(
        state=dict(type="str", choices=["present"], default="present"),
        tags=dict(type="list", elements="str", required=False),
        uuid=dict(type="str", required=False),
        slug=dict(type="str", required=False),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=[("tags", "uuid"), ("tags", "slug")],
    )

    run(module)


if __name__ == "__main__":
    main()
