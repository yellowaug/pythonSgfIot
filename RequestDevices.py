import requests as req

class RequestsDeviceObj:
    def __init__(self,hostip):
        self.host=hostip
    def __requestObj(self,req_data,uri):
        try:
            url=F"https://{self.host}{uri}"
            print(f"传入的参数是:{url}")
            headers = {
                "Content-Type": "application/json",
            }
            data = req_data
            response = req.post(url, json=data, headers=headers,verify=False)
            return response
        except Exception as e:
            print(e)
            return e
    def requestsAccessToken(self,secret,uri):
        # url=F"https://{self.host}{self.uri}"
        # print(f"传入的参数是:{url}")
        # headers = {
        #     "Content-Type": "application/json",
        # }

        data = {
            # "accessToken": "30612ab31213e7c1ad41ca5603fe883a",
            "secret": secret
        }
        response = self.__requestObj(req_data=data,uri=uri)
        if response.status_code == 200:
            result_dict = response.json()
            result=result_dict.get("data",[{}])[0].get("accessToken")
            print(result)
            return result
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def requestDeviceData(self,acc_token,hd_typeid,uri):
        data = {
            # "accessToken": "30612ab31213e7c1ad41ca5603fe883a",
            "accessToken": acc_token,
            "filter": {
                "all": True,
                "hardwareClassifications": ["terminal"],
                "hardwareTypeIDs": [hd_typeid]
            }
        }
        response = self.__requestObj(req_data=data,uri=uri)
        if response.status_code == 200:
            return response
        else:
            print(f"Error: {response.status_code}, {response.text}")
    def analyticalRequestsdata(self,response,dev_type,hd_name):
        # host="10.11.17.244"
        # url=F"https://{self.host}{self.uri}"
        # print(f"传入的参数是:{url}")
        # headers = {
        #     "Content-Type": "application/json",
        # }
        # data = {
        #     # "accessToken": "30612ab31213e7c1ad41ca5603fe883a",
        #     "accessToken": acc_token,
        #     "filter": {
        #         "all": True,
        #         "hardwareClassifications": ["terminal"],
        #         "hardwareTypeIDs": [hd_typeid]
        #     }
        # }
        # response = req.post(url, json=data, headers=headers,verify=False)
        # response = self.__requestObj(req_data=data)
        # if response.status_code == 200:
        result_list = response.json()
        print(result_list)
        # result_dict=json.loads(result)
        hard_list=result_list.get('data', {}).get('results', [])
        for hard in hard_list:
            hardwareName=hard.get('info',[]).get("hardwareName")
            if hardwareName == hd_name:
                print(f"温度区域：{hd_name}")
                states_list=hard.get('states', [])
                print(states_list)
                for state in states_list:
                    if state.get('stateID')==dev_type:
                        reported_value = state.get('reported')
                        print(reported_value)
                        if dev_type=="DEV_MOISTURE":
                            print(f"设备湿度: {reported_value}")
                        elif dev_type=="DEV_TEMPRATURE":
                            print(f"设备温度: {reported_value}")


                        #
                        # if dev_type=="DEV_TEMPRATURE":
                        #     reported_value = state.get('reported')
                        #     print(f"设备温度: {reported_value}")
                        # else:
                        #     print(f"Error,传入的参数是：{states_list},{hd_name},")
                    # print(state)
                    # if hardwareName=="配电柜温湿度1":
                    #     if state.get('stateID') == 'DEV_MOISTURE':
                    #         reported_value = state.get('reported')
                    #         print(f"设备湿度: {reported_value}")
                    #     if state.get('stateID') == 'DEV_TEMPRATURE':
                    #         reported_value = state.get('reported')
                    #         print(f"设备温度: {reported_value}")
                    # else:
                    #     print(f"Error:{state}")
        # else:
        #     print(f"Error: {response.status_code}, {response.text}")
        #     result_dict=response.json()


        #     states_list = result_list.get('data', {}).get('results', [])[0].get('states', [])
        #     for state in states_list:
        #         print(state)
        #         if state.get('stateID') == 'DEV_MOISTURE':
        #             reported_value = state.get('reported')
        #             print(f"设备湿度: {reported_value}")
        #         if state.get('stateID') == 'DEV_TEMPRATURE':
        #             reported_value = state.get('reported')
        #             print(f"设备温度: {reported_value}")
        # else:
        #     print(f"Error: {response.status_code}, {response.text}")