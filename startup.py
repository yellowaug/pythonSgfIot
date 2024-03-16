import os

from RequestDevices import RequestsDeviceObj as rdo
from DeviceInfo import Device as dev
import time
from dotenv import load_dotenv
def requestActive():

    load_dotenv()

    uri=os.getenv("URI")
    uri_devdata=os.getenv("URI_DEVICE")
    host=os.getenv("IOT_HOST")
    secretKey=os.getenv("SECRETKEY")
    requestTo = rdo(hostip=host)
    acc_token=requestTo.requestsAccessToken(secret=secretKey,uri=uri)


    #空调的参数
    hd_typeid_kt=dev.PRECISION_AIR_CONDITIONER_MIDEA.value
    dev_type_kt="UNIT_TEMP_OUTDOOR" #这个是获取空调湿度的参数
    dev_type_kt_wd="DEV_CURRENT_TEMP" #这个是获取空调温度的参数
    hd_name_kt="精密空调-美的-MAV013WT1N2S-电总QJF1350298-8-5-1"
    resp_kt=requestTo.requestDeviceData(acc_token,hd_typeid_kt,uri_devdata)
    sd_res=requestTo.analyticalRequestsdata(response=resp_kt,dev_type=dev_type_kt,hd_name=hd_name_kt) #获取空调湿度
    wd_res=requestTo.analyticalRequestsdata(response=resp_kt,dev_type=dev_type_kt_wd,hd_name=hd_name_kt) #获取空调温度
    print("=================================================================")
    print(f"空调的湿度是{sd_res}，空调的温度是{wd_res}")
    print("=================================================================")
if __name__ == '__main__':
    requestActive()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
