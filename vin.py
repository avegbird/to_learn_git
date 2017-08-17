# coding: utf-8

import urllib2
VIN_TO_CAR_MESSAGE_URL_AM = 'http://api.epc.heqi.io/vin/{}?client_id=retNdnPKjkrJbYT&nonce=ea3b81a39df2bfdb8e58f1fa2939d999.1501817378&sign=5d63c0813f518b8095859a5baccde521'
VIN_TO_CAR_MESSAGE_URL_LY = 'http://api.epc.heqi.io/vin/{}/ly?client_id=retNdnPKjkrJbYT&nonce=58f9c4744941ef19d5ccb8623c1c8acb.1502352494&sign=1e0831fbf614eae9ffb59c0cbad07276'

# sublime , atom ,v code
def vin_to_car(date_path, am_to_path, ly_to_path, is_ly=0):
    vin_code = open(date_path)
    am_output = open(am_to_path, 'a')
    ly_output = open(ly_to_path, 'a')
    while True:
        list_vin_code = vin_code.readline()
        list_vin_code = list_vin_code.replace('\n', '')
        list_vin_code = list_vin_code.replace('\r', '')
        print(list_vin_code)

        if list_vin_code:
            if not is_ly:
                # am
                url = VIN_TO_CAR_MESSAGE_URL_AM.format(list_vin_code)
                print(url)
                request = urllib2.Request(url=url)
                response = urllib2.urlopen(request, timeout=30)
                data = response.read()
                response.close()
                am_output.write(data)
            else:
                #  LY
                url = VIN_TO_CAR_MESSAGE_URL_LY.format(list_vin_code)
                print(url)
                request = urllib2.Request(url=url)
                response = urllib2.urlopen(request, timeout=30)
                data = response.read()
                response.close()
                ly_output.write(data)
        else:
            break
        #单步
        # break
    print('finally')
    vin_code.close()
    am_output.close()
    ly_output.close()



# urllib2.urlopen(urllib2.Request(url='http://www.baidu.com'))
vin_to_car('/Users/wangjunfu/Desktop/git_test/data_am.txt', '/Users/wangjunfu/Desktop/git_test/am_to_path', '/Users/wangjunfu/Desktop/git_test/ly_to_path',is_ly=0)