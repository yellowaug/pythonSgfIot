from RequestDevices import RequestsDeviceObj as rdo


def requestActive():
    # Use a breakpoint in the code line below to debug your script.
    requestTo=rdo()
    uri="/iotp/api/open/deviceManagement/hardware/list"
    dev_type="DEV_MOISTURE"
    hd_name="配电柜温湿度1"
    requestTo.requeststo(uri,dev_type,hd_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    requestActive()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
