#coding=utf-8;
from allpairspy import AllPairs
from collections import OrderedDict
from Until.readExcel import excel_data
import json

def create_test_data(parame_value):
    """
    创建测试数据并存入Excel（正交法或allpairs规则创建测试集）
    :param parame_value: 参数值
    :return: True
    """
    value_data = AllPairs(parame_value)
    for i, value in enumerate(value_data):
        excel_data.excel_write_data(i+1, 1, json.dumps(value._asdict(), ensure_ascii=False), 'allPairs_data.xlsx')
        print(value)
        # a = i._asdict()  # 从namedtuple 转化为 OrderedDict
        # print(json.dumps(a)) #从OrderedDict转化为 json 字符串
    return True


login_data = OrderedDict({

})

goodlist_data = OrderedDict({ #商品列表

})

invoice_data = OrderedDict({

})


paging = OrderedDict({ #分页

})

purchase_list = OrderedDict({  #我的采购/我的供货列表/我的报价

})

saleSearch = OrderedDict({  #采销搜索
})

getFreight_data = OrderedDict({
    "spuId": [1, 0, "zxc"],
    "areaId": [110101, 9999999, "", "110102"],
    "number": [1, 0, 999999]
})

test_data = create_test_data(getFreight_data)
print(test_data)




