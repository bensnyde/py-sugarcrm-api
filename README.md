py-sugarcrm-api
===============

Python Library for SugarCRM SOAP API

  <http://support.sugarcrm.com/02_Documentation/04_Sugar_Developer/Sugar_Developer_Guide_6.5/02_Application_Framework/Web_Services/>

- Author: Benton Snyder
- Website: <http://bensnyde.me>
- Created: 5/19/13
- Updated: 3/13/15

Usage
=====
```
sugar = SugarCrm("http://sugarcrm.example.com/service/v2/soap.php", "user1", "strongpasswrod")
print sugar.get_server_info()
```
