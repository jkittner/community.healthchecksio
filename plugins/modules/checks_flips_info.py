#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Mark Mercado <mamercad@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: checks_flips_info
short_description: Get a list of check flips
description:
  - Get a list of check's status changes.
  - Returns a list of "flips" this check has experienced.
  - A flip is a change of status (from "down" to "up," or from "up" to "down").
  - Optionally filter the flips by a time range.
author: "Mark Mercado (@mamercad)"
version_added: 0.1.0
options:
  state:
    description:
      - C(present) will return the check flips.
    type: str
    choices: ["present"]
    default: present
  uuid:
    description:
      - UUID of the check to get flips for.
      - UUID takes precedence over slug if both are provided.
    type: str
    required: false
  slug:
    description:
      - Slug of the check to get flips for.
      - The slug is a unique identifier within the project.
      - UUID takes precedence if both UUID and slug are provided.
    type: str
    required: false
  seconds:
    description:
      - Limit the flips to the last N seconds.
      - Cannot be combined with C(start) or C(end).
    type: int
    required: false
  start:
    description:
      - Only return flips from this Unix timestamp onwards.
      - Can be combined with C(end).
      - Cannot be combined with C(seconds).
    type: int
    required: false
  end:
    description:
      - Only return flips up to this Unix timestamp.
      - Can be combined with C(start).
      - Cannot be combined with C(seconds).
    type: int
    required: false
extends_documentation_fragment:
  - community.healthchecksio.healthchecksio.documentation
"""

EXAMPLES = r"""
- name: Get all flips for a check by UUID
  community.healthchecksio.checks_flips_info:
    uuid: "524d0f69-0ff3-4120-a2e2-03ebd5736b25"

- name: Get all flips for a check by slug
  community.healthchecksio.checks_flips_info:
    slug: "my-app-prod"

- name: Get the last 3600 seconds of flips (1 hour)
  community.healthchecksio.checks_flips_info:
    uuid: "524d0f69-0ff3-4120-a2e2-03ebd5736b25"
    seconds: 3600

- name: Get flips within a time range using Unix timestamps
  community.healthchecksio.checks_flips_info:
    uuid: "524d0f69-0ff3-4120-a2e2-03ebd5736b25"
    start: 1609459200
    end: 1609545600
"""

RETURN = r"""
data:
  description: List of check flips
  returned: always
  type: dict
  sample:
    flips:
      - timestamp: '2021-02-09T12:00:00+00:00'
        up: 1
      - timestamp: '2021-02-09T11:00:00+00:00'
        up: 0
"""


from ansible_collections.community.healthchecksio.plugins.module_utils.healthchecksio import (
    HealthchecksioHelper,
    ChecksFlipsInfo,
)
from ansible.module_utils.basic import AnsibleModule, env_fallback


def run(module):
    state = module.params.pop("state")
    flips = ChecksFlipsInfo(module)
    if state == "present":
        flips.get()


def main():
    argument_spec = HealthchecksioHelper.healthchecksio_argument_spec()
    argument_spec.update(
        state=dict(type="str", choices=["present"], default="present"),
        uuid=dict(type="str", required=False),
        slug=dict(type="str", required=False),
        seconds=dict(type="int", required=False),
        start=dict(type="int", required=False),
        end=dict(type="int", required=False),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=[("seconds", "start"), ("seconds", "end")],
    )

    run(module)


if __name__ == "__main__":
    main()
