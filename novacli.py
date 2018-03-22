import requests
import json


class NovaClient(object):

    def __init__(self):
        self._openstack_tenant = "xxxx"
        self._openstack_username = "xxxx"
        self._openstack_password = "xxxx"
        self._openstack_url = "xxxx"

    def _get_token(self):
        req_url = self._openstack_url + ":5000/v2.0/tokens"
        headers =  {'content-type': 'application/json'}
        payload = {
            "auth": {
                "tenantName": self._openstack_tenant,
                "passwordCredentials": {
                    "username": self._openstack_username,
                    "password": self._openstack_password,
                }
            }
        }
        res = requests.post(req_url, data=json.dumps(payload), headers=headers)
        result = res.json()
        token = result["access"]["token"]["id"]
        tenant_id = result["access"]["token"]["tenant"]["id"]
        return token, tenant_id 

    def get_hosts(self):
        token, tenant_id = self._get_token()
        headers = {
           "X-Auth-Token":token,
           "Content-Type":"application/json"
        }
        req_url = self._openstack_url + ":8774/v2/"+tenant_id+"/os-aggregates"
        res = requests.get(req_url,headers=headers)
        result=res.json()
        return result["aggregates"] 

    def get_hypervisors(self):
        token, tenant_id = self._get_token()
        headers = {
           "X-Auth-Token":token,
           "Content-Type":"application/json"
        }
        req_url = self._openstack_url + ":8774/v2/"+tenant_id+"/os-hypervisors"
        res = requests.get(req_url,headers=headers)
        result=res.json()
        return result["hypervisors"]

    def get_hypervisor_detail(self, hyper_id):
        token, tenant_id = self._get_token()
        headers = {
           "X-Auth-Token":token,
           "Content-Type":"application/json"
        }
        req_url = self._openstack_url + ":8774/v2/"+tenant_id+"/os-hypervisors/"+hyper_id
        res = requests.get(req_url,headers=headers)
        result=res.json()
        return result["hypervisor"]

    def get_hypervisors_statistics(self):
        token, tenant_id = self._get_token()
        headers = {
           "X-Auth-Token":token,
           "Content-Type":"application/json"
        }
        req_url = self._openstack_url + ":8774/v2/"+tenant_id+"/os-hypervisors/statistics"
        res = requests.get(req_url,headers=headers)
        result=res.json()
        print(result)
   
    def get_host_detail(self, host_name):
        token, tenant_id = self._get_token()
        headers = {
           "X-Auth-Token":token,
           "Content-Type":"application/json"
        }
        req_url = self._openstack_url + ":8774/v2/"+tenant_id+"/os-hosts/"+host_name
        res = requests.get(req_url,headers=headers)
        result=res.json()
        return result["host"]
