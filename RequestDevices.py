import requests as req
import json

class RequestsDeviceObj:
    def requeststo(self,uri,dev_type,hd_name):
        host="10.11.17.244"
        url=F"https://{host}{uri}"
        print(f"传入的参数是:{url}")
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            # "accessToken": "30612ab31213e7c1ad41ca5603fe883a",
            "accessToken": "a733bc4719f04d510a4d161b80bb00d6",
            "filter": {
                "all": True,
                "hardwareClassifications": ["terminal"],
                "hardwareTypeIDs": ["e1c8167f277f8266954b72b47fb44797"]
            }
        }
        response = req.post(url, json=data, headers=headers,verify=False)
        if response.status_code == 200:
            result_list = response.json()
            print(result_list)
            # result_dict=json.loads(result)
            hard_list=result_list.get('data', {}).get('results', [])
            debug_mode = True
            for hard in hard_list:
                hardwareName=hard.get('info',[]).get("hardwareName")
                if hardwareName == hd_name:
                    print(f"温度区域：{hd_name}")
                    states_list=hard.get('states', [])
                    print(states_list)
                    for state in states_list:
                        if state.get('stateID')==dev_type:
                            reported_value = state.get('reported')
                            if debug_mode:
                                if dev_type=="DEV_MOISTURE":
                                    print(f"设备湿度: {reported_value}")
                                elif dev_type=="DEV_TEMPRATURE":
                                    print(f"设备温度: {reported_value}")
                            else:
                                print(reported_value)
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
        else:
            print(f"Error: {response.status_code}, {response.text}")
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