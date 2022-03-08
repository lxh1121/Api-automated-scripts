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
    "username":["18737553592", "", 187, "18712345678"],
    "pwd":["123456", "", "123", "*&^&"]
})

goodlist_data = OrderedDict({ #商品列表
    "price":[0, 1, 2, "", "1", "2344"],
    "saleVolume":[0, 1, "", "0"],
    "condition":["{'brand':123, 'lowPrice':0.23, 'highPrice':10056, 'area':'上海'}","{'brand':123, 'lowPrice':0.23, 'area':'上海'}","{'brand':123, 'area':'上海'}","{'area':'上海'}", ""],
    "categoryId":[1, 2, "", "1"],
    "keyword":["安全帽", "", "的撒回单卡山东凯隆撒撒娇的吉安市大叔大婶大所"],
    "pageNum":["1", 1, ""],
    "pageSize":["10", 10, ""]
})

invoice_data = OrderedDict({
    "type": [1, 2, "", "1"],
    "kind": [1, 2, "", "1"],
    "company": ["a公司", 12, ""],
    "number": ["1234232", 123424, ""],
    "address": ["北京", 233, ""],
    "comTel": ["13512345678", 18712345678, ""],
    "openingBank": ["建设", 123, ""],
    "account": ["123213", 123, ""],
    "way": ["1", 2, ""],
    "name": ["name", ""],
    "perPhone": ["123323", ""]
})


paging = OrderedDict({ #分页
    "categoryId":[1, 12, 100, "12"],
    "pageNum":[1, "1", "", 100],
    "pageSize":[10, "10", "", "100"]
})

purchase_list = OrderedDict({  #我的采购/我的供货列表/我的报价
    "state": [0,1,2,3,4],#(1代表待签约,2.签约中3代表已签约,4.已拒绝)  报价状态(0全部 1报价中 2已结束 3被备选)
    "pageNum": 1,
    "pageSize": 10
})

saleSearch = OrderedDict({  #采销搜索
    "content":[""],#搜索关键字
    "orderBy":[],#排序方式1 全部, 2 最新, 3 价格从高到低 4 价格从低到高
    "categoryId":[],#分类id
    "pageSize":[],#每页数据条数
    "regionId":[],#区域id
    "alloyGrade":[],#合金牌号
    "provinceId":[],#省份id
    "cityId":[],#城市id
    "typeId":[],#一级分类Id 1大宗原材料，2铝及铝型材，3备品备件，采销首页调用此接口时需传
    "brand":[],#品牌 备品备件筛选时需传
})

getFreight_data = OrderedDict({
    "spuId": [1, 0, "zxc"],
    "areaId": [110101, 9999999, "", "110102"],
    "number": [1, 0, 999999]
})

test_data = create_test_data(getFreight_data)
print(test_data)




