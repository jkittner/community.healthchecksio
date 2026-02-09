#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Mark Mercado <mamercad@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: checks_pings_info
short_description: Get a list of check pings
description:
  - Returns a list of pings this check has received.
  - This endpoint returns pings in reverse order (most recent first).
  - The total number of returned pings depends on the account's billing plan (100 for free accounts, 1000 for paid accounts).
author: "Mark Mercado (@mamercad)"
version_added: 0.1.0
options:
  state:
    description:
      - C(present) will return the check pings.
    type: str
    choices: ["present"]
    default: present
  uuid:
    description:
      - UUID of the check to get pings for.
      - UUID takes precedence over slug if both are provided.
    type: str
    required: false
  slug:
    description:
      - Slug of the check to get pings for.
      - The slug is a unique identifier within the project.
      - UUID takes precedence if both UUID and slug are provided.
    type: str
    required: false
extends_documentation_fragment:
  - community.healthchecksio.healthchecksio.documentation
"""

EXAMPLES = r"""
- name: Get pings for a check by UUID
  community.healthchecksio.checks_pings_info:
    uuid: "524d0f69-0ff3-4120-a2e2-03ebd5736b25"

- name: Get pings for a check by slug
  community.healthchecksio.checks_pings_info:
    slug: "my-app-prod"
"""

RETURN = r"""
data:
  description: List of check pings
  returned: always
  type: dict
  sample:
    pings:
    - date: '2021-09-12T13:00:02.231650+00:00'
      method: GET
      n: 2759
      remote_addr: 58.46.132.66
      scheme: https
      type: success
      ua: curl/7.68.0
"""


from ansible_collections.community.healthchecksio.plugins.module_utils.healthchecksio import (
    HealthchecksioHelper,
    ChecksPingsInfo,
)
from ansible.module_utils.basic import AnsibleModule, env_fallback


def run(module):
    state = module.params.pop("state")
    pings = ChecksPingsInfo(module)
    if state == "present":
        pings.get()


def main():
    argument_spec = HealthchecksioHelper.healthchecksio_argument_spec()
    argument_spec.update(
        state=dict(type="str", choices=["present"], default="present"),
        uuid=dict(type="str", required=False),
        slug=dict(type="str", required=False),
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    run(module)


if __name__ == "__main__":
    main()
