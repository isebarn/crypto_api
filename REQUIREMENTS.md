## ToDo

* Mongodb 4.2
* Implement the endpoints in Python 3.6 
* Separation of queries, API code and logic (if any)
* Test cases are mandatory
* Externalize the endpoint routes in a separate file
* Should support swagger documentation

* Wrap the responses in the structure given below

``` javascript
{
  "code": "200 or XYZ",
  "status": "success",
  "response": {
    "data": {} or []
  },
  "message": ""
}
```

``` javascript
{
  "code": "500",
  "status": "failure",
  "response": {
    "data": {} or []
  },
  "message": ""
}
``` 


### Agents

#### /domain_api/va/max_threshold

* GET
* No Input

``` javascript
    {
      "initial_command": "resume",//va_preference(va_preference.initial_command)
      "inclusions": "qa-claims-webappunumfineoscom"//va_prefernce(va_preference.configs.inclusions),
      "isAutomationEnabled": "false",//va_preference(va_preference.configs.is_automation_enabled)
      "OCRinclusions": "",//va_preference(va_preference.configs.ocr_inclusions)
      "AutomationConfig": "",//va_preference(va_preference.configs.automation)
      "DiskIOThreshold": -1,//va_preference(va_preference.data_sync_thresholds.disk_i/o)
      "LocalPath": "skan\\Log",//va_preference(va_preference.path.local)
      "MemoryThreshold": -1,//va_preference(va_preference.data_sync_thresholds.memory)
      "NetworkThreshold": -1,//va_preference(va_preference.data_sync_thresholds.network)
      "PerfomanceInterval": 1,//va_preference(va_preference.intervals.performance)
      "RemotePath": "/datadrive/gatewayfolder",//va_preference(va_preference.path.remote)
      "SyncInterval": 2,//va_preference(va_preference.intervals.sync)
      "Anonymize": "false",//va_preference(va_preference.configs.anonymize)
      "AutomationInterval": 1,//va_preference(va_preference.intervals.automation)
      "CPUThreshold": -1,//va_preference(va_preference.intervals.cpu)
      "PollingInterval": 60000,//va_preference(va_preference.intervals.polling)
      "ImageCountThreshold": 10,//va_preference(va_preference.data_sync_thresholds.image_count)

    }
```

* fetch info from va_prefernce collection

#### /va/desired_properties?last_sync_time=<time>&device=<device>&user=<username>
  
* GET
  
  
``` javascript
    {
      "sftp_config": {
      "hostaddress": "cpxdev-next.skan.ai",
      "username": "rcloneskan",
      "has_private_key": true,
      "password": null,
      "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAkFtOCmosfWOGFhqcg7rNSaclp/mdS6+OAVau2pdPn8jUTqAu\nb6hVDdgqQlB2mxP9Pw9QZnPBKhRprvytS2EyuaFX/zC8Av8IlJ9zHuK0/uKGSUGJ\n6NoZoMxEoQEvEp/TiFT3BSuoSopvn6YpTGbZ37hOMT1WkLfzL/9dXNrff2f8Hc5c\nocftGjFT92xfFtvmKu/6bCekkmB6Ci6a5N5fHZsQoadNDfpWHleY4fKJazt0Crv2\n/rJaupy4mKbaQyVY0QzGO0+9CHTQNAE9DLQ650CZT/ikQRTRW84yDCOk4/CbX6D0\nhnuBqEeq8ABIvDfMsgTF/eQG9dqyajaz+sHngQIBJQKCAQEAgMAjAl6yDvfmSxDQ\nyIQDM9pELggkgcYW3plrhLB3ctW2b6OfCaP41P8Q7wl+ilAZOD4XRp6XhmU7qehH\niGtybjX0iagBoc60oDsvUuXfsuW2Cfwu5G9+pCvOgcLJHnLfQj3xEnMLuBqa6FXt\ne35TngU+0fhvzS5xHPiDs650Twhcwkv3tXCc5Elkz5ZilzxwXvHplukOIkfQvO/n\ntYQMkD/dp9yDrFsdcyeNUIEgfRnLzg/XjWeSMIj+7N83NrZJlsQu+QJKHo9PIf8Q\nEu/oOjuiFF1D2yHBsO9Cf+4T78utX1nb1rdH61+2p4Yl4uhw81EsSdys/HmT2Hqu\nSBYMnQKBgQDeh5us3eNgpL+9RsLBc92yOvpZD6J8+t7pIBaAdK53QqDY0AHTKdiv\nLEzXmcmOu4m4y9SY4bTc0PvoW9eTUYnbYtiIX+ZuMXQqYRSpeMvNmOuPHBZXkh9y\nI8+5SPac49FIWU+SWMGQV9rwhJ2OS7bvPDFA0inNx7o52Uxd7k+G/QKBgQCmEa73\nHz9/dXxjuGXZwx9JVvXpCKajYY4i/vuahaObtV1HDa47lz9fI1qHr9ZC3ZyQ60I2\nIVrSPtiqp5bxw8dZd5ZWxDgyChJkXzsz+svszvrn3v2bwQXToCiDiRKUjmmBH0m5\nRL3mftLeHClpLEXyNniCDzcppnFeb6aaZkoj1QKBgQCQV/ZGncPrqSJs76DsL3sL\n0zqaoluPVp5ts/LrifSgYpHYvkZfdRbuKpK1XNXEXfh33ikJOHVQ9kKI4aCW6Mgf\nmg/pwao5o4me8tz4Tlqu37tjvzEWNUTUakGM8Q6q9KNtMwMufsK+fi0mY9vR6+xI\nJwsw9wZb9yyv5uVtXE9CzQKBgQCLI5KXsmWiJCnyr0CT2tUGGG0rBz+B98odUiy/\nvBN0nt9y4fLX+0Lu2G5xrv+fzm5rlK0YmHyGo1uV5lvfUQD37pK3ZiE+rn4cvn21\n7c1zYU7CRTVY+6rvlAZEsR1ntZaqdCkDAj49qIcoy3ykOdm9GOGBubiYhIh/jfpK\nAqzR6QKBgH9ZCU+45q7+mdp5i3JEnoBLvQoqV6FpxdJdYzt2oV9r+ll4ph7Yg0ZW\next2rlesPEiDPedsVLzsajPgCoYf1WEltZ6NdZYVeMEfZc81sf2r3chzDKgvbi/1\nYoo7ZldQbXQasaUvYqp9M1JPIbACxISVp+EFPz2xtY3XfvuNmptU\n-----END RSA PRIVATE KEY-----\n"
      },
      "device_id": "5f6c366b84d335032ce292d6",
      "commands": "resume",
      "SkanAutomationDllPath": "",
      "ListenerExePath": "",
      "LatestVaBuildNumber": "20200524",
      "LatestVaVersion": "1.3.1.1",
      "UpdateExe": false,
      "UpdateDll": false,
      "remote_path": "/datadrive/gatewayfolder",
      "inclusions": "appsuitedashcom,yatracom",
      "last_updated_time": "25/09/2020 17:02:02",
      "AutomationConfig": "",
      "domains": "[

      {'domain': 'appsuitedashcom', 'automation_enabled': 'true', 'capture_dom': 'true', 'data_field_groups': [{'id': 1, 'when': {'agent_type_pattern': '.*', 'control_id_pattern': '.*', 'event_path_pattern': '.*', 'title_pattern': '.*', 'url_pattern': '(.*)app.suitedash.com/invoices/update/(.*)(.*)'}, 'then': [{'anonymize': 'false', 'is_case_id': 'true', 'wpath': '', 'query': [{'property_type': 30003, 'property_value': 50004}, {'property_type': 30011, 'property_value': 'invoiceNumber'}], 'name': '{10}invoiceNumber', 'propertyIDs': [30045]}, {'anonymize': 'false', 'is_case_id': 'true', 'wpath': '', 'query': [{'property_type': 30003, 'property_value': 50004}, {'property_type': 30011, 'property_value': 'dueDate'}], 'name': '{10}MM/DD/YYYY', 'propertyIDs': [30045]}, {'anonymize': 'false', 'is_case_id': 'true', 'wpath': '', 'query': [{'property_type': 30003, 'property_value': 50004}, {'property_type': 30011, 'property_value': 'invoiceTitle'}], 'name': '{10}invoiceTitle', 'propertyIDs': [30045]}]}, {'id': 2, 'when': {'agent_type_pattern': '.*', 'control_id_pattern': '.*', 'event_path_pattern': '.*', 'title_pattern': '.*', 'url_pattern': '(.*)app.suitedash.com/invoices/createInvoice/(.*)(.*)'}, 'then': [{'anonymize': 'false', 'is_case_id': 'false', 'wpath': '', 'query': [{'property_type': 30003, 'property_value': 50004}, {'property_type': 30011, 'property_value': 'paymentDetails'}], 'name': '{00}paymentDetails', 'propertyIDs': [30045]}]}]}]"
    }
``` 


* fetch sftp info from sftp_settings collection (General_preferences DB)
* fetch rest of the info from participants.va_info and respective document in participants collection for domains info,
* fetch enabled applications from persona id (use persona id and match _id in personas collection (Personas DB))
  fetch only apps with applications.collect_data true (domain = app name, automation_enabled and capture_dom by default true)
* use those app ids to match persona_application_widget collection application_id (Personas DB)
* data_field_groups = persona_application_widget data_attributes
* data_field_groups.id is autogenerated when: group all 5 patterns (ie: 'agent_type_pattern' ) , take all data attributes and create the structure 
* then: similar but prefix {01} values before sending here first character in braces = state of is_case_id[1 if true] and second character in braces = anonymize[1 if true] 
  
#### /va/system_info

* PUT
* Input is given below

``` javascript
  {
      "": null,
      "": null,
      "": null,
      "": null,
      "": null,
      "": null,
      "": null,
      "": null,
      "userName": null,
      "device": null
    }

      "osVersion": null,
      "language": null,
      "cultureName": null,
      "cultureLCID": null,
      "geoLocation": null,
      "ieVersion": null,
      "chromeVersion": null,
      "fireFoxVersion": null,
      "userName": null,
      "device": null
```

* Output is success and status code

* update/insert in devices collection with data in request body with changes as per given schema

    _id: ObjectId('5f722a742930714468ed8929'),
    name: 'a',
    unique_id: 'u168380',
    os: {
        version: '6.2.9200.0', osVersion
        name: 'Microsoft Windows 10 Pro',
        locale: {
            geo_location: null, geoLocation
            time_zone: 'IST',
            day_light_saving_support: false
        },
        culture: {
            name: 'en-US', cultureName
            LCID: '1033', cultureLCID
            language: 'English (United States)' language
        },
        browser: [
            {
                name: 'IE',
                value: '9.11.17763.0' ieVersion
            },
            {
                name: 'Chrome',
                value: '84.0.4147.105' chromeVersion
            },
            {
                name: 'Firefox',
                value: 'Not Found' fireFoxVersion
            }
        ]
    },
    created_by: '',
    created_on: '',
    modified_by: '',
    modified_on: ISODate('2020-07-20T06:08:50.876Z')