py-sugarcrm-api
===============

Python Library for SugarCRM's SOAP API

  <http://support.sugarcrm.com/02_Documentation/04_Sugar_Developer/Sugar_Developer_Guide_6.7/02_Application_Framework/Web_Services/>

- Author: Benton Snyder
- Website: <http://bensnyde.me>
- Created: 5/19/13
- Updated: 7/3/15

Usage
=====
```
sugar = SugarCRM('http://172.17.0.46/service/v4_1/soap.php?wsdl', 'admin', 'password')
print sugar.get_server_info()

lead = {
    'first_name': 'John',
    'last_name': 'Smith',
    'title': None,
    'created_by': 1,
    'status': 'New',
    'description': None,
    'email': 'john@smith.com',
    'website': None,
    'phone_home': None,
    'phone_mobile': None,
    'phone_work': None,
    'phone_other': None,
    'phone_fax': None,
    'contact_id': None,
    'opportunity_id': None,
    'campaign_id': None,
    'primary_address_street': None,
    'primary_address_street2': None,
    'primary_address_city': None,
    'primary_address_state': None, # NY
    'primary_address_postalcode': None,
    'primary_address_country': None, # USA
    'lead_source': 'API',
}

print sugar.set_entry('Leads', lead)
```
