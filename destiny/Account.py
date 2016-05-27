# -*- coding: utf-8 -*-

"""
destiny.Account
~~~~~~~~~~~~~~~~

This class provides access to the `GetDestinyAccountSummary` endpoint of the
Destiny API.

"""
from . import utils, constants
from .Guardian import Guardian


class Account(object):
    """
    Create Account object using JSON data from the
    `GetDestinyAccountSummary` endpoint.
    :param membership_type: 'xbox' or 'psn'; needed to accurately locate player
    :param display_name: Screen name of the player
    :kwarg api_key: API key to authorize access to Destiny API (optional)
    :kwarg params: Query parameters to pass to the `requests.get()` call
    """
    def __init__(self, membership_type, display_name, **kwargs):
        self.membership_type = constants.PLATFORMS[
            str(membership_type).lower()
        ]
        self.display_name = str(display_name)
        self.set_membership_id(**kwargs)
        data = utils.get_json(constants.API_PATHS[
            'get_destiny_account_summary'
        ].format(**locals()), **kwargs)
        guardian_data = data['Response']['data'].pop('characters')
        self.guardian_data = guardian_data
        self.guardians = Guardian.guardians_from_data(guardian_data)
        self.data = data['Response']['data']

    def get(self, data_path):
        """
        Get the value from a dict entry by specifying a period-delimited string
        :param data_path: period-delimited string defining path to wanted value
        :return: value of specified key from underlying JSON object
        """
        return utils.crawl_data(self, data_path)

    def set_membership_id(self, **kwargs):
        """
        Helper method to get the membership id for the account
        """
        self.membership_id = utils.get_json(constants.API_PATHS[
            'get_membership_id_by_display_name'
        ].format(**locals()),**kwargs)['Response']