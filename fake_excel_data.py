from faker import Faker
from faker.providers import BaseProvider

fake = Faker(locale='zh_CN')


# class MyProvider(BaseProvider):
#     def foo(self) -> str:
#         return 'bar'
# fake.add_provider(MyProvider)
# fake.foo()

from faker.providers import DynamicProvider

department_provider = DynamicProvider(
     provider_name="department",
     elements=["销售部", "组织部", "人力部"],
)
fake.add_provider(department_provider)
# fake.department()

key_list = ['人名', '日期', '年龄', '销售额', '部门']
value_list = []
for i in range(1000):
    one_value_item = {
        '人名': fake.name(),  # 人名
        '日期': fake.date(),  # 日期
        '年龄': fake.random.randint(10, 100),
        '部门': fake.department(),
        '销售额': round(fake.random.uniform(100000, 200000), 2),
        '两年日期': fake.date_between('-2y').strftime('%Y-%m-%d'),  # 日期
        '月份名': fake.month_name(),  # 月份名
        '时区': fake.timezone(),
        '邮箱号': fake.ascii_email(),  # 邮箱号
        'ipv4': fake.ipv4(),
        'uri': fake.uri(),
        'url': fake.url(),
        '职位': fake.job(),
        '手机号': fake.phone_number(),
        '身份证号': fake.ssn(),
        '占位段': fake.paragraph(nb_sentences=5, variable_nb_sentences=False),
        '占位段2': fake.paragraph(nb_sentences=5, ext_word_list=['你好', '世界', '吃了吗']),
        '占位句': fake.sentence(nb_words=10),
        '行政区': fake.administrative_unit(),  # '云南省'
        '公司名': fake.company(),  # '万迅电脑科技有限公司
        '国家': fake.country(),  # 国家 '奥地利'
        '城市': fake.city(),  # 城市 '郑州市'
        '地址': fake.address(),  # 地址 '河北省巢湖县怀柔南宁路f座 169812',
        '街道': fake.street_address(),  # 街道  '邯郸路W座'
        '街道名': fake.street_name(),  # 街道名 '合肥路'
        '邮政编码': fake.postcode(),  # 邮编 '314548'
        '纬度': fake.latitude(),  # 纬度  Decimal('68.0228435')
        '经度': fake.longitude(),  # 经度 Decimal('155.964341')
        # 'W座'
        '楼座号': fake.building_number(),
        # '六安'  '宁德'
        '城市名': fake.city_name(),
        # 城市的后缀,中文是：市或县 '市'
        '城市后缀': fake.city_suffix(),
        # '梵蒂冈' '牙买加'
        '国家名称': fake.country(),
        # '高明'  '大兴'
        '区域': fake.district(),
        # '云南省' '甘肃省'
        '省份': fake.province(),
        # '王路Y座'
        '街区座号': fake.street_address(),
        # '王路Y座'
        '街名': fake.street_name(),
    }
    focus_dict = {k: v for k, v in one_value_item.items() if k in key_list}
    value_list.append(focus_dict)

import pandas as pd
file_name = '模拟数据.xlsx'
df = pd.DataFrame(value_list)
df.index.name = '序号'
df.index = df.index + 1
df.to_excel(file_name)