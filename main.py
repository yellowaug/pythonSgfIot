import os

from RequestDevices import RequestsDeviceObj as rdo
from DeviceInfo import Device as dev
import time
from dotenv import load_dotenv
def requestActive():
    # Use a breakpoint in the code line below to debug your script.
    hd_typeid=dev.ROOM_TEMPERATURE_HUMIDITY_2.value
    load_dotenv()
    uri=os.getenv("URI")
    uri_devdata=os.getenv("URI_DEVICE")
    host=os.getenv("IOT_HOST")
    secretKey=os.getenv("SECRETKEY")
    dev_type="DEV_MOISTURE"
    hd_name="配电柜温湿度1"
    requestTo = rdo(hostip=host)
    acc_token=requestTo.requestsAccessToken(secret=secretKey,uri=uri)
    # response=requestTo.requestDeviceData(acc_token=acc_token,hd_typeid=hd_typeid,uri=uri_devdata)
    # requestTo.analyticalRequestsdata(response=response,dev_type=dev_type,hd_name=hd_name)

    #空调的参数
    hd_typeid_kt=dev.PRECISION_AIR_CONDITIONER_MIDEA.value
    dev_type_kt="UNIT_TEMP_OUTDOOR" #这个是获取空调湿度的参数
    dev_type_kt_wd="DEV_CURRENT_TEMP" #这个是获取空调温度的参数
    hd_name_kt="精密空调-美的-MAV013WT1N2S-电总QJF1350298-8-5-1"
    resp_kt=requestTo.requestDeviceData(acc_token,hd_typeid_kt,uri_devdata)
    sd_res=requestTo.analyticalRequestsdata(response=resp_kt,dev_type=dev_type_kt,hd_name=hd_name_kt) #获取空调湿度
    wd_res=requestTo.analyticalRequestsdata(response=resp_kt,dev_type=dev_type_kt_wd,hd_name=hd_name_kt) #获取空调温度
    print(f"空调的湿度是{sd_res}，空调的温度是{wd_res}")
    # requestTo.requeststo(uri,dev_type,hd_name,hd_typeid)

    #电量仪
    # hd_typeid_dly=dev.SOUND_AND_LIGHT_ALARM.value
    # dev_type_dly="SLA_CNT"
    # hd_name_dly="声光报警"
    # resp_dly=requestTo.requestDeviceData(acc_token=acc_token,hd_typeid=hd_typeid_dly,uri=uri_devdata)
    # requestTo.analyticalRequestsdata(response=resp_dly,dev_type=dev_type_dly,hd_name=hd_name_dly)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    now_starttime = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    msg = f"\n==========程序开始时间：{now_starttime}==================\n"
    print(msg)

    start_runtim = time.time()
    # runDelete()    #调用的方法
    requestActive()
    end_runtime = time.time()
    calculation_time = end_runtime - start_runtim
    msg1 = f"程序完成运行花费时间：{calculation_time:.6f}秒"
    print(msg1)
    now_endtime = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    msg = f"\n==============程序结束时间：{now_endtime}==============\n"
    print(msg)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
