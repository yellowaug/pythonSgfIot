import requests as req

class RequestsDeviceObj:
    def __init__(self,hostip):
        """
        初始化 RequestsDeviceObj 类。

        Parameters:
        - hostip (str): 设备的主机 IP 地址。
        """
        self.host=hostip
    def __requestObj(self,req_data,uri):
        """
        发送 HTTP 请求的私有方法。私有化方法，只供内部类使用

        Parameters:
        - req_data (dict): 请求数据，以 JSON 格式传递。
        - uri (str): 请求的 URI。

        Returns:
        - response: 请求的响应对象。
        """
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
        """
        请求获取 AccessToken。

        Parameters:
        - secret (str): 访问令牌请求的密钥。
        - uri (str): 请求 AccessToken 的 URI。

        Returns:
        - str: 获取到的 AccessToken。
        """
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
        """
        请求获取设备数据。

        Parameters:
        - acc_token (str): 访问令牌，用于验证身份。
        - hd_typeid (str): 硬件类型的 ID。
        - uri (str): 请求设备数据的 URI。

        Returns:
        - response: 请求的响应对象。
        """
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
        """
        解析设备数据的方法。

        Parameters:
        - response: 请求设备数据的响应对象。
        - dev_type (str): 设备类型，例如 'DEV_MOISTURE'。
        - hd_name (str): 设备名称。

        Prints:
        - 打印设备数据信息。
        """
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
                # print(f"温度区域：{hd_name}")
                states_list=hard.get('states', [])
                print(states_list)
                for state in states_list: #解析从传感器获得的数据并打印
                    if state.get('stateID')==dev_type:
                        reported_value = state.get('reported')
                        print(reported_value)
                        # if dev_type=="DEV_MOISTURE":
                        #     print(f"设备湿度: {reported_value}")
                        # elif dev_type=="DEV_TEMPRATURE":
                        #     print(f"设备温度: {reported_value}")


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