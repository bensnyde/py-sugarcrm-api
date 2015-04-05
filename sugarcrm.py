"""
Python Library for SugarCRM SOAP API

    http://support.sugarcrm.com/02_Documentation/04_Sugar_Developer/Sugar_Developer_Guide_6.5/02_Application_Framework/Web_Services/

Author: Benton Snyder
Website: http://bensnyde.me
Created: 5/19/13
Updated: 3/13/15

"""
import hashlib
import base64
from suds.client import Client

class SugarCrm:
    def __init__(self, url, username, password, application="default"):
        self._client = Client(url)
        response = self._client.service.login({"user_name":username, "password":hashlib.md5(password).hexdigest()}, application)
        self._session = response.id

    # Returns server information such as version, flavor, and gmt_time
    def get_server_info(self):
        return self._client.service.get_server_info()

    # Returns the ID of the user who is logged into the current session
    def get_user_id(self):
        return self._client.service.get_user_id(self._session)

    # Retrieves a single SugarBean based on ID
    def get_entry(self, module_name, id, select_fields=[], link_name_to_fields={}):
        return self._client.service.get_entry(self._session, module_name, id, select_fields, link_name_to_fields)

    # Retrieves a list of SugarBeans based on the specified IDs
    def get_entries(self, module_name, ids=[], select_fields=[], link_name_to_fields={}):
        return self._client.service.get_entries(self._session, module_name, ids, select_fields, link_name_to_fields)

    # Retrieves a list of SugarBeans
    def get_entry_list(self, module_name, query="", order_by="", offset=0, select_fields=[], link_name_to_fields={}, max_results=0, deleted=0, favorites=0):
        return self._client.service.get_entry_list(self._session, module_name, query, order_by, offset, select_fields, link_name_to_fields, max_results, deleted, favorites)

    # Retrieves the specified number of records in a module
    def get_entries_count(self, module_name, query="", deleted=0):
        return self._client.service.get_entries_count(self._session, module_name, query, deleted)

    # Sets a single relationship between two SugarBeans
    def set_relationship(self, module_name, module_id, link_field_name, related_ids=[], name_value_list={}, delete=0):
        return self._client.service.set_relationship(self._session, module_name, module_id, link_field_name, related_ids, name_value_list, delete)

    # Sets multiple relationships between two SugarBeans
    def set_relationships(self, module_names=[], module_ids=[], link_field_names=[], related_ids=[], name_value_lists={}, deleted=[]):
        return self._client.service.set_relationships(self._session, module_names, module_ids, link_field_names, related_ids, name_value_lists, deleted)

    # Creates or updates a SugarBean
    def set_entry(self, module_name, name_value_list={}):
        return self._client.service.set_entry(self._session, module_name, name_value_list)

    # Creates or updates a list of SugarBeans
    def set_entries(self, module_name, name_value_lists={}):
        return self._client.service.set_entries(self._session)

    # Add or replace a note's attachment
    def set_note_attachment(self, id, file, filename):
        note = {
            "id": id,
            "filename": filename,
            "file": base64.b64encode(file)
        }

        return self._client.service.set_note_attachment(self._session, note)

    # Sets a new revision to the document
    def set_document_revision(self, id, file, filename, revision):
        note = {
            "id": id,
            "filename": filename,
            "file": base64.b64encode(file),
            "revision": revision
        }

        return self._client.service.set_document_revision(self._session)

    # Allows authenticated user with appropriate permission to download a document
    def get_document_revision(self, id):
        return self._client.service.get_document_revision(self._session, id)

    # Returns the ID, module_name and fields for the specified modules
    def search_by_module(self, search_string, modules, offset=0, max_results=0, assigned_user_id="", select_fields=[], unified_search_only=0, favorites=0):
        return self._client.service.search_by_module(self._session, search_string, modules, offset, max_results, assigned_user_id, select_fields, unified_search_only, favorites)

    # Retrieves the list of modules available to the current user logged into the system
    def get_available_modules(self, filter="default"):
        if filter not in ["default", "all", "mobile"]:
            raise Exception("Invalid filter specified to getAvailableModules().")

        return self._client.service.get_available_modules(self._session, filter)

    # Retrieves the ID of the default team of the user who is logged into the current session
    def get_user_team_id(self):
        return self._client.service.get_user_team_id(self._session)

    # Performs a mail merge for the specified campaign
    def set_campaign_merge(self, campaign_id, targets=[]):
        return self._client.service.set_campaign_merge(self._session, targets, campaign_id)

    # Retrieves variable definitions for fields of the specified SugarBean
    def get_module_fields(self, module_name, fields=[]):
        return self._client.service.get_module_fields(self._session, module_name, fields)