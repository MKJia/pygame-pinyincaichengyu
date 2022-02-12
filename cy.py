# -*- coding:utf-8 -*-  
import random
import json
from turtle import end_fill


v=[[[u"\u7231",u"\u618e",u"\u5206",u"\u660e"],["ai","zeng","fen","ming"]],[[u"\u5b89",u"\u5206",u"\u5b88",u"\u5df1"],["an","fen","shou","ji"]],[[u"\u5b89",u"\u5c45",u"\u4e50",u"\u4e1a"],["an","ju","le","ye"]],[[u"\u5b89",u"\u7136",u"\u65e0",u"\u6059"],["an","ran","wu","yang"]],[[u"\u5b89",u"\u8eab",u"\u7acb",u"\u547d"],["an","shen","li","ming"]],[[u"\u978d",u"\u524d",u"\u9a6c",u"\u540e"],["an","qian","ma","hou"]],[[u"\u6309",u"\u90e8",u"\u5c31",u"\u73ed"],["an","bu","jiu","ban"]],[[u"\u6697",u"\u5ea6",u"\u9648",u"\u4ed3"],["an","du","chen","cang"]],[[u"\u6697",u"\u7bad",u"\u4f24",u"\u4eba"],["an","jian","shang","ren"]],[[u"\u6697",u"\u65e0",u"\u5929",u"\u65e5"],["an","wu","tian","ri"]],[[u"\u9eef",u"\u7136",u"\u9500",u"\u9b42"],["an","ran","xiao","hun"]],[[u"\u6602",u"\u9996",u"\u633a",u"\u80f8"],["ang","shou","ting","xiong"]],[[u"\u55f7",u"\u55f7",u"\u5f85",u"\u54fa"],["ao","ao","dai","bu"]],[[u"\u8dcb",u"\u5c71",u"\u6d89",u"\u6c34"],["ba","shan","she","shui"]],[[u"\u9738",u"\u738b",u"\u522b",u"\u59ec"],["ba","wang","bie","ji"]],[[u"\u767d",u"\u9a79",u"\u8fc7",u"\u9699"],["bai","ju","guo","xi"]],[[u"\u767d",u"\u624b",u"\u8d77",u"\u5bb6"],["bai","shou","qi","jia"]],[[u"\u767d",u"\u5934",u"\u5055",u"\u8001"],["bai","tou","xie","lao"]],[[u"\u767e",u"\u6b65",u"\u7a7f",u"\u6768"],["bai","bu","chuan","yang"]],[[u"\u767e",u"\u5c3a",u"\u7aff",u"\u5934"],["bai","chi","gan","tou"]],[[u"\u767e",u"\u5e9f",u"\u5f85",u"\u5174"],["bai","fei","dai","xing"]],[[u"\u767e",u"\u611f",u"\u4ea4",u"\u96c6"],["bai","gan","jiao","ji"]],[[u"\u767e",u"\u82b1",u"\u9f50",u"\u653e"],["bai","hua","qi","fang"]],[[u"\u767e",u"\u53e3",u"\u83ab",u"\u8fa9"],["bai","kou","mo","bian"]],[[u"\u767e",u"\u91cc",u"\u6311",u"\u4e00"],["bai","li","tiao","yi"]],[[u"\u767e",u"\u5bc6",u"\u4e00",u"\u758f"],["bai","mi","yi","shu"]],[[u"\u767e",u"\u5e74",u"\u597d",u"\u5408"],["bai","nian","hao","he"]],[[u"\u767e",u"\u9e1f",u"\u671d",u"\u51e4"],["bai","niao","chao","feng"]],[[u"\u73ed",u"\u95e8",u"\u5f04",u"\u65a7"],["ban","men","nong","fu"]],[[u"\u6591",u"\u9a73",u"\u9646",u"\u79bb"],["ban","bo","lu","li"]],[[u"\u642c",u"\u5f04",u"\u662f",u"\u975e"],["ban","nong","shi","fei"]],[[u"\u534a",u"\u9014",u"\u800c",u"\u5e9f"],["ban","tu","er","fei"]],[[u"\u5305",u"\u7f57",u"\u4e07",u"\u8c61"],["bao","luo","wan","xiang"]],[[u"\u9971",u"\u98df",u"\u7ec8",u"\u65e5"],["bao","shi","zhong","ri"]],[[u"\u62b1",u"\u5934",u"\u9f20",u"\u7a9c"],["bao","tou","shu","cuan"]],[[u"\u66b4",u"\u6b84",u"\u5929",u"\u7269"],["bao","tian","tian","wu"]],[[u"\u66b4",u"\u8df3",u"\u5982",u"\u96f7"],["bao","tiao","ru","lei"]],[[u"\u5351",u"\u8eac",u"\u5c48",u"\u819d"],["bei","gong","qu","xi"]],[[u"\u676f",u"\u5f13",u"\u86c7",u"\u5f71"],["bei","gong","she","ying"]],[[u"\u60b2",u"\u6b22",u"\u79bb",u"\u5408"],["bei","huan","li","he"]],[[u"\u60b2",u"\u5929",u"\u60af",u"\u4eba"],["bei","tian","min","ren"]],[[u"\u80cc",u"\u4e95",u"\u79bb",u"\u4e61"],["bei","jing","li","xiang"]],[[u"\u80cc",u"\u4fe1",u"\u5f03",u"\u4e49"],["bei","xin","qi","yi"]],[[u"\u672c",u"\u672b",u"\u5012",u"\u7f6e"],["ben","mo","dao","zhi"]],[[u"\u7b28",u"\u9e1f",u"\u5148",u"\u98de"],["ben","niao","xian","fei"]],[[u"\u6bd4",u"\u6bd4",u"\u7686",u"\u662f"],["bi","bi","jie","shi"]],[[u"\u95ed",u"\u95e8",u"\u9020",u"\u8f66"],["bi","men","zao","che"]],[[u"\u95ed",u"\u6708",u"\u7f9e",u"\u82b1"],["bi","yue","xiu","hua"]],[[u"\u7b5a",u"\u8def",u"\u8934",u"\u891b"],["bi","lu","lan","lv"]],[[u"\u5f0a",u"\u5e1a",u"\u81ea",u"\u73cd"],["bi","zhou","zi","zhen"]],[[u"\u907f",u"\u91cd",u"\u5c31",u"\u8f7b"],["bi","zhong","jiu","qing"]],[[u"\u97ad",u"\u957f",u"\u83ab",u"\u53ca"],["bian","chang","mo","ji"]],[[u"\u53d8",u"\u672c",u"\u52a0",u"\u5389"],["bian","ben","jia","li"]],[[u"\u904d",u"\u4f53",u"\u9cde",u"\u4f24"],["bian","ti","lin","shang"]],[[u"\u6807",u"\u65b0",u"\u7acb",u"\u5f02"],["biao","xin","li","yi"]],[[u"\u522b",u"\u51fa",u"\u5fc3",u"\u88c1"],["bie","chu","xin","cai"]],[[u"\u522b",u"\u5f00",u"\u751f",u"\u9762"],["bie","kai","sheng","mian"]],[[u"\u522b",u"\u6765",u"\u65e0",u"\u6059"],["bie","lai","wu","yang"]],[[u"\u522b",u"\u6709",u"\u6d1e",u"\u5929"],["bie","you","dong","tian"]],[[u"\u522b",u"\u6709",u"\u7528",u"\u5fc3"],["bie","you","yong","xin"]],[[u"\u5bbe",u"\u670b",u"\u6ee1",u"\u5ea7"],["bin","peng","man","zuo"]],[[u"\u5bbe",u"\u81f3",u"\u5982",u"\u5f52"],["bin","zhi","ru","gui"]],[[u"\u5f6c",u"\u5f6c",u"\u6709",u"\u793c"],["bin","bin","you","li"]],[[u"\u5175",u"\u4e0d",u"\u538c",u"\u8bc8"],["bing","bu","yan","zha"]],[[u"\u5175",u"\u614c",u"\u9a6c",u"\u4e71"],["bing","huang","ma","luan"]],[[u"\u75c5",u"\u5165",u"\u818f",u"\u8093"],["bing","ru","gao","huang"]],[[u"\u62e8",u"\u4e71",u"\u53cd",u"\u6b63"],["bo","luan","fan","zheng"]],[[u"\u62e8",u"\u4e91",u"\u89c1",u"\u65e5"],["bo","yun","jian","ri"]],[[u"\u535a",u"\u5927",u"\u7cbe",u"\u6df1"],["bo","da","jing","shen"]],[[u"\u535a",u"\u53e4",u"\u901a",u"\u4eca"],["bo","gu","tong","jin"]],[[u"\u535a",u"\u95fb",u"\u5f3a",u"\u8bc6"],["bo","wen","qiang","zhi"]],[[u"\u6355",u"\u98ce",u"\u6349",u"\u5f71"],["bu","feng","zhuo","ying"]],[[u"\u4e0d",u"\u5351",u"\u4e0d",u"\u4ea2"],["bu","bei","bu","kang"]],[[u"\u4e0d",u"\u803b",u"\u4e0b",u"\u95ee"],["bu","chi","xia","wen"]],[[u"\u4e0d",u"\u51fa",u"\u6240",u"\u6599"],["bu","chu","suo","liao"]],[[u"\u4e0d",u"\u8f9e",u"\u800c",u"\u522b"],["bu","ci","er","bie"]],[[u"\u4e0d",u"\u6253",u"\u81ea",u"\u62db"],["bu","da","zi","zhao"]],[[u"\u4e0d",u"\u52a8",u"\u58f0",u"\u8272"],["bu","dong","sheng","se"]],[[u"\u4e0d",u"\u5206",u"\u4f2f",u"\u4ef2"],["bu","fen","bo","zhong"]],[[u"\u4e0d",u"\u8d1f",u"\u4f17",u"\u671b"],["bu","fu","zhong","wang"]],[[u"\u4e0d",u"\u5171",u"\u6234",u"\u5929"],["bu","gong","dai","tian"]],[[u"\u4e0d",u"\u52a0",u"\u601d",u"\u7d22"],["bu","jia","si","suo"]],[[u"\u4e0d",u"\u89c1",u"\u5929",u"\u65e5"],["bu","jian","tian","ri"]],[[u"\u4e0d",u"\u80eb",u"\u800c",u"\u8d70"],["bu","jing","er","zou"]],[[u"\u4e0d",u"\u62d8",u"\u5c0f",u"\u8282"],["bu","ju","xiao","jie"]],[[u"\u4e0d",u"\u52b3",u"\u800c",u"\u83b7"],["bu","lao","er","huo"]],[[u"\u4e0d",u"\u8c0b",u"\u800c",u"\u5408"],["bu","mou","er","he"]],[[u"\u4e0d",u"\u52a1",u"\u6b63",u"\u4e1a"],["bu","wu","zheng","ye"]],[[u"\u4e0d",u"\u5b66",u"\u65e0",u"\u672f"],["bu","xue","wu","shu"]],[[u"\u4e0d",u"\u8a00",u"\u800c",u"\u55bb"],["bu","yan","er","yu"]],[[u"\u4e0d",u"\u9057",u"\u4f59",u"\u529b"],["bu","yi","yu","li"]],[[u"\u4e0d",u"\u4e49",u"\u4e4b",u"\u8d22"],["bu","yi","zhi","cai"]],[[u"\u4e0d",u"\u7531",u"\u81ea",u"\u4e3b"],["bu","you","zi","zhu"]],[[u"\u4e0d",u"\u7ea6",u"\u800c",u"\u540c"],["bu","yue","er","tong"]],[[u"\u4e0d",u"\u62e9",u"\u624b",u"\u6bb5"],["bu","ze","shou","duan"]],[[u"\u4e0d",u"\u8db3",u"\u4e3a",u"\u5947"],["bu","zu","wei","qi"]],[[u"\u6b65",u"\u5c65",u"\u8e52",u"\u8dda"],["bu","lv","pan","shan"]],[[u"\u6b65",u"\u5c65",u"\u7ef4",u"\u8270"],["bu","lv","wei","jian"]],[[u"\u624d",u"\u758f",u"\u5b66",u"\u6d45"],["cai","shu","xue","qian"]],[[u"\u6b8b",u"\u676f",u"\u51b7",u"\u7099"],["can","bei","leng","zhi"]],[[u"\u4ed3",u"\u7687",u"\u5931",u"\u63aa"],["cang","huang","shi","cuo"]],[[u"\u6ca7",u"\u6d77",u"\u6851",u"\u7530"],["cang","hai","sang","tian"]],[[u"\u6ca7",u"\u6d77",u"\u4e00",u"\u7c9f"],["cang","hai","yi","su"]],[[u"\u85cf",u"\u9f99",u"\u5367",u"\u864e"],["cang","long","wo","hu"]],[[u"\u85cf",u"\u6c61",u"\u7eb3",u"\u57a2"],["cang","wu","na","gou"]],[[u"\u8349",u"\u8239",u"\u501f",u"\u7bad"],["cao","chuan","jie","jian"]],[[u"\u8349",u"\u6728",u"\u7686",u"\u5175"],["cao","mu","jie","bing"]],[[u"\u607b",u"\u9690",u"\u4e4b",u"\u5fc3"],["ce","yin","zhi","xin"]],[[u"\u5c42",u"\u5ce6",u"\u8fed",u"\u5d82"],["ceng","luan","die","zhang"]],[[u"\u63d2",u"\u79d1",u"\u6253",u"\u8be8"],["cha","ke","da","hun"]],[[u"\u5bdf",u"\u8a00",u"\u89c2",u"\u8272"],["cha","yan","guan","se"]],[[u"\u5dee",u"\u5f3a",u"\u4eba",u"\u610f"],["cha","qiang","ren","yi"]],[[u"\u957f",u"\u6b4c",u"\u5f53",u"\u54ed"],["chang","ge","dang","ku"]],[[u"\u957f",u"\u8bdd",u"\u77ed",u"\u8bf4"],["chang","hua","duan","shuo"]],[[u"\u957f",u"\u7bc7",u"\u5927",u"\u8bba"],["chang","pian","da","lun"]],[[u"\u957f",u"\u7bc7",u"\u7d2f",u"\u724d"],["chang","pian","lei","du"]],[[u"\u5e38",u"\u5e74",u"\u7d2f",u"\u6708"],["chang","nian","lei","yue"]],[[u"\u7545",u"\u6240",u"\u6b32",u"\u8a00"],["chang","suo","yu","yan"]],[[u"\u671d",u"\u4e09",u"\u66ae",u"\u56db"],["zhao","san","mu","si"]],[[u"\u671d",u"\u751f",u"\u66ae",u"\u6b7b"],["zhao","sheng","mu","si"]],[[u"\u8f66",u"\u6c34",u"\u9a6c",u"\u9f99"],["che","shui","ma","long"]],[[u"\u8f66",u"\u8f7d",u"\u6597",u"\u91cf"],["che","zai","dou","liang"]],[[u"\u6c89",u"\u9c7c",u"\u843d",u"\u96c1"],["chen","yu","luo","yan"]],[[u"\u9648",u"\u8bcd",u"\u6ee5",u"\u8c03"],["chen","ci","lan","diao"]],[[u"\u9648",u"\u89c4",u"\u964b",u"\u4e60"],["chen","gui","lou","xi"]],[[u"\u6668",u"\u949f",u"\u66ae",u"\u9f13"],["chen","zhong","mu","gu"]],[[u"\u8d81",u"\u706b",u"\u6253",u"\u52ab"],["chen","huo","da","jie"]],[[u"\u8d81",u"\u865a",u"\u800c",u"\u5165"],["chen","xu","er","ru"]],[[u"\u77a0",u"\u76ee",u"\u7ed3",u"\u820c"],["cheng","mu","jie","she"]],[[u"\u6210",u"\u4eba",u"\u4e4b",u"\u7f8e"],["cheng","ren","zhi","mei"]],[[u"\u627f",u"\u524d",u"\u542f",u"\u540e"],["cheng","qian","qi","hou"]],[[u"\u627f",u"\u4e0a",u"\u542f",u"\u4e0b"],["cheng","shang","qi","xia"]],[[u"\u4e58",u"\u98ce",u"\u7834",u"\u6d6a"],["cheng","feng","po","lang"]],[[u"\u8d81",u"\u70ed",u"\u6253",u"\u94c1"],["chen","re","da","tie"]],[[u"\u4e58",u"\u4eba",u"\u4e4b",u"\u5371"],["cheng","ren","zhi","wei"]],[[u"\u4e58",u"\u865a",u"\u800c",u"\u5165"],["cheng","xu","er","ru"]],[[u"\u75f4",u"\u4eba",u"\u8bf4",u"\u68a6"],["chi","ren","shuo","meng"]],[[u"\u8fdf",u"\u66ae",u"\u4e4b",u"\u5e74"],["chi","mu","zhi","nian"]],[[u"\u6301",u"\u4e4b",u"\u4ee5",u"\u6052"],["chi","zhi","yi","heng"]],[[u"\u8d64",u"\u624b",u"\u7a7a",u"\u62f3"],["chi","shou","kong","quan"]],[[u"\u5145",u"\u8033",u"\u4e0d",u"\u95fb"],["chong","er","bu","wen"]],[[u"\u62bd",u"\u4e1d",u"\u5265",u"\u8327"],["chou","si","bao","jian"]],[[u"\u81ed",u"\u540d",u"\u662d",u"\u8457"],["chou","ming","zhao","zhu"]],[[u"\u81ed",u"\u5473",u"\u76f8",u"\u6295"],["chou","wei","xiang","tou"]],[[u"\u51fa",u"\u5c14",u"\u53cd",u"\u5c14"],["chu","er","fan","er"]],[[u"\u51fa",u"\u7c7b",u"\u62d4",u"\u8403"],["chu","lei","ba","cui"]],[[u"\u51fa",u"\u8c0b",u"\u5212",u"\u7b56"],["chu","mou","hua","ce"]],[[u"\u51fa",u"\u4eba",u"\u5934",u"\u5730"],["chu","ren","tou","di"]],[[u"\u51fa",u"\u795e",u"\u5165",u"\u5316"],["chu","shen","ru","hua"]],[[u"\u51fa",u"\u5e08",u"\u4e0d",u"\u5229"],["chu","shi","bu","li"]],[[u"\u51fa",u"\u6c34",u"\u8299",u"\u84c9"],["chu","shui","fu","rong"]],[[u"\u51fa",u"\u8a00",u"\u4e0d",u"\u900a"],["chu","yan","bu","xun"]],[[u"\u521d",u"\u51fa",u"\u8305",u"\u5e90"],["chu","chu","mao","lu"]],[[u"\u9504",u"\u5f3a",u"\u6276",u"\u5f31"],["chu","qiang","fu","ruo"]],[[u"\u695a",u"\u695a",u"\u52a8",u"\u4eba"],["chu","chu","dong","ren"]],[[u"\u5904",u"\u5fc3",u"\u79ef",u"\u8651"],["chu","xin","ji","lv"]],[[u"\u6035",u"\u76ee",u"\u60ca",u"\u5fc3"],["chu","mu","jing","xin"]],[[u"\u89e6",u"\u666f",u"\u751f",u"\u60c5"],["chu","jing","sheng","qing"]],[[u"\u89e6",u"\u7c7b",u"\u65c1",u"\u901a"],["chu","lei","pang","tong"]],[[u"\u7a7f",u"\u51ff",u"\u9644",u"\u4f1a"],["chuan","zao","fu","hui"]],[[u"\u7a7f",u"\u9488",u"\u5f15",u"\u7ebf"],["chuan","zhen","yin","xian"]],[[u"\u5439",u"\u6bdb",u"\u6c42",u"\u75b5"],["chui","mao","qiu","ci"]],[[u"\u5782",u"\u5934",u"\u4e27",u"\u6c14"],["chui","tou","sang","qi"]],[[u"\u5782",u"\u6d8e",u"\u4e09",u"\u5c3a"],["chui","xian","san","chi"]],[[u"\u6376",u"\u80f8",u"\u987f",u"\u8db3"],["chui","xiong","dun","zu"]],[[u"\u6625",u"\u98ce",u"\u5316",u"\u96e8"],["chun","feng","hua","yu"]],[[u"\u5507",u"\u4ea1",u"\u9f7f",u"\u5bd2"],["chun","wang","chi","han"]],[[u"\u8822",u"\u8822",u"\u6b32",u"\u52a8"],["chun","chun","yu","dong"]],[[u"\u7ef0",u"\u7ef0",u"\u6709",u"\u4f59"],["chuo","chuo","you","yu"]],[[u"\u6b64",u"\u8d77",u"\u5f7c",u"\u4f0f"],["ci","qi","bi","fu"]],[[u"\u4ece",u"\u4e00",u"\u800c",u"\u7ec8"],["cong","yi","er","zhong"]],[[u"\u7c97",u"\u679d",u"\u5927",u"\u53f6"],["cu","zhi","da","ye"]],[[u"\u6253",u"\u8349",u"\u60ca",u"\u86c7"],["da","cao","jing","she"]],[[u"\u5927",u"\u6750",u"\u5c0f",u"\u7528"],["da","cai","xiao","yong"]],[[u"\u5927",u"\u6d77",u"\u635e",u"\u9488"],["da","hai","lao","zhen"]],[[u"\u5927",u"\u60ca",u"\u5c0f",u"\u602a"],["da","jing","xiao","guai"]],[[u"\u5927",u"\u5757",u"\u6735",u"\u9890"],["da","kuai","duo","yi"]],[[u"\u5927",u"\u5668",u"\u665a",u"\u6210"],["da","qi","wan","cheng"]],[[u"\u5927",u"\u5ead",u"\u5e7f",u"\u4f17"],["da","ting","guang","zhong"]],[[u"\u5927",u"\u97f3",u"\u5e0c",u"\u58f0"],["da","yin","xi","sheng"]],[[u"\u5927",u"\u5f20",u"\u65d7",u"\u9f13"],["da","zhang","qi","gu"]],[[u"\u5927",u"\u667a",u"\u82e5",u"\u611a"],["da","zhi","ruo","yu"]],[[u"\u5446",u"\u82e5",u"\u6728",u"\u9e21"],["dai","ruo","mu","ji"]],[[u"\u6b9a",u"\u7cbe",u"\u7aed",u"\u8651"],["dan","jing","jie","lv"]],[[u"\u80c6",u"\u6218",u"\u5fc3",u"\u60ca"],["dan","zhan","xin","jing"]],[[u"\u5f39",u"\u51a0",u"\u76f8",u"\u5e86"],["tan","guan","xiang","qing"]],[[u"\u5f39",u"\u5c3d",u"\u7cae",u"\u7edd"],["dan","jin","liang","jue"]],[[u"\u5f53",u"\u4ec1",u"\u4e0d",u"\u8ba9"],["dang","ren","bu","rang"]],[[u"\u9053",u"\u8c8c",u"\u5cb8",u"\u7136"],["dao","mao","an","ran"]],[[u"\u9053",u"\u542c",u"\u9014",u"\u8bf4"],["dao","ting","tu","shuo"]],[[u"\u5f97",u"\u624b",u"\u5e94",u"\u5fc3"],["de","shou","ying","xin"]],[[u"\u5f97",u"\u610f",u"\u5fd8",u"\u5f62"],["de","yi","wang","xing"]],[[u"\u5fb7",u"\u624d",u"\u517c",u"\u5907"],["de","cai","jian","bei"]],[[u"\u767b",u"\u5cf0",u"\u9020",u"\u6781"],["deng","feng","zao","ji"]],[[u"\u7b49",u"\u95f2",u"\u4e4b",u"\u8f88"],["deng","xian","zhi","bei"]],[[u"\u4f4e",u"\u5531",u"\u6d45",u"\u914c"],["di","chang","qian","zhuo"]],[[u"\u98a0",u"\u6c9b",u"\u6d41",u"\u79bb"],["dian","pei","liu","li"]],[[u"\u70b9",u"\u77f3",u"\u6210",u"\u91d1"],["dian","shi","cheng","jin"]],[[u"\u96d5",u"\u866b",u"\u5c0f",u"\u6280"],["diao","chong","xiao","ji"]],[[u"\u4e1c",u"\u7a97",u"\u4e8b",u"\u53d1"],["dong","chuang","shi","fa"]],[[u"\u4e1c",u"\u65bd",u"\u6548",u"\u98a6"],["dong","shi","xiao","pin"]],[[u"\u72ec",u"\u8f9f",u"\u8e4a",u"\u5f84"],["du","pi","xi","jing"]],[[u"\u72ec",u"\u5584",u"\u5176",u"\u8eab"],["du","shan","qi","shen"]],[[u"\u8d4c",u"\u7269",u"\u601d",u"\u4eba"],["du","wu","si","ren"]],[[u"\u5ea6",u"\u65e5",u"\u5982",u"\u5e74"],["du","ri","ru","nian"]],[[u"\u65ad",u"\u58c1",u"\u6b8b",u"\u57a3"],["duan","bi","can","yuan"]],[[u"\u65ad",u"\u7ae0",u"\u53d6",u"\u610f"],["duan","zhang","qu","yi"]],[[u"\u5bf9",u"\u9152",u"\u5f53",u"\u6b4c"],["dui","jiu","dang","ge"]],[[u"\u5bf9",u"\u725b",u"\u5f39",u"\u7434"],["dui","niu","tan","qin"]],[[u"\u5c14",u"\u865e",u"\u6211",u"\u8bc8"],["er","yu","wo","zha"]],[[u"\u8033",u"\u9b13",u"\u53ae",u"\u78e8"],["er","bin","si","mo"]],[[u"\u53cd",u"\u749e",u"\u5f52",u"\u771f"],["fan","pu","gui","zhen"]],[[u"\u65b9",u"\u5174",u"\u672a",u"\u827e"],["fang","xing","wei","ai"]],[[u"\u9632",u"\u5fae",u"\u675c",u"\u6e10"],["fang","wei","du","jian"]],[[u"\u653e",u"\u6d6a",u"\u5f62",u"\u9ab8"],["fang","lang","xing","hai"]],[[u"\u98de",u"\u626c",u"\u8dcb",u"\u6248"],["fei","yang","ba","hu"]],[[u"\u5206",u"\u9053",u"\u626c",u"\u9573"],["fen","dao","yang","biao"]],[[u"\u7eb7",u"\u81f3",u"\u6c93",u"\u6765"],["fen","zhi","ta","lai"]],[[u"\u5fff",u"\u4e16",u"\u5ac9",u"\u4fd7"],["fen","shi","ji","su"]],[[u"\u98ce",u"\u9910",u"\u9732",u"\u5bbf"],["feng","can","lu","su"]],[[u"\u98ce",u"\u5c18",u"\u4ec6",u"\u4ec6"],["feng","chen","pu","pu"]],[[u"\u98ce",u"\u53e3",u"\u6d6a",u"\u5c16"],["feng","kou","lang","jian"]],[[u"\u98ce",u"\u58f0",u"\u9e64",u"\u5533"],["feng","sheng","he","li"]],[[u"\u5cf0",u"\u56de",u"\u8def",u"\u8f6c"],["feng","hui","lu","zhuan"]],[[u"\u950b",u"\u8292",u"\u6bd5",u"\u9732"],["feng","mang","bi","lu"]],[[u"\u9022",u"\u51f6",u"\u5316",u"\u5409"],["feng","xiong","hua","ji"]],[[u"\u51e4",u"\u6bdb",u"\u9e9f",u"\u89d2"],["feng","mao","lin","jiao"]],[[u"\u5426",u"\u6781",u"\u6cf0",u"\u6765"],["pi","ji","tai","lai"]],[[u"\u91dc",u"\u5e95",u"\u62bd",u"\u85aa"],["fu","di","chou","xin"]],[[u"\u8d1f",u"\u8346",u"\u8bf7",u"\u7f6a"],["fu","jing","qing","zui"]],[[u"\u8d1f",u"\u9685",u"\u987d",u"\u6297"],["fu","yu","wan","kang"]],[[u"\u8d74",u"\u6c64",u"\u8e48",u"\u706b"],["fu","tang","dao","huo"]],[[u"\u9ad8",u"\u5c71",u"\u6d41",u"\u6c34"],["gao","shan","liu","shui"]],[[u"\u9694",u"\u9774",u"\u6414",u"\u75d2"],["ge","xue","sao","yang"]],[[u"\u6839",u"\u6df1",u"\u8482",u"\u56fa"],["gen","shen","di","gu"]],[[u"\u803f",u"\u803f",u"\u4e8e",u"\u6000"],["geng","geng","yu","huai"]],[[u"\u529f",u"\u4e8f",u"\u4e00",u"\u7bd1"],["gong","kui","yi","kui"]],[[u"\u89e5",u"\u7b79",u"\u4ea4",u"\u9519"],["gong","chou","jiao","cuo"]],[[u"\u6cbd",u"\u540d",u"\u9493",u"\u8a89"],["gu","ming","diao","yu"]],[[u"\u6545",u"\u6b65",u"\u81ea",u"\u5c01"],["gu","bu","zi","feng"]],[[u"\u6545",u"\u5f04",u"\u7384",u"\u865a"],["gu","nong","xuan","xu"]],[[u"\u987e",u"\u6b64",u"\u5931",u"\u5f7c"],["gu","ci","shi","bi"]],[[u"\u987e",u"\u5f71",u"\u81ea",u"\u601c"],["gu","ying","zi","lian"]],[[u"\u6302",u"\u4e00",u"\u6f0f",u"\u4e07"],["gua","yi","lou","wan"]],[[u"\u7ba1",u"\u4e2d",u"\u7aa5",u"\u8c79"],["guan","zhong","kui","bao"]],[[u"\u8fc7",u"\u6cb3",u"\u62c6",u"\u6865"],["guo","he","chai","qiao"]],[[u"\u8fc7",u"\u72b9",u"\u4e0d",u"\u53ca"],["guo","you","bu","ji"]],[[u"\u6d77",u"\u5e95",u"\u635e",u"\u9488"],["hai","di","lao","zhen"]],[[u"\u6c57",u"\u725b",u"\u5145",u"\u680b"],["han","niu","chong","dong"]],[[u"\u6c86",u"\u7023",u"\u4e00",u"\u6c14"],["hang","xie","yi","qi"]],[[u"\u7ea2",u"\u674f",u"\u51fa",u"\u5899"],["hong","xing","chu","qiang"]],[[u"\u56eb",u"\u56f5",u"\u541e",u"\u67a3"],["hu","lun","tun","zao"]],[[u"\u864e",u"\u89c6",u"\u7708",u"\u7708"],["hu","shi","dan","dan"]],[[u"\u82b1",u"\u8a00",u"\u5de7",u"\u8bed"],["hua","yan","qiao","yu"]],[[u"\u54d7",u"\u4f17",u"\u53d6",u"\u5ba0"],["hua","zhong","qu","chong"]],[[u"\u5316",u"\u9669",u"\u4e3a",u"\u5937"],["hua","xian","wei","yi"]],[[u"\u753b",u"\u86c7",u"\u6dfb",u"\u8db3"],["hua","she","tian","zu"]],[[u"\u753b",u"\u9f99",u"\u70b9",u"\u775b"],["hua","long","dian","jing"]],[[u"\u6000",u"\u624d",u"\u4e0d",u"\u9047"],["huai","cai","bu","yu"]],[[u"\u7115",u"\u7136",u"\u4e00",u"\u65b0"],["huan","ran","yi","xin"]],[[u"\u6d51",u"\u7136",u"\u5929",u"\u6210"],["hun","ran","tian","cheng"]],[[u"\u96c6",u"\u814b",u"\u6210",u"\u88d8"],["ji","ye","cheng","qiu"]],[[u"\u5bb6",u"\u55bb",u"\u6237",u"\u6653"],["jia","yu","hu","xiao"]],[[u"\u89c1",u"\u5fae",u"\u77e5",u"\u8457"],["jian","wei","zhi","zhu"]],[[u"\u91d1",u"\u7389",u"\u826f",u"\u8a00"],["jin","yu","liang","yan"]],[[u"\u6765",u"\u9f99",u"\u53bb",u"\u8109"],["lai","long","qu","mai"]],[[u"\u6765",u"\u65e5",u"\u65b9",u"\u957f"],["lai","ri","fang","chang"]],[[u"\u52b1",u"\u7cbe",u"\u56fe",u"\u6cbb"],["li","jing","tu","zhi"]],[[u"\u826f",u"\u8fb0",u"\u5409",u"\u65e5"],["liang","chen","ji","ri"]],[[u"\u9189",u"\u751f",u"\u68a6",u"\u6b7b"],["zui","sheng","meng","si"]],[[u"\u8d70",u"\u9a6c",u"\u89c2",u"\u82b1"],["zou","ma","guan","hua"]],[[u"\u81ea",u"\u6295",u"\u7f57",u"\u7f51"],["zi","tou","luo","wang"]],[[u"\u7d2b",u"\u6c14",u"\u4e1c",u"\u6765"],["zi","qi","dong","lai"]],[[u"\u5fe0",u"\u8a00",u"\u9006",u"\u8033"],["zhong","yan","ni","er"]],[[u"\u7f6e",u"\u82e5",u"\u7f54",u"\u95fb"],["zhi","ruo","wang","wen"]],[[u"\u5fd7",u"\u540c",u"\u9053",u"\u5408"],["zhi","tong","dao","he"]],[[u"\u6307",u"\u9e7f",u"\u4e3a",u"\u9a6c"],["zhi","lu","wei","ma"]],[[u"\u996e",u"\u9e29",u"\u6b62",u"\u6e34"],["yin","zhen","zhi","ke"]],[[u"\u56e0",u"\u7978",u"\u5f97",u"\u798f"],["yin","huo","de","fu"]],[[u"\u6613",u"\u5982",u"\u53cd",u"\u638c"],["yi","ru","fan","zhang"]],[[u"\u4e00",u"\u89c6",u"\u540c",u"\u4ec1"],["yi","shi","tong","ren"]],[[u"\u4e00",u"\u77f3",u"\u4e8c",u"\u9e1f"],["yi","shi","er","niao"]],[[u"\u4e00",u"\u4e18",u"\u4e4b",u"\u8c89"],["yi","qiu","zhi","he"]],[[u"\u4e00",u"\u9e23",u"\u60ca",u"\u4eba"],["yi","ming","jing","ren"]],[[u"\u591c",u"\u4ee5",u"\u7ee7",u"\u65e5"],["ye","yi","ji","ri"]],[[u"\u54ac",u"\u6587",u"\u56bc",u"\u5b57"],["yao","wen","jiao","zi"]],[[u"\u773c",u"\u82b1",u"\u7f2d",u"\u4e71"],["yan","hua","liao","luan"]],[[u"\u96c5",u"\u4fd7",u"\u5171",u"\u8d4f"],["ya","su","gong","shang"]],[[u"\u5168",u"\u529b",u"\u4ee5",u"\u8d74"],["quan","li","yi","fu"]],[[u"\u8131",u"\u9896",u"\u800c",u"\u51fa"],["tuo","ying","er","chu"]],[[u"\u5b9e",u"\u4e8b",u"\u6c42",u"\u662f"],["shi","shi","qiu","shi"]],[[u"\u4e00",u"\u5982",u"\u65e2",u"\u5f80"],["yi","ru","ji","wang"]],[[u"\u4f17",u"\u6240",u"\u5468",u"\u77e5"],["zhong","suo","zhou","zhi"]],[[u"\u56e0",u"\u5730",u"\u5236",u"\u5b9c"],["yin","di","zhi","yi"]],[[u"\u5343",u"\u65b9",u"\u767e",u"\u8ba1"],["qian","fang","bai","ji"]],[[u"\u606f",u"\u606f",u"\u76f8",u"\u5173"],["xi","xi","xiang","guan"]],[[u"\u5c42",u"\u51fa",u"\u4e0d",u"\u7a77"],["ceng","chu","bu","qiong"]],[[u"\u5f15",u"\u4eba",u"\u6ce8",u"\u76ee"],["yin","ren","zhu","mu"]],[[u"\u5f53",u"\u52a1",u"\u4e4b",u"\u6025"],["dang","wu","zhi","ji"]],[[u"\u6df1",u"\u5165",u"\u4eba",u"\u5fc3"],["shen","ru","ren","xin"]],[[u"\u89c1",u"\u4e49",u"\u52c7",u"\u4e3a"],["jian","yi","yong","wei"]],[[u"\u540d",u"\u4e0d",u"\u865a",u"\u4f20"],["ming","bu","xu","chuan"]],[[u"\u6765",u"\u4e4b",u"\u4e0d",u"\u6613"],["lai","zhi","bu","yi"]],[[u"\u540d",u"\u526f",u"\u5176",u"\u5b9e"],["ming","fu","qi","shi"]],[[u"\u4e0b",u"\u843d",u"\u4e0d",u"\u660e"],["xia","luo","bu","ming"]],[[u"\u575a",u"\u6301",u"\u4e0d",u"\u61c8"],["jian","chi","bu","xie"]],[[u"\u6e90",u"\u6e90",u"\u4e0d",u"\u65ad"],["yuan","yuan","bu","duan"]],[[u"\u7edc",u"\u7ece",u"\u4e0d",u"\u7edd"],["luo","yi","bu","jue"]],[[u"\u5f04",u"\u865a",u"\u4f5c",u"\u5047"],["nong","xu","zuo","jia"]],[[u"\u4e0d",u"\u53ef",u"\u601d",u"\u8bae"],["bu","ke","si","yi"]],[[u"\u5c0f",u"\u5fc3",u"\u7ffc",u"\u7ffc"],["xiao","xin","yi","yi"]],[[u"\u957f",u"\u6cbb",u"\u4e45",u"\u5b89"],["chang","zhi","jiu","an"]],[[u"\u5982",u"\u706b",u"\u5982",u"\u837c"],["ru","huo","ru","tu"]],[[u"\u4e0d",u"\u6298",u"\u4e0d",u"\u6263"],["bu","zhe","bu","kou"]],[[u"\u540e",u"\u987e",u"\u4e4b",u"\u5fe7"],["hou","gu","zhi","you"]],[[u"\u7eb8",u"\u9189",u"\u91d1",u"\u8ff7"],["zhi","zui","jin","mi"]],[[u"\u529b",u"\u6240",u"\u80fd",u"\u53ca"],["li","suo","neng","ji"]],[[u"\u4f9b",u"\u4e0d",u"\u5e94",u"\u6c42"],["gong","bu","ying","qiu"]],[[u"\u4e00",u"\u76ee",u"\u4e86",u"\u7136"],["yi","mu","liao","ran"]],[[u"\u663e",u"\u800c",u"\u6613",u"\u89c1"],["xian","er","yi","jian"]],[[u"\u5b89",u"\u5c45",u"\u4e50",u"\u4e1a"],["an","ju","le","ye"]],[[u"\u9f50",u"\u5fc3",u"\u534f",u"\u529b"],["qi","xin","xie","li"]],[[u"\u5f97",u"\u5929",u"\u72ec",u"\u539a"],["de","tian","du","hou"]],[[u"\u4e00",u"\u89c1",u"\u949f",u"\u60c5"],["yi","jian","zhong","qing"]],[[u"\u72ec",u"\u4e00",u"\u65e0",u"\u4e8c"],["du","yi","wu","er"]],[[u"\u4e0d",u"\u7ea6",u"\u800c",u"\u540c"],["bu","yue","er","tong"]],[[u"\u7d27",u"\u9523",u"\u5bc6",u"\u9f13"],["jin","luo","mi","gu"]],[[u"\u4e94",u"\u82b1",u"\u516b",u"\u95e8"],["wu","hua","ba","men"]],[[u"\u4e00",u"\u5e94",u"\u4ff1",u"\u5168"],["yi","ying","ju","quan"]],[[u"\u5e94",u"\u8fd0",u"\u800c",u"\u751f"],["ying","yun","er","sheng"]],[[u"\u4e0e",u"\u4f17",u"\u4e0d",u"\u540c"],["yu","zhong","bu","tong"]],[[u"\u89e6",u"\u76ee",u"\u60ca",u"\u5fc3"],["chu","mu","jing","xin"]],[[u"\u5c61",u"\u89c1",u"\u4e0d",u"\u9c9c"],["lv","jian","bu","xian"]],[[u"\u65e0",u"\u72ec",u"\u6709",u"\u5076"],["wu","du","you","ou"]],[[u"\u884c",u"\u4e4b",u"\u6709",u"\u6548"],["xing","zhi","you","xiao"]],[[u"\u5927",u"\u52bf",u"\u6240",u"\u8d8b"],["da","shi","suo","qu"]],[[u"\u5fc3",u"\u6709",u"\u4f59",u"\u60b8"],["xin","you","yu","ji"]],[[u"\u4e0d",u"\u5f97",u"\u800c",u"\u77e5"],["bu","de","er","zhi"]],[[u"\u524d",u"\u6240",u"\u672a",u"\u6709"],["qian","suo","wei","you"]],[[u"\u8feb",u"\u4e0d",u"\u53ca",u"\u5f85"],["po","bu","ji","dai"]],[[u"\u96ea",u"\u4e0a",u"\u52a0",u"\u971c"],["xue","shang","jia","shuang"]],[[u"\u8feb",u"\u5728",u"\u7709",u"\u776b"],["po","zai","mei","jie"]],[[u"\u6b64",u"\u8d77",u"\u5f7c",u"\u4f0f"],["ci","qi","bi","fu"]],[[u"\u811a",u"\u8e0f",u"\u5b9e",u"\u5730"],["jiao","ta","shi","di"]],[[u"\u610f",u"\u60f3",u"\u4e0d",u"\u5230"],["yi","xiang","bu","dao"]],[[u"\u9519",u"\u7efc",u"\u590d",u"\u6742"],["cuo","zong","fu","za"]],[[u"\u65e0",u"\u53ef",u"\u539a",u"\u975e"],["wu","ke","hou","fei"]],[[u"\u6e90",u"\u8fdc",u"\u6d41",u"\u957f"],["yuan","yuan","liu","chang"]],[[u"\u4e3e",u"\u4e00",u"\u53cd",u"\u4e09"],["ju","yi","fan","san"]],[[u"\u5faa",u"\u5e8f",u"\u6e10",u"\u8fdb"],["xun","xu","jian","jin"]],[[u"\u4e0d",u"\u9057",u"\u4f59",u"\u529b"],["bu","yi","yu","li"]],[[u"\u4e0d",u"\u8a00",u"\u800c",u"\u55bb"],["bu","yan","er","yu"]],[[u"\u6df1",u"\u6076",u"\u75db",u"\u7edd"],["shen","wu","tong","jue"]],[[u"\u4e09",u"\u4f4d",u"\u4e00",u"\u4f53"],["san","wei","yi","ti"]],[[u"\u622a",u"\u7136",u"\u4e0d",u"\u540c"],["jie","ran","bu","tong"]],[[u"\u559c",u"\u95fb",u"\u4e50",u"\u89c1"],["xi","wen","le","jian"]],[[u"\u5bb6",u"\u55bb",u"\u6237",u"\u6653"],["jia","yu","hu","xiao"]],[[u"\u65e5",u"\u65b0",u"\u6708",u"\u5f02"],["ri","xin","yue","yi"]],[[u"\u53d6",u"\u800c",u"\u4ee3",u"\u4e4b"],["qu","er","dai","zhi"]],[[u"\u83ab",u"\u540d",u"\u5176",u"\u5999"],["mo","ming","qi","miao"]],[[u"\u540d",u"\u5217",u"\u524d",u"\u8305"],["ming","lie","qian","mao"]],[[u"\u6392",u"\u5fe7",u"\u89e3",u"\u96be"],["pai","you","jie","nan"]],[[u"\u73a9",u"\u5ffd",u"\u804c",u"\u5b88"],["wan","hu","zhi","shou"]],[[u"\u4efb",u"\u91cd",u"\u9053",u"\u8fdc"],["ren","zhong","dao","yuan"]],[[u"\u4e3e",u"\u8db3",u"\u8f7b",u"\u91cd"],["ju","zu","qing","zhong"]],[[u"\u6bd4",u"\u6bd4",u"\u7686",u"\u662f"],["bi","bi","jie","shi"]],[[u"\u5353",u"\u6709",u"\u6210",u"\u6548"],["zhuo","you","cheng","xiao"]],[[u"\u843d",u"\u5730",u"\u751f",u"\u6839"],["la","di","sheng","gen"]],[[u"\u52bf",u"\u5728",u"\u5fc5",u"\u884c"],["shi","zai","bi","xing"]],[[u"\u53f2",u"\u65e0",u"\u524d",u"\u4f8b"],["shi","wu","qian","li"]],[[u"\u7406",u"\u6240",u"\u5f53",u"\u7136"],["li","suo","dang","ran"]],[[u"\u8033",u"\u719f",u"\u80fd",u"\u8be6"],["er","shu","neng","xiang"]],[[u"\u94e4",u"\u800c",u"\u8d70",u"\u9669"],["ting","er","zou","xian"]],[[u"\u4e3e",u"\u4e16",u"\u77a9",u"\u76ee"],["ju","shi","zhu","mu"]],[[u"\u518d",u"\u63a5",u"\u518d",u"\u5389"],["zai","jie","zai","li"]],[[u"\u8db3",u"\u4e0d",u"\u51fa",u"\u6237"],["zu","bu","chu","hu"]],[[u"\u7ffb",u"\u5929",u"\u8986",u"\u5730"],["fan","tian","fu","di"]],[[u"\u4e0d",u"\u7ffc",u"\u800c",u"\u98de"],["bu","yi","er","fei"]],[[u"\u53c2",u"\u5dee",u"\u4e0d",u"\u9f50"],["can","ci","bu","qi"]],[[u"\u6c34",u"\u6da8",u"\u8239",u"\u9ad8"],["shui","zhang","chuan","gao"]],[[u"\u5148",u"\u53d1",u"\u5236",u"\u4eba"],["xian","fa","zhi","ren"]],[[u"\u8f69",u"\u7136",u"\u5927",u"\u6ce2"],["xuan","ran","da","bo"]],[[u"\u7edf",u"\u7b79",u"\u517c",u"\u987e"],["tong","chou","jian","gu"]],[[u"\u660e",u"\u5bdf",u"\u6697",u"\u8bbf"],["ming","cha","an","fang"]],[[u"\u523b",u"\u4e0d",u"\u5bb9",u"\u7f13"],["ke","bu","rong","huan"]],[[u"\u878d",u"\u4e3a",u"\u4e00",u"\u4f53"],["rong","wei","yi","ti"]],[[u"\u7115",u"\u7136",u"\u4e00",u"\u65b0"],["huan","ran","yi","xin"]],[[u"\u4ee5",u"\u8eab",u"\u4f5c",u"\u5219"],["yi","shen","zuo","ze"]],[[u"\u6f5c",u"\u79fb",u"\u9ed8",u"\u5316"],["qian","yi","mo","hua"]],[[u"\u98ce",u"\u53e3",u"\u6d6a",u"\u5c16"],["feng","kou","lang","jian"]],[[u"\u6709",u"\u6761",u"\u4e0d",u"\u7d0a"],["you","tiao","bu","wen"]],[[u"\u5f52",u"\u6839",u"\u7ed3",u"\u5e95"],["gui","gen","jie","di"]],[[u"\u53d1",u"\u626c",u"\u5149",u"\u5927"],["fa","yang","guang","da"]],[[u"\u65d7",u"\u5e1c",u"\u9c9c",u"\u660e"],["qi","zhi","xian","ming"]],[[u"\u4e07",u"\u65e0",u"\u4e00",u"\u5931"],["wan","wu","yi","shi"]],[[u"\u53ef",u"\u89c1",u"\u4e00",u"\u6591"],["ke","jian","yi","ban"]],[[u"\u4e00",u"\u89c6",u"\u540c",u"\u4ec1"],["yi","shi","tong","ren"]],[[u"\u76f8",u"\u8f85",u"\u76f8",u"\u6210"],["xiang","fu","xiang","cheng"]],[[u"\u6dcb",u"\u6f13",u"\u5c3d",u"\u81f4"],["lin","li","jin","zhi"]],[[u"\u8033",u"\u76ee",u"\u4e00",u"\u65b0"],["er","mu","yi","xin"]],[[u"\u4e0d",u"\u4e86",u"\u4e86",u"\u4e4b"],["bu","liao","liao","zhi"]],[[u"\u70ed",u"\u706b",u"\u671d",u"\u5929"],["re","huo","chao","tian"]],[[u"\u6709",u"\u76ee",u"\u5171",u"\u7779"],["you","mu","gong","du"]],[[u"\u4e45",u"\u800c",u"\u4e45",u"\u4e4b"],["jiu","er","jiu","zhi"]],[[u"\u89c6",u"\u800c",u"\u4e0d",u"\u89c1"],["shi","er","bu","jian"]],[[u"\u81ea",u"\u5f3a",u"\u4e0d",u"\u606f"],["zi","qiang","bu","xi"]],[[u"\u4ee5",u"\u6743",u"\u8c0b",u"\u79c1"],["yi","quan","mou","si"]],[[u"\u7ee7",u"\u5f80",u"\u5f00",u"\u6765"],["ji","wang","kai","lai"]],[[u"\u8d5e",u"\u4e0d",u"\u7edd",u"\u53e3"],["zan","bu","jue","kou"]],[[u"\u4e49",u"\u4e0d",u"\u5bb9",u"\u8f9e"],["yi","bu","rong","ci"]],[[u"\u672a",u"\u96e8",u"\u7ef8",u"\u7f2a"],["wei","yu","chou","mou"]],[[u"\u7ef3",u"\u4e4b",u"\u4ee5",u"\u6cd5"],["sheng","zhi","yi","fa"]],[[u"\u5bf9",u"\u75c7",u"\u4e0b",u"\u836f"],["dui","zheng","xia","yao"]],[[u"\u51fa",u"\u8c0b",u"\u5212",u"\u7b56"],["chu","mou","hua","ce"]],[[u"\u9996",u"\u5f53",u"\u5176",u"\u51b2"],["shou","dang","qi","chong"]],[[u"\u9a6c",u"\u4e0d",u"\u505c",u"\u8e44"],["ma","bu","ting","ti"]],[[u"\u4e0d",u"\u4ee5",u"\u4e3a",u"\u7136"],["bu","yi","wei","ran"]],[[u"\u4e00",u"\u8e74",u"\u800c",u"\u5c31"],["yi","cu","er","jiu"]],[[u"\u4eba",u"\u6ee1",u"\u4e3a",u"\u60a3"],["ren","man","wei","huan"]],[[u"\u8eab",u"\u4f53",u"\u529b",u"\u884c"],["shen","ti","li","xing"]],[[u"\u7cbe",u"\u76ca",u"\u6c42",u"\u7cbe"],["jing","yi","qiu","jing"]],[[u"\u7aed",u"\u5c3d",u"\u5168",u"\u529b"],["jie","jin","quan","li"]],[[u"\u62ed",u"\u76ee",u"\u4ee5",u"\u5f85"],["shi","mu","yi","dai"]],[[u"\u65e0",u"\u5bb6",u"\u53ef",u"\u5f52"],["wu","jia","ke","gui"]],[[u"\u54ed",u"\u7b11",u"\u4e0d",u"\u5f97"],["ku","xiao","bu","de"]],[[u"\u4e0d",u"\u77e5",u"\u6240",u"\u63aa"],["bu","zhi","suo","cuo"]],[[u"\u5ea7",u"\u65e0",u"\u865a",u"\u5e2d"],["zuo","wu","xu","xi"]],[[u"\u53ef",u"\u4e58",u"\u4e4b",u"\u673a"],["ke","cheng","zhi","ji"]],[[u"\u7433",u"\u7405",u"\u6ee1",u"\u76ee"],["lin","lang","man","mu"]],[[u"\u5377",u"\u571f",u"\u91cd",u"\u6765"],["juan","tu","chong","lai"]],[[u"\u94fa",u"\u5929",u"\u76d6",u"\u5730"],["pu","tian","gai","di"]],[[u"\u7406",u"\u76f4",u"\u6c14",u"\u58ee"],["li","zhi","qi","zhuang"]],[[u"\u9762",u"\u76ee",u"\u5168",u"\u975e"],["mian","mu","quan","fei"]],[[u"\u5fe7",u"\u5fc3",u"\u5fe1",u"\u5fe1"],["you","xin","chong","chong"]],[[u"\u5728",u"\u6240",u"\u96be",u"\u514d"],["zai","suo","nan","mian"]],[[u"\u71c3",u"\u7709",u"\u4e4b",u"\u6025"],["ran","mei","zhi","ji"]],[[u"\u56fe",u"\u6587",u"\u5e76",u"\u8302"],["tu","wen","bing","mao"]],[[u"\u4e0d",u"\u7edd",u"\u4e8e",u"\u8033"],["bu","jue","yu","er"]],[[u"\u6d25",u"\u6d25",u"\u4e50",u"\u9053"],["jin","jin","le","dao"]],[[u"\u7acb",u"\u7aff",u"\u89c1",u"\u5f71"],["li","gan","jian","ying"]],[[u"\u4e0e",u"\u65e5",u"\u4ff1",u"\u589e"],["yu","ri","ju","zeng"]],[[u"\u7cbe",u"\u5fc3",u"\u8bbe",u"\u8ba1"],["jing","xin","she","ji"]],[[u"\u6025",u"\u529f",u"\u8fd1",u"\u5229"],["ji","gong","jin","li"]],[[u"\u9c9c",u"\u4e3a",u"\u4eba",u"\u77e5"],["xian","wei","ren","zhi"]],[[u"\u6839",u"\u6df1",u"\u8482",u"\u56fa"],["gen","shen","di","gu"]],[[u"\u535a",u"\u5927",u"\u7cbe",u"\u6df1"],["bo","da","jing","shen"]],[[u"\u5927",u"\u6709",u"\u53ef",u"\u4e3a"],["da","you","ke","wei"]],[[u"\u60ca",u"\u5fc3",u"\u52a8",u"\u9b44"],["jing","xin","dong","po"]],[[u"\u4e0d",u"\u4ea6",u"\u4e50",u"\u4e4e"],["bu","yi","le","hu"]],[[u"\u76f8",u"\u5f97",u"\u76ca",u"\u5f70"],["xiang","de","yi","zhang"]],[[u"\u8010",u"\u4eba",u"\u5bfb",u"\u5473"],["nai","ren","xun","wei"]],[[u"\u522b",u"\u5f00",u"\u751f",u"\u9762"],["bie","kai","sheng","mian"]],[[u"\u6c34",u"\u6cc4",u"\u4e0d",u"\u901a"],["shui","xie","bu","tong"]],[[u"\u63a5",u"\u4e8c",u"\u8fde",u"\u4e09"],["jie","er","lian","san"]],[[u"\u65e0",u"\u80fd",u"\u4e3a",u"\u529b"],["wu","neng","wei","li"]],[[u"\u96be",u"\u4ee5",u"\u4e3a",u"\u7ee7"],["nan","yi","wei","ji"]],[[u"\u9677",u"\u5165",u"\u50f5",u"\u5c40"],["xian","ru","jiang","ju"]],[[u"\u611f",u"\u540c",u"\u8eab",u"\u53d7"],["gan","tong","shen","shou"]],[[u"\u532a",u"\u5937",u"\u6240",u"\u601d"],["fei","yi","suo","si"]],[[u"\u80cc",u"\u9053",u"\u800c",u"\u9a70"],["bei","dao","er","chi"]],[[u"\u96be",u"\u4ee5",u"\u7f6e",u"\u4fe1"],["nan","yi","zhi","xin"]],[[u"\u4e00",u"\u5e06",u"\u98ce",u"\u987a"],["yi","fan","feng","shun"]],[[u"\u6389",u"\u4ee5",u"\u8f7b",u"\u5fc3"],["diao","yi","qing","xin"]],[[u"\u7545",u"\u6240",u"\u6b32",u"\u8a00"],["chang","suo","yu","yan"]],[[u"\u4e60",u"\u4ee5",u"\u4e3a",u"\u5e38"],["xi","yi","wei","chang"]],[[u"\u6f0f",u"\u6d1e",u"\u767e",u"\u51fa"],["lou","dong","bai","chu"]],[[u"\u5e74",u"\u4e45",u"\u5931",u"\u4fee"],["nian","jiu","shi","xiu"]],[[u"\u4e00",u"\u8109",u"\u76f8",u"\u627f"],["yi","mai","xiang","cheng"]],[[u"\u5f53",u"\u4e4b",u"\u65e0",u"\u6127"],["dang","zhi","wu","kui"]],[[u"\u8086",u"\u65e0",u"\u5fcc",u"\u60ee"],["si","wu","ji","dan"]],[[u"\u5be5",u"\u5be5",u"\u65e0",u"\u51e0"],["liao","liao","wu","ji"]],[[u"\u987a",u"\u85e4",u"\u6478",u"\u74dc"],["shun","teng","mo","gua"]],[[u"\u52a9",u"\u4eba",u"\u4e3a",u"\u4e50"],["zhu","ren","wei","le"]],[[u"\u6b22",u"\u805a",u"\u4e00",u"\u5802"],["huan","ju","yi","tang"]],[[u"\u6cea",u"\u6d41",u"\u6ee1",u"\u9762"],["lei","liu","man","mian"]],[[u"\u63a5",u"\u8e35",u"\u800c",u"\u81f3"],["jie","zhong","er","zhi"]],[[u"\u76f4",u"\u8a00",u"\u4e0d",u"\u8bb3"],["zhi","yan","bu","hui"]],[[u"\u4e49",u"\u65e0",u"\u53cd",u"\u987e"],["yi","wu","fan","gu"]],[[u"\u529b",u"\u4e0d",u"\u4ece",u"\u5fc3"],["li","bu","cong","xin"]],[[u"\u6155",u"\u540d",u"\u800c",u"\u6765"],["mu","ming","er","lai"]],[[u"\u7eb7",u"\u81f3",u"\u6c93",u"\u6765"],["fen","zhi","ta","lai"]],[[u"\u5174",u"\u81f4",u"\u52c3",u"\u52c3"],["xing","zhi","bo","bo"]],[[u"\u5bb6",u"\u5e38",u"\u4fbf",u"\u996d"],["jia","chang","bian","fan"]],[[u"\u63aa",u"\u624b",u"\u4e0d",u"\u53ca"],["cuo","shou","bu","ji"]],[[u"\u5fc3",u"\u6025",u"\u5982",u"\u711a"],["xin","ji","ru","fen"]],[[u"\u4e00",u"\u5e2d",u"\u4e4b",u"\u5730"],["yi","xi","zhi","di"]],[[u"\u6829",u"\u6829",u"\u5982",u"\u751f"],["xu","xu","ru","sheng"]],[[u"\u773c",u"\u82b1",u"\u7f2d",u"\u4e71"],["yan","hua","liao","luan"]],[[u"\u96ea",u"\u4e2d",u"\u9001",u"\u70ad"],["xue","zhong","song","tan"]],[[u"\u5f97",u"\u4e0d",u"\u507f",u"\u5931"],["de","bu","chang","shi"]],[[u"\u5b89",u"\u7136",u"\u65e0",u"\u6059"],["an","ran","wu","yang"]],[[u"\u6df1",u"\u5165",u"\u6d45",u"\u51fa"],["shen","ru","qian","chu"]],[[u"\u6349",u"\u895f",u"\u89c1",u"\u8098"],["zhuo","jin","jian","zhou"]],[[u"\u62d2",u"\u4e4b",u"\u95e8",u"\u5916"],["ju","zhi","men","wai"]],[[u"\u671b",u"\u800c",u"\u5374",u"\u6b65"],["wang","er","que","bu"]],[[u"\u9ed8",u"\u9ed8",u"\u65e0",u"\u95fb"],["mo","mo","wu","wen"]],[[u"\u987a",u"\u7406",u"\u6210",u"\u7ae0"],["shun","li","cheng","zhang"]],[[u"\u96be",u"\u80fd",u"\u53ef",u"\u8d35"],["nan","neng","ke","gui"]],[[u"\u6765",u"\u9f99",u"\u53bb",u"\u8109"],["lai","long","qu","mai"]],[[u"\u4e0d",u"\u8c0b",u"\u800c",u"\u5408"],["bu","mou","er","he"]],[[u"\u5982",u"\u51fa",u"\u4e00",u"\u8f99"],["ru","chu","yi","zhe"]],[[u"\u63d0",u"\u5fc3",u"\u540a",u"\u80c6"],["ti","xin","diao","dan"]],[[u"\u5f87",u"\u79c1",u"\u821e",u"\u5f0a"],["xun","si","wu","bi"]],[[u"\u4e00",u"\u65e0",u"\u6240",u"\u77e5"],["yi","wu","suo","zhi"]],[[u"\u522b",u"\u6709",u"\u7528",u"\u5fc3"],["bie","you","yong","xin"]],[[u"\u5927",u"\u6253",u"\u51fa",u"\u624b"],["da","da","chu","shou"]],[[u"\u540c",u"\u821f",u"\u5171",u"\u6d4e"],["tong","zhou","gong","ji"]],[[u"\u96e8",u"\u540e",u"\u6625",u"\u7b0b"],["yu","hou","chun","sun"]],[[u"\u5162",u"\u5162",u"\u4e1a",u"\u4e1a"],["jing","jing","ye","ye"]],[[u"\u6ce3",u"\u4e0d",u"\u6210",u"\u58f0"],["qi","bu","cheng","sheng"]],[[u"\u65e0",u"\u4eba",u"\u95ee",u"\u6d25"],["wu","ren","wen","jin"]],[[u"\u5e94",u"\u6709",u"\u5c3d",u"\u6709"],["ying","you","jin","you"]],[[u"\u5f15",u"\u4ee5",u"\u4e3a",u"\u6212"],["yin","yi","wei","jie"]],[[u"\u5f02",u"\u519b",u"\u7a81",u"\u8d77"],["yi","jun","tu","qi"]],[[u"\u901a",u"\u4fd7",u"\u6613",u"\u61c2"],["tong","su","yi","dong"]],[[u"\u6ce2",u"\u6f9c",u"\u58ee",u"\u9614"],["bo","lan","zhuang","kuo"]],[[u"\u65e0",u"\u53ef",u"\u5948",u"\u4f55"],["wu","ke","nai","he"]],[[u"\u54c1",u"\u5b66",u"\u517c",u"\u4f18"],["pin","xue","jian","you"]],[[u"\u53f8",u"\u7a7a",u"\u89c1",u"\u60ef"],["si","kong","jian","guan"]],[[u"\u63a8",u"\u6ce2",u"\u52a9",u"\u6f9c"],["tui","bo","zhu","lan"]],[[u"\u5fae",u"\u4e4e",u"\u5176",u"\u5fae"],["wei","hu","qi","wei"]],[[u"\u76f8",u"\u63d0",u"\u5e76",u"\u8bba"],["xiang","ti","bing","lun"]],[[u"\u675f",u"\u624b",u"\u65e0",u"\u7b56"],["shu","shou","wu","ce"]],[[u"\u4fe1",u"\u4ee5",u"\u4e3a",u"\u771f"],["xin","yi","wei","zhen"]],[[u"\u6b7b",u"\u7070",u"\u590d",u"\u71c3"],["si","hui","fu","ran"]],[[u"\u82e6",u"\u4e0d",u"\u582a",u"\u8a00"],["ku","bu","kan","yan"]],[[u"\u4e89",u"\u5206",u"\u593a",u"\u79d2"],["zheng","fen","duo","miao"]],[[u"\u96c6",u"\u601d",u"\u5e7f",u"\u76ca"],["ji","si","guang","yi"]],[[u"\u81ea",u"\u529b",u"\u66f4",u"\u751f"],["zi","li","geng","sheng"]],[[u"\u6709",u"\u7684",u"\u653e",u"\u77e2"],["you","di","fang","shi"]],[[u"\u4e25",u"\u9635",u"\u4ee5",u"\u5f85"],["yan","zhen","yi","dai"]],[[u"\u5efa",u"\u529f",u"\u7acb",u"\u4e1a"],["jian","gong","li","ye"]],[[u"\u6e83",u"\u4e0d",u"\u6210",u"\u519b"],["kui","bu","cheng","jun"]],[[u"\u5e74",u"\u4e8b",u"\u5df2",u"\u9ad8"],["nian","shi","yi","gao"]],[[u"\u7eff",u"\u6c34",u"\u9752",u"\u5c71"],["lv","shui","qing","shan"]],[[u"\u534a",u"\u58c1",u"\u6c5f",u"\u5c71"],["ban","bi","jiang","shan"]],[[u"\u6c42",u"\u540c",u"\u5b58",u"\u5f02"],["qiu","tong","cun","yi"]],[[u"\u86db",u"\u4e1d",u"\u9a6c",u"\u8ff9"],["zhu","si","ma","ji"]],[[u"\u9c7c",u"\u9f99",u"\u6df7",u"\u6742"],["yu","long","hun","za"]],[[u"\u6251",u"\u6714",u"\u8ff7",u"\u79bb"],["pu","shuo","mi","li"]],[[u"\u7199",u"\u7199",u"\u6518",u"\u6518"],["xi","xi","rang","rang"]],[[u"\u4e00",u"\u6280",u"\u4e4b",u"\u957f"],["yi","ji","zhi","chang"]],[[u"\u5927",u"\u6c5f",u"\u5357",u"\u5317"],["da","jiang","nan","bei"]],[[u"\u5c48",u"\u6307",u"\u53ef",u"\u6570"],["qu","zhi","ke","shu"]],[[u"\u4ea4",u"\u76f8",u"\u8f89",u"\u6620"],["jiao","xiang","hui","ying"]],[[u"\u516c",u"\u4e4b",u"\u4e8e",u"\u4f17"],["gong","zhi","yu","zhong"]],[[u"\u4e00",u"\u62cd",u"\u5373",u"\u5408"],["yi","pai","ji","he"]],[[u"\u4e00",u"\u4e1d",u"\u4e0d",u"\u82df"],["yi","si","bu","gou"]],[[u"\u76f8",u"\u4f9d",u"\u4e3a",u"\u547d"],["xiang","yi","wei","ming"]],[[u"\u5fae",u"\u4e0d",u"\u8db3",u"\u9053"],["wei","bu","zu","dao"]],[[u"\u826f",u"\u83a0",u"\u4e0d",u"\u9f50"],["liang","you","bu","qi"]],[[u"\u8fce",u"\u5203",u"\u800c",u"\u89e3"],["ying","ren","er","jie"]],[[u"\u4ece",u"\u5929",u"\u800c",u"\u964d"],["cong","tian","er","jiang"]],[[u"\u4e0d",u"\u5408",u"\u65f6",u"\u5b9c"],["bu","he","shi","yi"]],[[u"\u53d7",u"\u76ca",u"\u532a",u"\u6d45"],["shou","yi","fei","qian"]],[[u"\u65b0",u"\u9648",u"\u4ee3",u"\u8c22"],["xin","chen","dai","xie"]],[[u"\u9ad8",u"\u9ad8",u"\u5728",u"\u4e0a"],["gao","gao","zai","shang"]],[[u"\u91cf",u"\u529b",u"\u800c",u"\u884c"],["liang","li","er","xing"]],[[u"\u4e0d",u"\u5207",u"\u5b9e",u"\u9645"],["bu","qie","shi","ji"]],[[u"\u9488",u"\u950b",u"\u76f8",u"\u5bf9"],["zhen","feng","xiang","dui"]],[[u"\u8d23",u"\u65e0",u"\u65c1",u"\u8d37"],["ze","wu","pang","dai"]],[[u"\u9ad8",u"\u77bb",u"\u8fdc",u"\u77a9"],["gao","zhan","yuan","zhu"]],[[u"\u660e",u"\u76ee",u"\u5f20",u"\u80c6"],["ming","mu","zhang","dan"]],[[u"\u9002",u"\u5f97",u"\u5176",u"\u53cd"],["shi","de","qi","fan"]],[[u"\u8dc3",u"\u8dc3",u"\u6b32",u"\u8bd5"],["yue","yue","yu","shi"]],[[u"\u805a",u"\u7cbe",u"\u4f1a",u"\u795e"],["ju","jing","hui","shen"]],[[u"\u627f",u"\u524d",u"\u542f",u"\u540e"],["cheng","qian","qi","hou"]],[[u"\u676f",u"\u6c34",u"\u8f66",u"\u85aa"],["bei","shui","che","xin"]],[[u"\u4e00",u"\u7f51",u"\u6253",u"\u5c3d"],["yi","wang","da","jin"]],[[u"\u6177",u"\u6168",u"\u89e3",u"\u56ca"],["kang","kai","jie","nang"]],[[u"\u7d20",u"\u4e0d",u"\u76f8",u"\u8bc6"],["su","bu","xiang","shi"]],[[u"\u957f",u"\u6b64",u"\u4ee5",u"\u5f80"],["chang","ci","yi","wang"]],[[u"\u683c",u"\u683c",u"\u4e0d",u"\u5165"],["ge","ge","bu","ru"]],[[u"\u851a",u"\u7136",u"\u6210",u"\u98ce"],["wei","ran","cheng","feng"]],[[u"\u751f",u"\u673a",u"\u52c3",u"\u52c3"],["sheng","ji","bo","bo"]],[[u"\u5927",u"\u76f8",u"\u5f84",u"\u5ead"],["da","xiang","jing","ting"]],[[u"\u5802",u"\u800c",u"\u7687",u"\u4e4b"],["tang","er","huang","zhi"]],[[u"\u5982",u"\u6570",u"\u5bb6",u"\u73cd"],["ru","shu","jia","zhen"]],[[u"\u66f4",u"\u65b0",u"\u6362",u"\u4ee3"],["geng","xin","huan","dai"]],[[u"\u4e89",u"\u5148",u"\u6050",u"\u540e"],["zheng","xian","kong","hou"]],[[u"\u6d53",u"\u58a8",u"\u91cd",u"\u5f69"],["nong","mo","zhong","cai"]],[[u"\u5927",u"\u5200",u"\u9614",u"\u65a7"],["da","dao","kuo","fu"]],[[u"\u60ca",u"\u614c",u"\u5931",u"\u63aa"],["jing","huang","shi","cuo"]],[[u"\u6240",u"\u5269",u"\u65e0",u"\u51e0"],["suo","sheng","wu","ji"]],[[u"\u9ad8",u"\u5b98",u"\u539a",u"\u7984"],["gao","guan","hou","lu"]],[[u"\u4e95",u"\u7136",u"\u6709",u"\u5e8f"],["jing","ran","you","xu"]],[[u"\u4e00",u"\u6ce2",u"\u4e09",u"\u6298"],["yi","bo","san","zhe"]],[[u"\u5f62",u"\u8ff9",u"\u53ef",u"\u7591"],["xing","ji","ke","yi"]],[[u"\u7099",u"\u624b",u"\u53ef",u"\u70ed"],["zhi","shou","ke","re"]],[[u"\u8eab",u"\u4e34",u"\u5176",u"\u5883"],["shen","lin","qi","jing"]],[[u"\u4e8c",u"\u8bdd",u"\u4e0d",u"\u8bf4"],["er","hua","bu","shuo"]],[[u"\u6d41",u"\u8fde",u"\u5fd8",u"\u8fd4"],["liu","lian","wang","fan"]],[[u"\u70ed",u"\u6cea",u"\u76c8",u"\u7736"],["re","lei","ying","kuang"]],[[u"\u9500",u"\u58f0",u"\u533f",u"\u8ff9"],["xiao","sheng","ni","ji"]],[[u"\u4e00",u"\u4ee5",u"\u8d2f",u"\u4e4b"],["yi","yi","guan","zhi"]],[[u"\u604d",u"\u7136",u"\u5927",u"\u609f"],["huang","ran","da","wu"]],[[u"\u7f6e",u"\u4e4b",u"\u4e0d",u"\u7406"],["zhi","zhi","bu","li"]],[[u"\u8f7b",u"\u800c",u"\u6613",u"\u4e3e"],["qing","er","yi","ju"]],[[u"\u4eba",u"\u6765",u"\u4eba",u"\u5f80"],["ren","lai","ren","wang"]],[[u"\u9752",u"\u5c71",u"\u7eff",u"\u6c34"],["qing","shan","lv","shui"]],[[u"\u9f50",u"\u5934",u"\u5e76",u"\u8fdb"],["qi","tou","bing","jin"]],[[u"\u4e00",u"\u7b79",u"\u83ab",u"\u5c55"],["yi","chou","mo","zhan"]],[[u"\u767e",u"\u82b1",u"\u9f50",u"\u653e"],["bai","hua","qi","fang"]],[[u"\u5404",u"\u6267",u"\u4e00",u"\u8bcd"],["ge","zhi","yi","ci"]],[[u"\u5fd7",u"\u540c",u"\u9053",u"\u5408"],["zhi","tong","dao","he"]],[[u"\u7ede",u"\u5c3d",u"\u8111",u"\u6c41"],["jiao","jin","nao","zhi"]],[[u"\u9996",u"\u5c48",u"\u4e00",u"\u6307"],["shou","qu","yi","zhi"]],[[u"\u6c34",u"\u5230",u"\u6e20",u"\u6210"],["shui","dao","qu","cheng"]],[[u"\u7269",u"\u7f8e",u"\u4ef7",u"\u5ec9"],["wu","mei","jia","lian"]],[[u"\u4f17",u"\u8bf4",u"\u7eb7",u"\u7ead"],["zhong","shuo","fen","yun"]],[[u"\u5404",u"\u81ea",u"\u4e3a",u"\u653f"],["ge","zi","wei","zheng"]],[[u"\u8bed",u"\u91cd",u"\u5fc3",u"\u957f"],["yu","zhong","xin","chang"]],[[u"\u5fb7",u"\u624d",u"\u517c",u"\u5907"],["de","cai","jian","bei"]],[[u"\u4e50",u"\u6b64",u"\u4e0d",u"\u75b2"],["le","ci","bu","pi"]],[[u"\u4e94",u"\u989c",u"\u516d",u"\u8272"],["wu","yan","liu","se"]],[[u"\u65e0",u"\u52a8",u"\u4e8e",u"\u8877"],["wu","dong","yu","zhong"]],[[u"\u9526",u"\u4e0a",u"\u6dfb",u"\u82b1"],["jin","shang","tian","hua"]],[[u"\u8352",u"\u6deb",u"\u65e0",u"\u5ea6"],["huang","yin","wu","du"]],[[u"\u63a8",u"\u9648",u"\u51fa",u"\u65b0"],["tui","chen","chu","xin"]],[[u"\u72ec",u"\u6811",u"\u4e00",u"\u5e1c"],["du","shu","yi","zhi"]],[[u"\u7701",u"\u5403",u"\u4fed",u"\u7528"],["sheng","chi","jian","yong"]],[[u"\u65e0",u"\u6d4e",u"\u4e8e",u"\u4e8b"],["wu","ji","yu","shi"]],[[u"\u60c5",u"\u4e0d",u"\u81ea",u"\u7981"],["qing","bu","zi","jin"]],[[u"\u4e0d",u"\u8db3",u"\u4e3a",u"\u5947"],["bu","zu","wei","qi"]],[[u"\u5fcd",u"\u65e0",u"\u53ef",u"\u5fcd"],["ren","wu","ke","ren"]],[[u"\u90c1",u"\u90c1",u"\u8471",u"\u8471"],["yu","yu","cong","cong"]],[[u"\u4e8b",u"\u534a",u"\u529f",u"\u500d"],["shi","ban","gong","bei"]],[[u"\u5206",u"\u95e8",u"\u522b",u"\u7c7b"],["fen","men","bie","lei"]],[[u"\u522b",u"\u51fa",u"\u5fc3",u"\u88c1"],["bie","chu","xin","cai"]],[[u"\u5927",u"\u5f20",u"\u65d7",u"\u9f13"],["da","zhang","qi","gu"]],[[u"\u9632",u"\u4e0d",u"\u80dc",u"\u9632"],["fang","bu","sheng","fang"]],[[u"\u60ca",u"\u9b42",u"\u672a",u"\u5b9a"],["jing","hun","wei","ding"]],[[u"\u8499",u"\u6df7",u"\u8fc7",u"\u5173"],["meng","hun","guo","guan"]],[[u"\u9519",u"\u843d",u"\u6709",u"\u81f4"],["cuo","luo","you","zhi"]],[[u"\u5165",u"\u4e0d",u"\u6577",u"\u51fa"],["ru","bu","fu","chu"]],[[u"\u6211",u"\u884c",u"\u6211",u"\u7d20"],["wo","xing","wo","su"]],[[u"\u6df1",u"\u601d",u"\u719f",u"\u8651"],["shen","si","shu","lv"]],[[u"\u8d8b",u"\u4e4b",u"\u82e5",u"\u9e5c"],["qu","zhi","ruo","wu"]],[[u"\u65e0",u"\u5fae",u"\u4e0d",u"\u81f3"],["wu","wei","bu","zhi"]],[[u"\u8f66",u"\u6c34",u"\u9a6c",u"\u9f99"],["che","shui","ma","long"]],[[u"\u65e0",u"\u6240",u"\u9002",u"\u4ece"],["wu","suo","shi","cong"]],[[u"\u53d8",u"\u672c",u"\u52a0",u"\u5389"],["bian","ben","jia","li"]],[[u"\u58ee",u"\u58eb",u"\u65ad",u"\u8155"],["zhuang","shi","duan","wan"]],[[u"\u96c4",u"\u5fc3",u"\u52c3",u"\u52c3"],["xiong","xin","bo","bo"]],[[u"\u5b66",u"\u4ee5",u"\u81f4",u"\u7528"],["xue","yi","zhi","yong"]],[[u"\u4e94",u"\u6e56",u"\u56db",u"\u6d77"],["wu","hu","si","hai"]],[[u"\u5ba1",u"\u65f6",u"\u5ea6",u"\u52bf"],["shen","shi","du","shi"]],[[u"\u4e0d",u"\u62e9",u"\u624b",u"\u6bb5"],["bu","ze","shou","duan"]],[[u"\u5927",u"\u8d77",u"\u5927",u"\u843d"],["da","qi","da","luo"]],[[u"\u4e0d",u"\u538c",u"\u5176",u"\u70e6"],["bu","yan","qi","fan"]],[[u"\u56db",u"\u901a",u"\u516b",u"\u8fbe"],["si","tong","ba","da"]],[[u"\u4e0d",u"\u53ef",u"\u5f00",u"\u4ea4"],["bu","ke","kai","jiao"]],[[u"\u6625",u"\u6696",u"\u82b1",u"\u5f00"],["chun","nuan","hua","kai"]],[[u"\u5929",u"\u7ecf",u"\u5730",u"\u4e49"],["tian","jing","di","yi"]],[[u"\u60ac",u"\u800c",u"\u672a",u"\u51b3"],["xuan","er","wei","jue"]],[[u"\u4e00",u"\u8a00",u"\u4e0d",u"\u53d1"],["yi","yan","bu","fa"]],[[u"\u8702",u"\u62e5",u"\u800c",u"\u81f3"],["feng","yong","er","zhi"]],[[u"\u626c",u"\u957f",u"\u800c",u"\u53bb"],["yang","chang","er","qu"]],[[u"\u6c34",u"\u843d",u"\u77f3",u"\u51fa"],["shui","luo","shi","chu"]],[[u"\u5927",u"\u5f00",u"\u773c",u"\u754c"],["da","kai","yan","jie"]],[[u"\u8f7d",u"\u6b4c",u"\u8f7d",u"\u821e"],["zai","ge","zai","wu"]],[[u"\u5b50",u"\u865a",u"\u4e4c",u"\u6709"],["zi","xu","wu","you"]],[[u"\u4e86",u"\u5982",u"\u6307",u"\u638c"],["liao","ru","zhi","zhang"]],[[u"\u5386",u"\u5386",u"\u5728",u"\u76ee"],["li","li","zai","mu"]],[[u"\u5f87",u"\u79c1",u"\u6789",u"\u6cd5"],["xun","si","wang","fa"]],[[u"\u98ce",u"\u4e91",u"\u53d8",u"\u5e7b"],["feng","yun","bian","huan"]],[[u"\u516c",u"\u6b63",u"\u5ec9",u"\u6d01"],["gong","zheng","lian","jie"]],[[u"\u5343",u"\u4e1d",u"\u4e07",u"\u7f15"],["qian","si","wan","lv"]],[[u"\u594b",u"\u4e0d",u"\u987e",u"\u8eab"],["fen","bu","gu","shen"]],[[u"\u8f7b",u"\u63cf",u"\u6de1",u"\u5199"],["qing","miao","dan","xie"]],[[u"\u4e0d",u"\u89e3",u"\u4e4b",u"\u7f18"],["bu","jie","zhi","yuan"]],[[u"\u987e",u"\u540d",u"\u601d",u"\u4e49"],["gu","ming","si","yi"]],[[u"\u6709",u"\u58f0",u"\u6709",u"\u8272"],["you","sheng","you","se"]],[[u"\u6d41",u"\u79bb",u"\u5931",u"\u6240"],["liu","li","shi","suo"]],[[u"\u8bf8",u"\u5982",u"\u6b64",u"\u7c7b"],["zhu","ru","ci","lei"]],[[u"\u4e00",u"\u6e05",u"\u4e8c",u"\u695a"],["yi","qing","er","chu"]],[[u"\u4f17",u"\u5fd7",u"\u6210",u"\u57ce"],["zhong","zhi","cheng","cheng"]],[[u"\u6551",u"\u6b7b",u"\u6276",u"\u4f24"],["jiu","si","fu","shang"]],[[u"\u68a6",u"\u5bd0",u"\u4ee5",u"\u6c42"],["meng","mei","yi","qiu"]],[[u"\u900d",u"\u9065",u"\u6cd5",u"\u5916"],["xiao","yao","fa","wai"]],[[u"\u4fe1",u"\u8a93",u"\u65e6",u"\u65e6"],["xin","shi","dan","dan"]],[[u"\u4e0d",u"\u8ba1",u"\u5176",u"\u6570"],["bu","ji","qi","shu"]],[[u"\u7f3a",u"\u4e00",u"\u4e0d",u"\u53ef"],["que","yi","bu","ke"]],[[u"\u8131",u"\u80ce",u"\u6362",u"\u9aa8"],["tuo","tai","huan","gu"]],[[u"\u771f",u"\u5fc3",u"\u5b9e",u"\u610f"],["zhen","xin","shi","yi"]],[[u"\u5bf9",u"\u7c3f",u"\u516c",u"\u5802"],["dui","bu","gong","tang"]],[[u"\u4e0d",u"\u8fb1",u"\u4f7f",u"\u547d"],["bu","ru","shi","ming"]],[[u"\u72c2",u"\u98ce",u"\u66b4",u"\u96e8"],["kuang","feng","bao","yu"]],[[u"\u65e5",u"\u590d",u"\u4e00",u"\u65e5"],["ri","fu","yi","ri"]],[[u"\u767d",u"\u53d1",u"\u82cd",u"\u82cd"],["bai","fa","cang","cang"]],[[u"\u5c71",u"\u6e05",u"\u6c34",u"\u79c0"],["shan","qing","shui","xiu"]],[[u"\u968f",u"\u5fc3",u"\u6240",u"\u6b32"],["sui","xin","suo","yu"]],[[u"\u4e0d",u"\u582a",u"\u8bbe",u"\u60f3"],["bu","kan","she","xiang"]],[[u"\u53f9",u"\u4e3a",u"\u89c2",u"\u6b62"],["tan","wei","guan","zhi"]],[[u"\u4e0d",u"\u7531",u"\u81ea",u"\u4e3b"],["bu","you","zi","zhu"]],[[u"\u5982",u"\u613f",u"\u4ee5",u"\u507f"],["ru","yuan","yi","chang"]],[[u"\u53d6",u"\u957f",u"\u8865",u"\u77ed"],["qu","chang","bu","duan"]],[[u"\u8fd1",u"\u5728",u"\u54ab",u"\u5c3a"],["jin","zai","zhi","chi"]],[[u"\u60e8",u"\u4e0d",u"\u5fcd",u"\u7779"],["can","bu","ren","du"]],[[u"\u4e00",u"\u65e0",u"\u6240",u"\u83b7"],["yi","wu","suo","huo"]],[[u"\u547c",u"\u4e4b",u"\u6b32",u"\u51fa"],["hu","zhi","yu","chu"]],[[u"\u4e00",u"\u53a2",u"\u60c5",u"\u613f"],["yi","xiang","qing","yuan"]],[[u"\u65e0",u"\u4e0e",u"\u4f26",u"\u6bd4"],["wu","yu","lun","bi"]],[[u"\u65e0",u"\u4e2d",u"\u751f",u"\u6709"],["wu","zhong","sheng","you"]],[[u"\u8f70",u"\u52a8",u"\u4e00",u"\u65f6"],["hong","dong","yi","shi"]],[[u"\u8857",u"\u5934",u"\u5df7",u"\u5c3e"],["jie","tou","xiang","wei"]],[[u"\u63b7",u"\u5730",u"\u6709",u"\u58f0"],["zhi","di","you","sheng"]],[[u"\u621b",u"\u7136",u"\u800c",u"\u6b62"],["jia","ran","er","zhi"]],[[u"\u5ff5",u"\u5ff5",u"\u4e0d",u"\u5fd8"],["nian","nian","bu","wang"]],[[u"\u5077",u"\u5de5",u"\u51cf",u"\u6599"],["tou","gong","jian","liao"]],[[u"\u6d25",u"\u6d25",u"\u6709",u"\u5473"],["jin","jin","you","wei"]],[[u"\u6539",u"\u5934",u"\u6362",u"\u9762"],["gai","tou","huan","mian"]],[[u"\u636e",u"\u4e3a",u"\u5df1",u"\u6709"],["ju","wei","ji","you"]],[[u"\u5927",u"\u540c",u"\u5c0f",u"\u5f02"],["da","tong","xiao","yi"]],[[u"\u522e",u"\u76ee",u"\u76f8",u"\u770b"],["gua","mu","xiang","kan"]],[[u"\u4ee4",u"\u4eba",u"\u53d1",u"\u6307"],["ling","ren","fa","zhi"]],[[u"\u76ee",u"\u77aa",u"\u53e3",u"\u5446"],["mu","deng","kou","dai"]],[[u"\u96f7",u"\u5389",u"\u98ce",u"\u884c"],["lei","li","feng","xing"]],[[u"\u98ce",u"\u96e8",u"\u65e0",u"\u963b"],["feng","yu","wu","zu"]],[[u"\u6c5f",u"\u90ce",u"\u624d",u"\u5c3d"],["jiang","lang","cai","jin"]],[[u"\u7f8e",u"\u8f6e",u"\u7f8e",u"\u5942"],["mei","lun","mei","huan"]],[[u"\u8d27",u"\u771f",u"\u4ef7",u"\u5b9e"],["huo","zhen","jia","shi"]],[[u"\u4e09",u"\u4ee4",u"\u4e94",u"\u7533"],["san","ling","wu","shen"]],[[u"\u611f",u"\u6168",u"\u4e07",u"\u5343"],["gan","kai","wan","qian"]],[[u"\u62fe",u"\u91d1",u"\u4e0d",u"\u6627"],["shi","jin","bu","mei"]],[[u"\u56e0",u"\u4eba",u"\u800c",u"\u5f02"],["yin","ren","er","yi"]],[[u"\u4e00",u"\u7eb8",u"\u7a7a",u"\u6587"],["yi","zhi","kong","wen"]],[[u"\u53cc",u"\u7ba1",u"\u9f50",u"\u4e0b"],["shuang","guan","qi","xia"]],[[u"\u8131",u"\u53e3",u"\u800c",u"\u51fa"],["tuo","kou","er","chu"]],[[u"\u66fe",u"\u51e0",u"\u4f55",u"\u65f6"],["ceng","ji","he","shi"]],[[u"\u9003",u"\u4e4b",u"\u592d",u"\u592d"],["tao","zhi","yao","yao"]],[[u"\u5fc3",u"\u7518",u"\u60c5",u"\u613f"],["xin","gan","qing","yuan"]],[[u"\u4e00",u"\u671d",u"\u4e00",u"\u5915"],["yi","zhao","yi","xi"]],[[u"\u503e",u"\u5bb6",u"\u8361",u"\u4ea7"],["qing","jia","dang","chan"]],[[u"\u6709",u"\u5229",u"\u53ef",u"\u56fe"],["you","li","ke","tu"]],[[u"\u4e07",u"\u4f17",u"\u4e00",u"\u5fc3"],["wan","zhong","yi","xin"]],[[u"\u53e4",u"\u8272",u"\u53e4",u"\u9999"],["gu","se","gu","xiang"]],[[u"\u523b",u"\u9aa8",u"\u94ed",u"\u5fc3"],["ke","gu","ming","xin"]],[[u"\u4e1c",u"\u7a97",u"\u4e8b",u"\u53d1"],["dong","chuang","shi","fa"]],[[u"\u5f00",u"\u95e8",u"\u89c1",u"\u5c71"],["kai","men","jian","shan"]],[[u"\u84b8",u"\u84b8",u"\u65e5",u"\u4e0a"],["zheng","zheng","ri","shang"]],[[u"\u8270",u"\u82e6",u"\u5353",u"\u7edd"],["jian","ku","zhuo","jue"]],[[u"\u627f",u"\u4e0a",u"\u542f",u"\u4e0b"],["cheng","shang","qi","xia"]],[[u"\u98ce",u"\u8d77",u"\u4e91",u"\u6d8c"],["feng","qi","yun","yong"]],[[u"\u4e71",u"\u4e03",u"\u516b",u"\u7cdf"],["luan","qi","ba","zao"]],[[u"\u6d51",u"\u8eab",u"\u89e3",u"\u6570"],["hun","shen","xie","shu"]],[[u"\u4e00",u"\u610f",u"\u5b64",u"\u884c"],["yi","yi","gu","xing"]],[[u"\u5e74",u"\u590d",u"\u4e00",u"\u5e74"],["nian","fu","yi","nian"]],[[u"\u6c34",u"\u571f",u"\u4e0d",u"\u670d"],["shui","tu","bu","fu"]],[[u"\u7edd",u"\u65e0",u"\u4ec5",u"\u6709"],["jue","wu","jin","you"]],[[u"\u5944",u"\u5944",u"\u4e00",u"\u606f"],["yan","yan","yi","xi"]],[[u"\u751f",u"\u751f",u"\u4e0d",u"\u606f"],["sheng","sheng","bu","xi"]],[[u"\u8feb",u"\u4e0d",u"\u5f97",u"\u5df2"],["po","bu","de","yi"]],[[u"\u72ec",u"\u5584",u"\u5176",u"\u8eab"],["du","shan","qi","shen"]],[[u"\u6070",u"\u5230",u"\u597d",u"\u5904"],["qia","dao","hao","chu"]],[[u"\u4e00",u"\u89e6",u"\u5373",u"\u53d1"],["yi","chu","ji","fa"]],[[u"\u8bf4",u"\u4e09",u"\u9053",u"\u56db"],["shuo","san","dao","si"]],[[u"\u4e0d",u"\u80dc",u"\u679a",u"\u4e3e"],["bu","sheng","mei","ju"]],[[u"\u5404",u"\u6292",u"\u5df1",u"\u89c1"],["ge","shu","ji","jian"]],[[u"\u610f",u"\u5473",u"\u6df1",u"\u957f"],["yi","wei","shen","chang"]],[[u"\u751f",u"\u6b7b",u"\u5b58",u"\u4ea1"],["sheng","si","cun","wang"]],[[u"\u8822",u"\u8822",u"\u6b32",u"\u52a8"],["chun","chun","yu","dong"]],[[u"\u6447",u"\u6447",u"\u6b32",u"\u5760"],["yao","yao","yu","zhui"]],[[u"\u4e16",u"\u5916",u"\u6843",u"\u6e90"],["shi","wai","tao","yuan"]],[[u"\u6ed4",u"\u6ed4",u"\u4e0d",u"\u7edd"],["tao","tao","bu","jue"]],[[u"\u6b23",u"\u6b23",u"\u5411",u"\u8363"],["xin","xin","xiang","rong"]],[[u"\u6dfb",u"\u7816",u"\u52a0",u"\u74e6"],["tian","zhuan","jia","wa"]],[[u"\u6765",u"\u52bf",u"\u6c79",u"\u6c79"],["lai","shi","xiong","xiong"]],[[u"\u6709",u"\u671d",u"\u4e00",u"\u65e5"],["you","zhao","yi","ri"]],[[u"\u7591",u"\u96be",u"\u6742",u"\u75c7"],["yi","nan","za","zheng"]],[[u"\u6307",u"\u65e5",u"\u53ef",u"\u5f85"],["zhi","ri","ke","dai"]],[[u"\u6bcf",u"\u51b5",u"\u6108",u"\u4e0b"],["mei","kuang","yu","xia"]],[[u"\u7cbe",u"\u6253",u"\u7ec6",u"\u7b97"],["jing","da","xi","suan"]],[[u"\u771f",u"\u77e5",u"\u707c",u"\u89c1"],["zhen","zhi","zhuo","jian"]],[[u"\u9065",u"\u9065",u"\u65e0",u"\u671f"],["yao","yao","wu","qi"]],[[u"\u4ee3",u"\u4ee3",u"\u76f8",u"\u4f20"],["dai","dai","xiang","chuan"]],[[u"\u52c7",u"\u5f80",u"\u76f4",u"\u524d"],["yong","wang","zhi","qian"]],[[u"\u597d",u"\u666f",u"\u4e0d",u"\u957f"],["hao","jing","bu","chang"]],[[u"\u53e6",u"\u8f9f",u"\u8e4a",u"\u5f84"],["ling","pi","xi","jing"]],[[u"\u671d",u"\u6c14",u"\u84ec",u"\u52c3"],["zhao","qi","peng","bo"]],[[u"\u89c1",u"\u602a",u"\u4e0d",u"\u602a"],["jian","guai","bu","guai"]],[[u"\u4e00",u"\u52b3",u"\u6c38",u"\u9038"],["yi","lao","yong","yi"]],[[u"\u76ee",u"\u4e0d",u"\u6687",u"\u63a5"],["mu","bu","xia","jie"]],[[u"\u810d",u"\u7099",u"\u4eba",u"\u53e3"],["kuai","zhi","ren","kou"]],[[u"\u65e0",u"\u6240",u"\u4e8b",u"\u4e8b"],["wu","suo","shi","shi"]],[[u"\u751a",u"\u56a3",u"\u5c18",u"\u4e0a"],["shen","xiao","chen","shang"]],[[u"\u65f6",u"\u4e0d",u"\u6211",u"\u5f85"],["shi","bu","wo","dai"]],[[u"\u6253",u"\u6210",u"\u4e00",u"\u7247"],["da","cheng","yi","pian"]],[[u"\u4e00",u"\u6210",u"\u4e0d",u"\u53d8"],["yi","cheng","bu","bian"]],[[u"\u6000",u"\u6068",u"\u5728",u"\u5fc3"],["huai","hen","zai","xin"]],[[u"\u603b",u"\u800c",u"\u8a00",u"\u4e4b"],["zong","er","yan","zhi"]],[[u"\u8270",u"\u82e6",u"\u521b",u"\u4e1a"],["jian","ku","chuang","ye"]],[[u"\u4e0d",u"\u52a1",u"\u6b63",u"\u4e1a"],["bu","wu","zheng","ye"]],[[u"\u8eab",u"\u65e0",u"\u5206",u"\u6587"],["shen","wu","fen","wen"]],[[u"\u522b",u"\u5177",u"\u4e00",u"\u683c"],["bie","ju","yi","ge"]],[[u"\u6cbb",u"\u75c5",u"\u6551",u"\u4eba"],["zhi","bing","jiu","ren"]],[[u"\u5c8c",u"\u5c8c",u"\u53ef",u"\u5371"],["ji","ji","ke","wei"]],[[u"\u4e30",u"\u529f",u"\u4f1f",u"\u7ee9"],["feng","gong","wei","ji"]],[[u"\u4ed6",u"\u5c71",u"\u4e4b",u"\u77f3"],["ta","shan","zhi","shi"]],[[u"\u907f",u"\u91cd",u"\u5c31",u"\u8f7b"],["bi","zhong","jiu","qing"]],[[u"\u6309",u"\u90e8",u"\u5c31",u"\u73ed"],["an","bu","jiu","ban"]],[[u"\u6025",u"\u8f6c",u"\u76f4",u"\u4e0b"],["ji","zhuan","zhi","xia"]],[[u"\u4e00",u"\u4e3e",u"\u4e24",u"\u5f97"],["yi","ju","liang","de"]],[[u"\u5174",u"\u9ad8",u"\u91c7",u"\u70c8"],["xing","gao","cai","lie"]],[[u"\u540c",u"\u5fc3",u"\u534f",u"\u529b"],["tong","xin","xie","li"]],[[u"\u4f83",u"\u4f83",u"\u800c",u"\u8c08"],["kan","kan","er","tan"]],[[u"\u607c",u"\u7f9e",u"\u6210",u"\u6012"],["nao","xiu","cheng","nu"]],[[u"\u5929",u"\u58e4",u"\u4e4b",u"\u522b"],["tian","rang","zhi","bie"]],[[u"\u5484",u"\u5484",u"\u903c",u"\u4eba"],["duo","duo","bi","ren"]],[[u"\u5343",u"\u7bc7",u"\u4e00",u"\u5f8b"],["qian","pian","yi","lv"]],[[u"\u5bf8",u"\u6b65",u"\u96be",u"\u884c"],["cun","bu","nan","xing"]],[[u"\u5618",u"\u5bd2",u"\u95ee",u"\u6696"],["xu","han","wen","nuan"]],[[u"\u4e0d",u"\u5931",u"\u65f6",u"\u673a"],["bu","shi","shi","ji"]],[[u"\u76f4",u"\u622a",u"\u4e86",u"\u5f53"],["zhi","jie","liao","dang"]],[[u"\u767d",u"\u624b",u"\u8d77",u"\u5bb6"],["bai","shou","qi","jia"]],[[u"\u4eba",u"\u53bb",u"\u697c",u"\u7a7a"],["ren","qu","lou","kong"]],[[u"\u7f6e",u"\u82e5",u"\u7f54",u"\u95fb"],["zhi","ruo","wang","wen"]],[[u"\u77a0",u"\u76ee",u"\u7ed3",u"\u820c"],["cheng","mu","jie","she"]],[[u"\u957f",u"\u9014",u"\u8dcb",u"\u6d89"],["chang","tu","ba","she"]],[[u"\u7fa4",u"\u7b56",u"\u7fa4",u"\u529b"],["qun","ce","qun","li"]],[[u"\u524d",u"\u8f66",u"\u4e4b",u"\u9274"],["qian","che","zhi","jian"]],[[u"\u4e00",u"\u62e5",u"\u800c",u"\u4e0a"],["yi","yong","er","shang"]],[[u"\u6bcb",u"\u5eb8",u"\u8bb3",u"\u8a00"],["wu","yong","hui","yan"]],[[u"\u8fdd",u"\u6cd5",u"\u4e71",u"\u7eaa"],["wei","fa","luan","ji"]],[[u"\u75db",u"\u5b9a",u"\u601d",u"\u75db"],["tong","ding","si","tong"]],[[u"\u96be",u"\u4e0a",u"\u52a0",u"\u96be"],["nan","shang","jia","nan"]],[[u"\u5e76",u"\u80a9",u"\u4f5c",u"\u6218"],["bing","jian","zuo","zhan"]],[[u"\u59cb",u"\u7ec8",u"\u5982",u"\u4e00"],["shi","zhong","ru","yi"]],[[u"\u6570",u"\u4e0d",u"\u80dc",u"\u6570"],["shu","bu","sheng","shu"]],[[u"\u557c",u"\u7b11",u"\u7686",u"\u975e"],["ti","xiao","jie","fei"]],[[u"\u4e0d",u"\u95fb",u"\u4e0d",u"\u95ee"],["bu","wen","bu","wen"]],[[u"\u4e0d",u"\u76f8",u"\u4e0a",u"\u4e0b"],["bu","xiang","shang","xia"]],[[u"\u81ea",u"\u7ed9",u"\u81ea",u"\u8db3"],["zi","ji","zi","zu"]],[[u"\u6709",u"\u751f",u"\u4e4b",u"\u5e74"],["you","sheng","zhi","nian"]],[[u"\u6253",u"\u8349",u"\u60ca",u"\u86c7"],["da","cao","jing","she"]],[[u"\u9f13",u"\u821e",u"\u4eba",u"\u5fc3"],["gu","wu","ren","xin"]],[[u"\u4e09",u"\u4e94",u"\u6210",u"\u7fa4"],["san","wu","cheng","qun"]],[[u"\u94ff",u"\u9535",u"\u6709",u"\u529b"],["keng","qiang","you","li"]],[[u"\u8d4f",u"\u5fc3",u"\u60a6",u"\u76ee"],["shang","xin","yue","mu"]],[[u"\u591c",u"\u4ee5",u"\u7ee7",u"\u65e5"],["ye","yi","ji","ri"]],[[u"\u8d77",u"\u65e9",u"\u8d2a",u"\u9ed1"],["qi","zao","tan","hei"]],[[u"\u7231",u"\u4e0d",u"\u91ca",u"\u624b"],["ai","bu","shi","shou"]],[[u"\u624b",u"\u8db3",u"\u65e0",u"\u63aa"],["shou","zu","wu","cuo"]],[[u"\u4e00",u"\u5206",u"\u4e3a",u"\u4e8c"],["yi","fen","wei","er"]],[[u"\u4e0d",u"\u53ef",u"\u591a",u"\u5f97"],["bu","ke","duo","de"]],[[u"\u559c",u"\u51fa",u"\u671b",u"\u5916"],["xi","chu","wang","wai"]],[[u"\u53e3",u"\u53e3",u"\u76f8",u"\u4f20"],["kou","kou","xiang","chuan"]],[[u"\u53ea",u"\u4e89",u"\u671d",u"\u5915"],["zhi","zheng","zhao","xi"]],[[u"\u6c14",u"\u5598",u"\u5401",u"\u5401"],["qi","chuan","xu","xu"]],[[u"\u731d",u"\u4e0d",u"\u53ca",u"\u9632"],["cu","bu","ji","fang"]],[[u"\u4e0d",u"\u7518",u"\u793a",u"\u5f31"],["bu","gan","shi","ruo"]],[[u"\u4ea1",u"\u7f8a",u"\u8865",u"\u7262"],["wang","yang","bu","lao"]],[[u"\u610f",u"\u6c14",u"\u98ce",u"\u53d1"],["yi","qi","feng","fa"]],[[u"\u6469",u"\u62f3",u"\u64e6",u"\u638c"],["mo","quan","ca","zhang"]],[[u"\u559c",u"\u6012",u"\u54c0",u"\u4e50"],["xi","nu","ai","le"]],[[u"\u60df",u"\u5999",u"\u60df",u"\u8096"],["wei","miao","wei","xiao"]],[[u"\u81ea",u"\u76f8",u"\u77db",u"\u76fe"],["zi","xiang","mao","dun"]],[[u"\u4e2d",u"\u6d41",u"\u7825",u"\u67f1"],["zhong","liu","di","zhu"]],[[u"\u771f",u"\u76f8",u"\u5927",u"\u767d"],["zhen","xiang","da","bai"]],[[u"\u65e9",u"\u51fa",u"\u665a",u"\u5f52"],["zao","chu","wan","gui"]],[[u"\u7e41",u"\u8363",u"\u660c",u"\u76db"],["fan","rong","chang","sheng"]],[[u"\u5f02",u"\u53e3",u"\u540c",u"\u58f0"],["yi","kou","tong","sheng"]],[[u"\u559c",u"\u6c14",u"\u6d0b",u"\u6d0b"],["xi","qi","yang","yang"]],[[u"\u5927",u"\u662f",u"\u5927",u"\u975e"],["da","shi","da","fei"]],[[u"\u81ea",u"\u98df",u"\u5176",u"\u529b"],["zi","shi","qi","li"]],[[u"\u8a00",u"\u4f20",u"\u8eab",u"\u6559"],["yan","chuan","shen","jiao"]],[[u"\u6d74",u"\u8840",u"\u594b",u"\u6218"],["yu","xue","fen","zhan"]],[[u"\u5927",u"\u60ca",u"\u5c0f",u"\u602a"],["da","jing","xiao","guai"]],[[u"\u8f6c",u"\u5371",u"\u4e3a",u"\u5b89"],["zhuan","wei","wei","an"]],[[u"\u89c1",u"\u7f1d",u"\u63d2",u"\u9488"],["jian","feng","cha","zhen"]],[[u"\u5e73",u"\u6613",u"\u8fd1",u"\u4eba"],["ping","yi","jin","ren"]],[[u"\u53e4",u"\u4eca",u"\u4e2d",u"\u5916"],["gu","jin","zhong","wai"]],[[u"\u6028",u"\u58f0",u"\u8f7d",u"\u9053"],["yuan","sheng","zai","dao"]],[[u"\u4eba",u"\u58f0",u"\u9f0e",u"\u6cb8"],["ren","sheng","ding","fei"]],[[u"\u5343",u"\u91cc",u"\u8fe2",u"\u8fe2"],["qian","li","tiao","tiao"]],[[u"\u878d",u"\u4f1a",u"\u8d2f",u"\u901a"],["rong","hui","guan","tong"]],[[u"\u6574",u"\u88c5",u"\u5f85",u"\u53d1"],["zheng","zhuang","dai","fa"]],[[u"\u5f97",u"\u5fc3",u"\u5e94",u"\u624b"],["de","xin","ying","shou"]],[[u"\u6c38",u"\u65e0",u"\u6b62",u"\u5883"],["yong","wu","zhi","jing"]],[[u"\u72b9",u"\u8c6b",u"\u4e0d",u"\u51b3"],["you","yu","bu","jue"]],[[u"\u706b",u"\u773c",u"\u91d1",u"\u775b"],["huo","yan","jin","jing"]],[[u"\u8896",u"\u624b",u"\u65c1",u"\u89c2"],["xiu","shou","pang","guan"]],[[u"\u82e6",u"\u53e3",u"\u5a46",u"\u5fc3"],["ku","kou","po","xin"]],[[u"\u6e38",u"\u5203",u"\u6709",u"\u4f59"],["you","ren","you","yu"]],[[u"\u59cb",u"\u7ec8",u"\u4e0d",u"\u6e1d"],["shi","zhong","bu","yu"]],[[u"\u803f",u"\u803f",u"\u4e8e",u"\u6000"],["geng","geng","yu","huai"]],[[u"\u6cb9",u"\u7136",u"\u800c",u"\u751f"],["you","ran","er","sheng"]],[[u"\u5bb3",u"\u7fa4",u"\u4e4b",u"\u9a6c"],["hai","qun","zhi","ma"]],[[u"\u6743",u"\u5b9c",u"\u4e4b",u"\u8ba1"],["quan","yi","zhi","ji"]],[[u"\u80cc",u"\u4e95",u"\u79bb",u"\u4e61"],["bei","jing","li","xiang"]],[[u"\u652f",u"\u79bb",u"\u7834",u"\u788e"],["zhi","li","po","sui"]],[[u"\u7686",u"\u5927",u"\u6b22",u"\u559c"],["jie","da","huan","xi"]],[[u"\u5927",u"\u540d",u"\u9f0e",u"\u9f0e"],["da","ming","ding","ding"]],[[u"\u5408",u"\u4e8c",u"\u4e3a",u"\u4e00"],["he","er","wei","yi"]],[[u"\u98ce",u"\u5439",u"\u8349",u"\u52a8"],["feng","chui","cao","dong"]],[[u"\u4f9d",u"\u4f9d",u"\u4e0d",u"\u820d"],["yi","yi","bu","she"]],[[u"\u79cb",u"\u9ad8",u"\u6c14",u"\u723d"],["qiu","gao","qi","shuang"]],[[u"\u633a",u"\u8eab",u"\u800c",u"\u51fa"],["ting","shen","er","chu"]],[[u"\u63a9",u"\u4eba",u"\u8033",u"\u76ee"],["yan","ren","er","mu"]],[[u"\u59d7",u"\u59d7",u"\u6765",u"\u8fdf"],["shan","shan","lai","chi"]],[[u"\u5b9e",u"\u81f3",u"\u540d",u"\u5f52"],["shi","zhi","ming","gui"]],[[u"\u4e8b",u"\u4e0e",u"\u613f",u"\u8fdd"],["shi","yu","yuan","wei"]],[[u"\u7fe9",u"\u7fe9",u"\u8d77",u"\u821e"],["pian","pian","qi","wu"]],[[u"\u51e4",u"\u6bdb",u"\u9e9f",u"\u89d2"],["feng","mao","lin","jiao"]],[[u"\u5fcd",u"\u6c14",u"\u541e",u"\u58f0"],["ren","qi","tun","sheng"]],[[u"\u8033",u"\u6fe1",u"\u76ee",u"\u67d3"],["er","ru","mu","ran"]],[[u"\u5929",u"\u4f26",u"\u4e4b",u"\u4e50"],["tian","lun","zhi","le"]],[[u"\u4e00",u"\u6c14",u"\u5475",u"\u6210"],["yi","qi","he","cheng"]],[[u"\u5343",u"\u8f7d",u"\u96be",u"\u9022"],["qian","zai","nan","feng"]],[[u"\u6ee1",u"\u76ee",u"\u75ae",u"\u75cd"],["man","mu","chuang","yi"]],[[u"\u4e00",u"\u65e0",u"\u6240",u"\u6709"],["yi","wu","suo","you"]],[[u"\u8ffd",u"\u6839",u"\u6eaf",u"\u6e90"],["zhui","gen","su","yuan"]],[[u"\u7cbe",u"\u795e",u"\u6296",u"\u64de"],["jing","shen","dou","sou"]],[[u"\u4eba",u"\u5fc3",u"\u60f6",u"\u60f6"],["ren","xin","huang","huang"]],[[u"\u671d",u"\u5915",u"\u76f8",u"\u5904"],["zhao","xi","xiang","chu"]],[[u"\u5f53",u"\u4ec1",u"\u4e0d",u"\u8ba9"],["dang","ren","bu","rang"]],[[u"\u4e0d",u"\u4f9d",u"\u4e0d",u"\u9976"],["bu","yi","bu","rao"]],[[u"\u8bbe",u"\u8eab",u"\u5904",u"\u5730"],["she","shen","chu","di"]],[[u"\u7126",u"\u5934",u"\u70c2",u"\u989d"],["jiao","tou","lan","e"]],[[u"\u65e0",u"\u7f18",u"\u65e0",u"\u6545"],["wu","yuan","wu","gu"]],[[u"\u65e5",u"\u79ef",u"\u6708",u"\u7d2f"],["ri","ji","yue","lei"]],[[u"\u65f7",u"\u65e5",u"\u6301",u"\u4e45"],["kuang","ri","chi","jiu"]],[[u"\u4e0d",u"\u80eb",u"\u800c",u"\u8d70"],["bu","jing","er","zou"]],[[u"\u5fcd",u"\u4fca",u"\u4e0d",u"\u7981"],["ren","jun","bu","jin"]],[[u"\u6210",u"\u7fa4",u"\u7ed3",u"\u961f"],["cheng","qun","jie","dui"]],[[u"\u65e0",u"\u7a3d",u"\u4e4b",u"\u8c08"],["wu","ji","zhi","tan"]],[[u"\u503a",u"\u53f0",u"\u9ad8",u"\u7b51"],["zhai","tai","gao","zhu"]],[[u"\u56e0",u"\u6750",u"\u65bd",u"\u6559"],["yin","cai","shi","jiao"]],[[u"\u5c45",u"\u5b89",u"\u601d",u"\u5371"],["ju","an","si","wei"]],[[u"\u624b",u"\u5fd9",u"\u811a",u"\u4e71"],["shou","mang","jiao","luan"]],[[u"\u8f7b",u"\u91cd",u"\u7f13",u"\u6025"],["qing","zhong","huan","ji"]],[[u"\u5e94",u"\u63a5",u"\u4e0d",u"\u6687"],["ying","jie","bu","xia"]],[[u"\u77e2",u"\u5fd7",u"\u4e0d",u"\u6e1d"],["shi","zhi","bu","yu"]],[[u"\u89e6",u"\u624b",u"\u53ef",u"\u53ca"],["chu","shou","ke","ji"]],[[u"\u53d1",u"\u4eba",u"\u6df1",u"\u7701"],["fa","ren","shen","xing"]],[[u"\u7834",u"\u95e8",u"\u800c",u"\u5165"],["po","men","er","ru"]],[[u"\u5f02",u"\u66f2",u"\u540c",u"\u5de5"],["yi","qu","tong","gong"]],[[u"\u5de6",u"\u90bb",u"\u53f3",u"\u820d"],["zuo","lin","you","she"]],[[u"\u4e50",u"\u5728",u"\u5176",u"\u4e2d"],["le","zai","qi","zhong"]],[[u"\u4ee5",u"\u8eab",u"\u8bd5",u"\u6cd5"],["yi","shen","shi","fa"]],[[u"\u517b",u"\u5bb6",u"\u7cca",u"\u53e3"],["yang","jia","hu","kou"]],[[u"\u4f17",u"\u77e2",u"\u4e4b",u"\u7684"],["zhong","shi","zhi","di"]],[[u"\u5fc3",u"\u5e73",u"\u6c14",u"\u548c"],["xin","ping","qi","he"]],[[u"\u82e5",u"\u9690",u"\u82e5",u"\u73b0"],["ruo","yin","ruo","xian"]],[[u"\u54d7",u"\u4f17",u"\u53d6",u"\u5ba0"],["hua","zhong","qu","chong"]],[[u"\u7a7a",u"\u7a74",u"\u6765",u"\u98ce"],["kong","xue","lai","feng"]],[[u"\u56e0",u"\u52bf",u"\u5229",u"\u5bfc"],["yin","shi","li","dao"]],[[u"\u5fb7",u"\u9ad8",u"\u671b",u"\u91cd"],["de","gao","wang","zhong"]],[[u"\u6709",u"\u6043",u"\u65e0",u"\u6050"],["you","shi","wu","kong"]],[[u"\u4eba",u"\u547d",u"\u5173",u"\u5929"],["ren","ming","guan","tian"]],[[u"\u6c14",u"\u52bf",u"\u78c5",u"\u7934"],["qi","shi","bang","bo"]],[[u"\u6619",u"\u82b1",u"\u4e00",u"\u73b0"],["tan","hua","yi","xian"]],[[u"\u606f",u"\u4e8b",u"\u5b81",u"\u4eba"],["xi","shi","ning","ren"]],[[u"\u8361",u"\u7136",u"\u65e0",u"\u5b58"],["dang","ran","wu","cun"]],[[u"\u6b22",u"\u6b23",u"\u9f13",u"\u821e"],["huan","xin","gu","wu"]],[[u"\u60ca",u"\u5929",u"\u52a8",u"\u5730"],["jing","tian","dong","di"]],[[u"\u8270",u"\u96be",u"\u9669",u"\u963b"],["jian","nan","xian","zu"]],[[u"\u9669",u"\u8c61",u"\u73af",u"\u751f"],["xian","xiang","huan","sheng"]],[[u"\u5207",u"\u8eab",u"\u4f53",u"\u4f1a"],["qie","shen","ti","hui"]],[[u"\u4ee5",u"\u5047",u"\u4e71",u"\u771f"],["yi","jia","luan","zhen"]],[[u"\u5929",u"\u5bd2",u"\u5730",u"\u51bb"],["tian","han","di","dong"]],[[u"\u8f9e",u"\u65e7",u"\u8fce",u"\u65b0"],["ci","jiu","ying","xin"]],[[u"\u8d1f",u"\u503a",u"\u7d2f",u"\u7d2f"],["fu","zhai","lei","lei"]],[[u"\u4efb",u"\u52b3",u"\u4efb",u"\u6028"],["ren","lao","ren","yuan"]],[[u"\u8d70",u"\u6295",u"\u65e0",u"\u8def"],["zou","tou","wu","lu"]],[[u"\u91cd",u"\u8e48",u"\u8986",u"\u8f99"],["zhong","dao","fu","zhe"]],[[u"\u65e0",u"\u65f6",u"\u65e0",u"\u523b"],["wu","shi","wu","ke"]],[[u"\u6210",u"\u5bb6",u"\u7acb",u"\u4e1a"],["cheng","jia","li","ye"]],[[u"\u708e",u"\u9ec4",u"\u5b50",u"\u5b59"],["yan","huang","zi","sun"]],[[u"\u5251",u"\u62d4",u"\u5f29",u"\u5f20"],["jian","ba","nu","zhang"]],[[u"\u5c06",u"\u5fc3",u"\u6bd4",u"\u5fc3"],["jiang","xin","bi","xin"]],[[u"\u4e00",u"\u89c8",u"\u65e0",u"\u4f59"],["yi","lan","wu","yu"]],[[u"\u4e3a",u"\u6240",u"\u6b32",u"\u4e3a"],["wei","suo","yu","wei"]],[[u"\u540d",u"\u6b63",u"\u8a00",u"\u987a"],["ming","zheng","yan","shun"]],[[u"\u7eb8",u"\u4e0a",u"\u8c08",u"\u5175"],["zhi","shang","tan","bing"]],[[u"\u5ddd",u"\u6d41",u"\u4e0d",u"\u606f"],["chuan","liu","bu","xi"]],[[u"\u591c",u"\u6df1",u"\u4eba",u"\u9759"],["ye","shen","ren","jing"]],[[u"\u7f8e",u"\u4e0d",u"\u80dc",u"\u6536"],["mei","bu","sheng","shou"]],[[u"\u5584",u"\u59cb",u"\u5584",u"\u7ec8"],["shan","shi","shan","zhong"]],[[u"\u679d",u"\u7e41",u"\u53f6",u"\u8302"],["zhi","fan","ye","mao"]],[[u"\u65a9",u"\u9489",u"\u622a",u"\u94c1"],["zhan","ding","jie","tie"]],[[u"\u5927",u"\u6709",u"\u88e8",u"\u76ca"],["da","you","bi","yi"]],[[u"\u9632",u"\u5fae",u"\u675c",u"\u6e10"],["fang","wei","du","jian"]],[[u"\u65e0",u"\u5f71",u"\u65e0",u"\u8e2a"],["wu","ying","wu","zong"]],[[u"\u4e3e",u"\u624b",u"\u4e4b",u"\u52b3"],["ju","shou","zhi","lao"]],[[u"\u8d70",u"\u9a6c",u"\u4e0a",u"\u4efb"],["zou","ma","shang","ren"]],[[u"\u62cd",u"\u624b",u"\u79f0",u"\u5feb"],["pai","shou","cheng","kuai"]],[[u"\u6d77",u"\u7eb3",u"\u767e",u"\u5ddd"],["hai","na","bai","chuan"]],[[u"\u6765",u"\u5386",u"\u4e0d",u"\u660e"],["lai","li","bu","ming"]],[[u"\u6c57",u"\u6d41",u"\u6d43",u"\u80cc"],["han","liu","jia","bei"]],[[u"\u4e03",u"\u5634",u"\u516b",u"\u820c"],["qi","zui","ba","she"]],[[u"\u672c",u"\u672b",u"\u5012",u"\u7f6e"],["ben","mo","dao","zhi"]],[[u"\u6df7",u"\u6dc6",u"\u89c6",u"\u542c"],["hun","xiao","shi","ting"]],[[u"\u70ed",u"\u8840",u"\u6cb8",u"\u817e"],["re","xue","fei","teng"]],[[u"\u5de6",u"\u53f3",u"\u4e3a",u"\u96be"],["zuo","you","wei","nan"]],[[u"\u98ce",u"\u5e73",u"\u6d6a",u"\u9759"],["feng","ping","lang","jing"]],[[u"\u5982",u"\u5c65",u"\u8584",u"\u51b0"],["ru","lv","bo","bing"]],[[u"\u5148",u"\u5929",u"\u4e0d",u"\u8db3"],["xian","tian","bu","zu"]],[[u"\u62db",u"\u6447",u"\u649e",u"\u9a97"],["zhao","yao","zhuang","pian"]],[[u"\u89e3",u"\u7591",u"\u91ca",u"\u60d1"],["jie","yi","shi","huo"]],[[u"\u4e0d",u"\u901f",u"\u4e4b",u"\u5ba2"],["bu","su","zhi","ke"]],[[u"\u5fc3",u"\u670d",u"\u53e3",u"\u670d"],["xin","fu","kou","fu"]],[[u"\u4e1c",u"\u62fc",u"\u897f",u"\u51d1"],["dong","pin","xi","cou"]],[[u"\u4e00",u"\u843d",u"\u5343",u"\u4e08"],["yi","luo","qian","zhang"]],[[u"\u706b",u"\u4e0a",u"\u6d47",u"\u6cb9"],["huo","shang","jiao","you"]],[[u"\u5c31",u"\u4e8b",u"\u8bba",u"\u4e8b"],["jiu","shi","lun","shi"]],[[u"\u6ca1",u"\u5b8c",u"\u6ca1",u"\u4e86"],["mei","wan","mei","liao"]],[[u"\u5371",u"\u8a00",u"\u8038",u"\u542c"],["wei","yan","song","ting"]],[[u"\u5929",u"\u9a6c",u"\u884c",u"\u7a7a"],["tian","ma","xing","kong"]],[[u"\u715e",u"\u8d39",u"\u82e6",u"\u5fc3"],["sha","fei","ku","xin"]],[[u"\u81ea",u"\u6b3a",u"\u6b3a",u"\u4eba"],["zi","qi","qi","ren"]],[[u"\u8bb3",u"\u83ab",u"\u5982",u"\u6df1"],["hui","mo","ru","shen"]],[[u"\u65ad",u"\u7ae0",u"\u53d6",u"\u4e49"],["duan","zhang","qu","yi"]],[[u"\u4e94",u"\u5f69",u"\u7f24",u"\u7eb7"],["wu","cai","bin","fen"]],[[u"\u8fdb",u"\u9000",u"\u4e24",u"\u96be"],["jin","tui","liang","nan"]],[[u"\u6539",u"\u8fc7",u"\u81ea",u"\u65b0"],["gai","guo","zi","xin"]],[[u"\u6025",u"\u4e8e",u"\u6c42",u"\u6210"],["ji","yu","qiu","cheng"]],[[u"\u4e25",u"\u60e9",u"\u4e0d",u"\u8d37"],["yan","cheng","bu","dai"]],[[u"\u75b2",u"\u60eb",u"\u4e0d",u"\u582a"],["pi","bei","bu","kan"]],[[u"\u767e",u"\u6298",u"\u4e0d",u"\u6320"],["bai","zhe","bu","nao"]],[[u"\u5927",u"\u663e",u"\u8eab",u"\u624b"],["da","xian","shen","shou"]],[[u"\u5934",u"\u7834",u"\u8840",u"\u6d41"],["tou","po","xue","liu"]],[[u"\u6d51",u"\u6c34",u"\u6478",u"\u9c7c"],["hun","shui","mo","yu"]],[[u"\u4e0d",u"\u5bb9",u"\u7f6e",u"\u7591"],["bu","rong","zhi","yi"]],[[u"\u5b5c",u"\u5b5c",u"\u4e0d",u"\u5026"],["zi","zi","bu","juan"]],[[u"\u957f",u"\u4e45",u"\u4e4b",u"\u8ba1"],["chang","jiu","zhi","ji"]],[[u"\u95fb",u"\u540d",u"\u9050",u"\u8fe9"],["wen","ming","xia","er"]],[[u"\u6307",u"\u624b",u"\u753b",u"\u811a"],["zhi","shou","hua","jiao"]],[[u"\u8d6b",u"\u8d6b",u"\u6709",u"\u540d"],["he","he","you","ming"]],[[u"\u706d",u"\u9876",u"\u4e4b",u"\u707e"],["mie","ding","zhi","zai"]],[[u"\u5982",u"\u5f71",u"\u968f",u"\u5f62"],["ru","ying","sui","xing"]],[[u"\u98ce",u"\u8c03",u"\u96e8",u"\u987a"],["feng","tiao","yu","shun"]],[[u"\u8336",u"\u4f59",u"\u996d",u"\u540e"],["cha","yu","fan","hou"]],[[u"\u75db",u"\u54ed",u"\u6d41",u"\u6d95"],["tong","ku","liu","ti"]],[[u"\u9ad8",u"\u5c4b",u"\u5efa",u"\u74f4"],["gao","wu","jian","ling"]],[[u"\u8d70",u"\u9a6c",u"\u89c2",u"\u82b1"],["zou","ma","guan","hua"]],[[u"\u61a8",u"\u6001",u"\u53ef",u"\u63ac"],["han","tai","ke","ju"]],[[u"\u5c61",u"\u6559",u"\u4e0d",u"\u6539"],["lv","jiao","bu","gai"]],[[u"\u6b6a",u"\u98ce",u"\u90aa",u"\u6c14"],["wai","feng","xie","qi"]],[[u"\u5931",u"\u4e4b",u"\u4ea4",u"\u81c2"],["shi","zhi","jiao","bi"]],[[u"\u5e73",u"\u5fc3",u"\u800c",u"\u8bba"],["ping","xin","er","lun"]],[[u"\u4e0d",u"\u5728",u"\u8bdd",u"\u4e0b"],["bu","zai","hua","xia"]],[[u"\u62c5",u"\u60ca",u"\u53d7",u"\u6015"],["dan","jing","shou","pa"]],[[u"\u7ea6",u"\u5b9a",u"\u4fd7",u"\u6210"],["yue","ding","su","cheng"]],[[u"\u5ec9",u"\u6d01",u"\u5949",u"\u516c"],["lian","jie","feng","gong"]],[[u"\u679c",u"\u4e0d",u"\u5176",u"\u7136"],["guo","bu","qi","ran"]],[[u"\u6674",u"\u5929",u"\u9739",u"\u96f3"],["qing","tian","pi","li"]],[[u"\u6b63",u"\u672c",u"\u6e05",u"\u6e90"],["zheng","ben","qing","yuan"]],[[u"\u4e0d",u"\u8d1f",u"\u4f17",u"\u671b"],["bu","fu","zhong","wang"]],[[u"\u77ac",u"\u606f",u"\u4e07",u"\u53d8"],["shun","xi","wan","bian"]],[[u"\u4e0d",u"\u53ef",u"\u903e",u"\u8d8a"],["bu","ke","yu","yue"]],[[u"\u8bed",u"\u7109",u"\u4e0d",u"\u8be6"],["yu","yan","bu","xiang"]],[[u"\u60b2",u"\u75db",u"\u6b32",u"\u7edd"],["bei","tong","yu","jue"]],[[u"\u5404",u"\u663e",u"\u795e",u"\u901a"],["ge","xian","shen","tong"]],[[u"\u524d",u"\u8d74",u"\u540e",u"\u7ee7"],["qian","fu","hou","ji"]],[[u"\u7ffb",u"\u5c71",u"\u8d8a",u"\u5cad"],["fan","shan","yue","ling"]],[[u"\u4e34",u"\u5371",u"\u53d7",u"\u547d"],["lin","wei","shou","ming"]],[[u"\u5fd0",u"\u5fd1",u"\u4e0d",u"\u5b89"],["tan","te","bu","an"]],[[u"\u4e0d",u"\u62d8",u"\u4e00",u"\u683c"],["bu","ju","yi","ge"]],[[u"\u6709",u"\u673a",u"\u53ef",u"\u4e58"],["you","ji","ke","cheng"]],[[u"\u6f2b",u"\u5c71",u"\u904d",u"\u91ce"],["man","shan","bian","ye"]],[[u"\u8d5e",u"\u53f9",u"\u4e0d",u"\u5df2"],["zan","tan","bu","yi"]],[[u"\u800c",u"\u7acb",u"\u4e4b",u"\u5e74"],["er","li","zhi","nian"]],[[u"\u4e0d",u"\u5047",u"\u601d",u"\u7d22"],["bu","jia","si","suo"]],[[u"\u4e0d",u"\u5c48",u"\u4e0d",u"\u6320"],["bu","qu","bu","nao"]],[[u"\u6f78",u"\u7136",u"\u6cea",u"\u4e0b"],["shan","ran","lei","xia"]],[[u"\u793c",u"\u5c1a",u"\u5f80",u"\u6765"],["li","shang","wang","lai"]],[[u"\u7075",u"\u673a",u"\u4e00",u"\u52a8"],["ling","ji","yi","dong"]],[[u"\u5f15",u"\u4eba",u"\u5165",u"\u80dc"],["yin","ren","ru","sheng"]],[[u"\u82e5",u"\u65e0",u"\u5176",u"\u4e8b"],["ruo","wu","qi","shi"]],[[u"\u719f",u"\u89c6",u"\u65e0",u"\u7779"],["shu","shi","wu","du"]],[[u"\u9a87",u"\u4eba",u"\u542c",u"\u95fb"],["hai","ren","ting","wen"]],[[u"\u8d8b",u"\u5229",u"\u907f",u"\u5bb3"],["qu","li","bi","hai"]],[[u"\u7cbe",u"\u529b",u"\u5145",u"\u6c9b"],["jing","li","chong","pei"]],[[u"\u51a0",u"\u5195",u"\u5802",u"\u7687"],["guan","mian","tang","huang"]],[[u"\u5206",u"\u9053",u"\u626c",u"\u9573"],["fen","dao","yang","biao"]],[[u"\u8377",u"\u67aa",u"\u5b9e",u"\u5f39"],["he","qiang","shi","dan"]],[[u"\u8001",u"\u751f",u"\u5e38",u"\u8c08"],["lao","sheng","chang","tan"]],[[u"\u5f7b",u"\u5934",u"\u5f7b",u"\u5c3e"],["che","tou","che","wei"]],[[u"\u5b89",u"\u8eab",u"\u7acb",u"\u547d"],["an","shen","li","ming"]],[[u"\u98ce",u"\u96e8",u"\u540c",u"\u821f"],["feng","yu","tong","zhou"]],[[u"\u6e38",u"\u624b",u"\u597d",u"\u95f2"],["you","shou","hao","xian"]],[[u"\u5fc3",u"\u7070",u"\u610f",u"\u51b7"],["xin","hui","yi","leng"]],[[u"\u7f51",u"\u5f00",u"\u4e00",u"\u9762"],["wang","kai","yi","mian"]],[[u"\u7cbe",u"\u5175",u"\u5f3a",u"\u5c06"],["jing","bing","qiang","jiang"]],[[u"\u7535",u"\u95ea",u"\u96f7",u"\u9e23"],["dian","shan","lei","ming"]],[[u"\u661f",u"\u7f57",u"\u68cb",u"\u5e03"],["xing","luo","qi","bu"]],[[u"\u4e09",u"\u7f04",u"\u5176",u"\u53e3"],["san","jian","qi","kou"]],[[u"\u4f17",u"\u76ee",u"\u777d",u"\u777d"],["zhong","mu","kui","kui"]],[[u"\u6df7",u"\u4e3a",u"\u4e00",u"\u8c08"],["hun","wei","yi","tan"]],[[u"\u4e0d",u"\u6b22",u"\u800c",u"\u6563"],["bu","huan","er","san"]],[[u"\u4e95",u"\u4e95",u"\u6709",u"\u6761"],["jing","jing","you","tiao"]],[[u"\u9cde",u"\u6b21",u"\u6809",u"\u6bd4"],["lin","ci","zhi","bi"]],[[u"\u81ea",u"\u4ee5",u"\u4e3a",u"\u662f"],["zi","yi","wei","shi"]],[[u"\u4e0d",u"\u52a8",u"\u58f0",u"\u8272"],["bu","dong","sheng","se"]],[[u"\u7a33",u"\u624e",u"\u7a33",u"\u6253"],["wen","zha","wen","da"]],[[u"\u4f3c",u"\u66fe",u"\u76f8",u"\u8bc6"],["si","ceng","xiang","shi"]],[[u"\u7a7a",u"\u7a7a",u"\u5982",u"\u4e5f"],["kong","kong","ru","ye"]],[[u"\u5371",u"\u5728",u"\u65e6",u"\u5915"],["wei","zai","dan","xi"]],[[u"\u5f00",u"\u8bda",u"\u5e03",u"\u516c"],["kai","cheng","bu","gong"]],[[u"\u53ef",u"\u6b4c",u"\u53ef",u"\u6ce3"],["ke","ge","ke","qi"]],[[u"\u53e3",u"\u8bdb",u"\u7b14",u"\u4f10"],["kou","zhu","bi","fa"]],[[u"\u91dc",u"\u5e95",u"\u62bd",u"\u85aa"],["fu","di","chou","xin"]],[[u"\u4e3e",u"\u4e16",u"\u95fb",u"\u540d"],["ju","shi","wen","ming"]],[[u"\u4e00",u"\u95e8",u"\u5fc3",u"\u601d"],["yi","men","xin","si"]],[[u"\u4e0d",u"\u4e00",u"\u800c",u"\u8db3"],["bu","yi","er","zu"]],[[u"\u5fb7",u"\u827a",u"\u53cc",u"\u99a8"],["de","yi","shuang","xin"]],[[u"\u80c6",u"\u6218",u"\u5fc3",u"\u60ca"],["dan","zhan","xin","jing"]],[[u"\u575a",u"\u97e7",u"\u4e0d",u"\u62d4"],["jian","ren","bu","ba"]],[[u"\u8d77",u"\u6b7b",u"\u56de",u"\u751f"],["qi","si","hui","sheng"]],[[u"\u5168",u"\u795e",u"\u8d2f",u"\u6ce8"],["quan","shen","guan","zhu"]],[[u"\u6b7b",u"\u91cc",u"\u9003",u"\u751f"],["si","li","tao","sheng"]],[[u"\u4e00",u"\u9a6c",u"\u5f53",u"\u5148"],["yi","ma","dang","xian"]],[[u"\u539a",u"\u79ef",u"\u8584",u"\u53d1"],["hou","ji","bao","fa"]],[[u"\u65e0",u"\u7406",u"\u53d6",u"\u95f9"],["wu","li","qu","nao"]],[[u"\u5f53",u"\u673a",u"\u7acb",u"\u65ad"],["dang","ji","li","duan"]],[[u"\u540d",u"\u5b58",u"\u5b9e",u"\u4ea1"],["ming","cun","shi","wang"]],[[u"\u5982",u"\u91ca",u"\u91cd",u"\u8d1f"],["ru","shi","zhong","fu"]],[[u"\u96f7",u"\u6253",u"\u4e0d",u"\u52a8"],["lei","da","bu","dong"]],[[u"\u4e00",u"\u671b",u"\u65e0",u"\u9645"],["yi","wang","wu","ji"]],[[u"\u4e0e",u"\u4e16",u"\u9694",u"\u7edd"],["yu","shi","ge","jue"]],[[u"\u95e8",u"\u53ef",u"\u7f57",u"\u96c0"],["men","ke","luo","que"]],[[u"\u5927",u"\u6447",u"\u5927",u"\u6446"],["da","yao","da","bai"]],[[u"\u5c06",u"\u4fe1",u"\u5c06",u"\u7591"],["jiang","xin","jiang","yi"]],[[u"\u9976",u"\u6709",u"\u5174",u"\u8da3"],["rao","you","xing","qu"]],[[u"\u5fc3",u"\u65f7",u"\u795e",u"\u6021"],["xin","kuang","shen","yi"]],[[u"\u5fc3",u"\u7167",u"\u4e0d",u"\u5ba3"],["xin","zhao","bu","xuan"]],[[u"\u534a",u"\u9014",u"\u800c",u"\u5e9f"],["ban","tu","er","fei"]],[[u"\u65e0",u"\u8ba1",u"\u53ef",u"\u65bd"],["wu","ji","ke","shi"]],[[u"\u4e00",u"\u584c",u"\u7cca",u"\u6d82"],["yi","ta","hu","tu"]],[[u"\u540e",u"\u6765",u"\u5c45",u"\u4e0a"],["hou","lai","ju","shang"]],[[u"\u5e76",u"\u9a7e",u"\u9f50",u"\u9a71"],["bing","jia","qi","qu"]],[[u"\u4e0d",u"\u65f6",u"\u4e4b",u"\u9700"],["bu","shi","zhi","xu"]],[[u"\u81ea",u"\u544a",u"\u594b",u"\u52c7"],["zi","gao","fen","yong"]],[[u"\u4e1c",u"\u5c71",u"\u518d",u"\u8d77"],["dong","shan","zai","qi"]],[[u"\u9512",u"\u94db",u"\u5165",u"\u72f1"],["lang","dang","ru","yu"]],[[u"\u77f3",u"\u6c89",u"\u5927",u"\u6d77"],["shi","chen","da","hai"]],[[u"\u9690",u"\u59d3",u"\u57cb",u"\u540d"],["yin","xing","mai","ming"]],[[u"\u6124",u"\u6124",u"\u4e0d",u"\u5e73"],["fen","fen","bu","ping"]],[[u"\u4e00",u"\u9f13",u"\u4f5c",u"\u6c14"],["yi","gu","zuo","qi"]],[[u"\u5fc3",u"\u5b89",u"\u7406",u"\u5f97"],["xin","an","li","de"]],[[u"\u5343",u"\u5934",u"\u4e07",u"\u7eea"],["qian","tou","wan","xu"]],[[u"\u51b0",u"\u5929",u"\u96ea",u"\u5730"],["bing","tian","xue","di"]],[[u"\u540e",u"\u8d77",u"\u4e4b",u"\u79c0"],["hou","qi","zhi","xiu"]],[[u"\u8c28",u"\u8a00",u"\u614e",u"\u884c"],["jin","yan","shen","xing"]],[[u"\u65f6",u"\u8fc7",u"\u5883",u"\u8fc1"],["shi","guo","jing","qian"]],[[u"\u552f",u"\u5229",u"\u662f",u"\u56fe"],["wei","li","shi","tu"]],[[u"\u5c45",u"\u9ad8",u"\u4e34",u"\u4e0b"],["ju","gao","lin","xia"]],[[u"\u4e8b",u"\u65e0",u"\u5de8",u"\u7ec6"],["shi","wu","ju","xi"]],[[u"\u65e0",u"\u5b54",u"\u4e0d",u"\u5165"],["wu","kong","bu","ru"]],[[u"\u52bf",u"\u4e0d",u"\u53ef",u"\u6321"],["shi","bu","ke","dang"]],[[u"\u70df",u"\u6d88",u"\u4e91",u"\u6563"],["yan","xiao","yun","san"]],[[u"\u5e2d",u"\u5730",u"\u800c",u"\u5750"],["xi","di","er","zuo"]],[[u"\u8c41",u"\u7136",u"\u5f00",u"\u6717"],["huo","ran","kai","lang"]],[[u"\u4e49",u"\u6124",u"\u586b",u"\u81ba"],["yi","fen","tian","ying"]],[[u"\u4e0d",u"\u8fdb",u"\u5219",u"\u9000"],["bu","jin","ze","tui"]],[[u"\u8eab",u"\u5148",u"\u58eb",u"\u5352"],["shen","xian","shi","zu"]],[[u"\u4e00",u"\u6982",u"\u800c",u"\u8bba"],["yi","gai","er","lun"]],[[u"\u6577",u"\u884d",u"\u4e86",u"\u4e8b"],["fu","yan","liao","shi"]],[[u"\u9ad8",u"\u6795",u"\u65e0",u"\u5fe7"],["gao","zhen","wu","you"]],[[u"\u5de7",u"\u7acb",u"\u540d",u"\u76ee"],["qiao","li","ming","mu"]],[[u"\u4e07",u"\u4e0d",u"\u5f97",u"\u5df2"],["wan","bu","de","yi"]],[[u"\u9707",u"\u8033",u"\u6b32",u"\u804b"],["zhen","er","yu","long"]],[[u"\u4eca",u"\u975e",u"\u6614",u"\u6bd4"],["jin","fei","xi","bi"]],[[u"\u62c9",u"\u5e2e",u"\u7ed3",u"\u6d3e"],["la","bang","jie","pai"]],[[u"\u624b",u"\u821e",u"\u8db3",u"\u8e48"],["shou","wu","zu","dao"]],[[u"\u5343",u"\u547c",u"\u4e07",u"\u5524"],["qian","hu","wan","huan"]],[[u"\u9065",u"\u9065",u"\u9886",u"\u5148"],["yao","yao","ling","xian"]],[[u"\u76f8",u"\u6fe1",u"\u4ee5",u"\u6cab"],["xiang","ru","yi","mo"]],[[u"\u5148",u"\u5165",u"\u4e3a",u"\u4e3b"],["xian","ru","wei","zhu"]],[[u"\u6a2a",u"\u4e03",u"\u7ad6",u"\u516b"],["heng","qi","shu","ba"]],[[u"\u75db",u"\u5fc3",u"\u75be",u"\u9996"],["tong","xin","ji","shou"]],[[u"\u5316",u"\u6574",u"\u4e3a",u"\u96f6"],["hua","zheng","wei","ling"]],[[u"\u9633",u"\u5949",u"\u9634",u"\u8fdd"],["yang","feng","yin","wei"]],[[u"\u6c89",u"\u9ed8",u"\u5be1",u"\u8a00"],["chen","mo","gua","yan"]],[[u"\u987a",u"\u624b",u"\u7275",u"\u7f8a"],["shun","shou","qian","yang"]],[[u"\u6e10",u"\u5165",u"\u4f73",u"\u5883"],["jian","ru","jia","jing"]],[[u"\u675f",u"\u624b",u"\u5c31",u"\u64d2"],["shu","shou","jiu","qin"]],[[u"\u5fc3",u"\u65e0",u"\u65c1",u"\u9a9b"],["xin","wu","pang","wu"]],[[u"\u632f",u"\u804b",u"\u53d1",u"\u8069"],["zhen","long","fa","kui"]],[[u"\u6773",u"\u65e0",u"\u97f3",u"\u8baf"],["yao","wu","yin","xun"]],[[u"\u60c5",u"\u6709",u"\u53ef",u"\u539f"],["qing","you","ke","yuan"]],[[u"\u5c3d",u"\u529b",u"\u800c",u"\u4e3a"],["jin","li","er","wei"]],[[u"\u6295",u"\u673a",u"\u53d6",u"\u5de7"],["tou","ji","qu","qiao"]],[[u"\u5c0f",u"\u9898",u"\u5927",u"\u505a"],["xiao","ti","da","zuo"]],[[u"\u7ea6",u"\u6cd5",u"\u4e09",u"\u7ae0"],["yue","fa","san","zhang"]],[[u"\u4e0d",u"\u5c51",u"\u4e00",u"\u987e"],["bu","xie","yi","gu"]],[[u"\u81ea",u"\u5706",u"\u5176",u"\u8bf4"],["zi","yuan","qi","shuo"]],[[u"\u4eba",u"\u5c3d",u"\u5176",u"\u624d"],["ren","jin","qi","cai"]],[[u"\u968f",u"\u6ce2",u"\u9010",u"\u6d41"],["sui","bo","zhu","liu"]],[[u"\u671b",u"\u5b50",u"\u6210",u"\u9f99"],["wang","zi","cheng","long"]],[[u"\u9e21",u"\u6bdb",u"\u849c",u"\u76ae"],["ji","mao","suan","pi"]],[[u"\u8083",u"\u7136",u"\u8d77",u"\u656c"],["su","ran","qi","jing"]],[[u"\u675f",u"\u4e4b",u"\u9ad8",u"\u9601"],["shu","zhi","gao","ge"]],[[u"\u56e0",u"\u564e",u"\u5e9f",u"\u98df"],["yin","ye","fei","shi"]],[[u"\u53e6",u"\u8d77",u"\u7089",u"\u7076"],["ling","qi","lu","zao"]],[[u"\u9752",u"\u9ec4",u"\u4e0d",u"\u63a5"],["qing","huang","bu","jie"]],[[u"\u9762",u"\u9762",u"\u4ff1",u"\u5230"],["mian","mian","ju","dao"]],[[u"\u5929",u"\u6daf",u"\u6d77",u"\u89d2"],["tian","ya","hai","jiao"]],[[u"\u8bed",u"\u65e0",u"\u4f26",u"\u6b21"],["yu","wu","lun","ci"]],[[u"\u6717",u"\u6717",u"\u4e0a",u"\u53e3"],["lang","lang","shang","kou"]],[[u"\u820d",u"\u8fd1",u"\u6c42",u"\u8fdc"],["she","jin","qiu","yuan"]],[[u"\u7f6e",u"\u8eab",u"\u4e8b",u"\u5916"],["zhi","shen","shi","wai"]],[[u"\u97a0",u"\u8eac",u"\u5c3d",u"\u7601"],["ju","gong","jin","cui"]],[[u"\u6d3b",u"\u8e66",u"\u4e71",u"\u8df3"],["huo","beng","luan","tiao"]],[[u"\u4e0d",u"\u5bd2",u"\u800c",u"\u6817"],["bu","han","er","li"]],[[u"\u660e",u"\u8fa8",u"\u662f",u"\u975e"],["ming","bian","shi","fei"]],[[u"\u8a00",u"\u7b80",u"\u610f",u"\u8d45"],["yan","jian","yi","gai"]],[[u"\u9e1f",u"\u8bed",u"\u82b1",u"\u9999"],["niao","yu","hua","xiang"]],[[u"\u907f",u"\u800c",u"\u4e0d",u"\u8c08"],["bi","er","bu","tan"]],[[u"\u5934",u"\u5934",u"\u662f",u"\u9053"],["tou","tou","shi","dao"]],[[u"\u5b89",u"\u8425",u"\u624e",u"\u5be8"],["an","ying","zha","zhai"]],[[u"\u98ce",u"\u5c18",u"\u4ec6",u"\u4ec6"],["feng","chen","pu","pu"]],[[u"\u524d",u"\u65e0",u"\u53e4",u"\u4eba"],["qian","wu","gu","ren"]],[[u"\u65e0",u"\u53ef",u"\u975e",u"\u8bae"],["wu","ke","fei","yi"]],[[u"\u65e0",u"\u6240",u"\u4e0d",u"\u80fd"],["wu","suo","bu","neng"]],[[u"\u7b4b",u"\u75b2",u"\u529b",u"\u5c3d"],["jin","pi","li","jin"]],[[u"\u5f20",u"\u706f",u"\u7ed3",u"\u5f69"],["zhang","deng","jie","cai"]],[[u"\u4e00",u"\u54c4",u"\u800c",u"\u4e0a"],["yi","hong","er","shang"]],[[u"\u4e0d",u"\u7531",u"\u5206",u"\u8bf4"],["bu","you","fen","shuo"]],[[u"\u9163",u"\u7545",u"\u6dcb",u"\u6f13"],["han","chang","lin","li"]],[[u"\u5357",u"\u8f95",u"\u5317",u"\u8f99"],["nan","yuan","bei","zhe"]],[[u"\u5192",u"\u540d",u"\u9876",u"\u66ff"],["mao","ming","ding","ti"]],[[u"\u4e0d",u"\u4e49",u"\u4e4b",u"\u8d22"],["bu","yi","zhi","cai"]]]

ii=["a","ai","an","ang","ao","ba","bai","ban","bang","bao","bei","ben","beng","bi","bian","biao","bie","bin","bing","bo","bu","ca","cai","can","cang","cao","ce","cen","ceng","cha","chai","chan","chang","chao","che","chen","cheng","chi","chong","chou","chu","chua","chuai","chuan","chuang","chui","chun","chuo","ci","cong","cou","cu","cuan","cui","cun","cuo","da","dai","dan","dang","dao","de","dei","den","deng","di","dia","dian","diao","die","ding","diu","dong","dou","du","duan","dui","dun","duo","e","en","eng","er","fa","fan","fang","fei","fen","feng","fiao","fo","fou","fu","ga","gai","gan","gang","gao","ge","gei","gen","geng","gong","gou","gu","gua","guai","guan","guang","gui","gun","guo","ha","hai","han","hang","hao","he","hei","hen","heng","hong","hou","hu","hua","huai","huan","huang","hui","hun","huo","ji","jia","jian","jiang","jiao","jie","jin","jing","jiong","jiu","ju","jun","juan","jue","ka","kai","kan","kang","kao","ke","ken","keng","kong","kou","ku","kua","kuai","kuan","kuang","kui","kun","kuo","la","lai","lan","lang","lao","le","lei","leng","li","lia","lian","liang","liao","lie","lin","ling","liu","lo","long","lou","lu","lue","luan","lun","luo","lv","lve","ma","mai","man","mang","mao","me","mei","men","meng","mi","mian","miao","mie","min","ming","miu","mo","mou","mu","na","nai","nan","nang","nao","ne","nei","nen","neng","ni","nian","niang","niao","nie","nin","ning","niu","nong","nou","nu","nuan","nun","nuo","nv","nve","o","ou","pa","pai","pan","pang","pao","pei","pen","peng","pi","pian","piao","pie","pin","ping","po","pou","pu","qi","qia","qian","qiang","qiao","qie","qin","qing","qiong","qiu","qu","quan","que","qun","ran","rang","rao","re","ren","reng","ri","rong","rou","ru","rua","ruan","rui","run","ruo","sa","sai","san","sang","sao","se","sen","seng","sha","shai","shan","shang","shao","she","shei","shen","sheng","shi","shou","shu","shua","shuai","shuan","shuang","shui","shun","shuo","si","song","sou","su","suan","sui","sun","suo","ta","tai","tan","tang","tao","te","tei","teng","ti","tian","tiao","tie","ting","tong","tou","tu","tuan","tui","tun","tuo","wa","wai","wan","wang","wei","wen","weng","wo","wu","xi","xia","xian","xiang","xiao","xie","xin","xing","xiong","xiu","xu","xuan","xue","xun","ya","yan","yang","yao","ye","yi","yin","ying","yo","yong","you","yu","yuan","yue","yun","za","zai","zan","zang","zao","ze","zei","zen","zeng","zha","zhai","zhan","zhang","zhao","zhe","zhei","zhen","zheng","zhi","zhong","zhou","zhu","zhua","zhuai","zhuan","zhuang","zhui","zhun","zhuo","zi","zong","zou","zu","zuan","zui","zun","zuo"]

index = random.randint(0, len(v)-1)
answer = v[index][1]
count1 = len(answer[0])
count2 = len(answer[1])
count3 = len(answer[2])
count4 = len(answer[3])

print(str(count1)+","+str(count2)+","+str(count3)+","+str(count4))

chinese = v[index][0]

#print(json.dumps([chinese], ensure_ascii=False))
while True:
    guess1 = raw_input("guess1:\n")
    guess1_list = guess1.split(" ")
    if(len(guess1_list) != 4):
        print("成语长度错误")
        continue
    elif(len(guess1_list[0])) != count1:
        print("第1个字拼音长度错误")
        continue
    elif(len(guess1_list[1])) != count2:
        print("第2个字拼音长度错误")
        continue    
    elif(len(guess1_list[2])) != count3:
        print("第3个字拼音长度错误")
        continue
    elif(len(guess1_list[3])) != count4:
        print("第4个字拼音长度错误")
        continue
    elif(str(guess1_list[0]) not in ii):
        print("第1个字拼音拼写错误")
        continue
    elif(str(guess1_list[1]) not in ii):
        print("第2个字拼音拼写错误")
        continue
    elif(str(guess1_list[2]) not in ii):
        print("第3个字拼音拼写错误")
        continue
    elif(str(guess1_list[3]) not in ii):
        print("第4个字拼音拼写错误")
        continue
    # print(guess1_list)
    # print(answer)
    tmp_str = ""
    rest_table = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[0][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[1][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[2][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[3][i])
    # print(tmp_str)
    # print(rest_table)
    rest_list = list(rest_table)
# next round
    tmp_str = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        elif(guess1_list[0][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[0][i])
            # # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        elif(guess1_list[1][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[1][i])
            # # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        elif(guess1_list[2][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[2][i])
            # # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        elif(guess1_list[3][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[3][i])
            # # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str)

    break

while True:
    guess1 = raw_input("guess2:\n")
    guess1_list = guess1.split(" ")
    if(len(guess1_list) != 4):
        print("成语长度错误")
        continue
    elif(len(guess1_list[0])) != count1:
        print("第1个字拼音长度错误")
        continue
    elif(len(guess1_list[1])) != count2:
        print("第2个字拼音长度错误")
        continue    
    elif(len(guess1_list[2])) != count3:
        print("第3个字拼音长度错误")
        continue
    elif(len(guess1_list[3])) != count4:
        print("第4个字拼音长度错误")
        continue
    elif(str(guess1_list[0]) not in ii):
        print("第1个字拼音拼写错误")
        continue
    elif(str(guess1_list[1]) not in ii):
        print("第2个字拼音拼写错误")
        continue
    elif(str(guess1_list[2]) not in ii):
        print("第3个字拼音拼写错误")
        continue
    elif(str(guess1_list[3]) not in ii):
        print("第4个字拼音拼写错误")
        continue
    # print(guess1_list)
    # print(answer)
    tmp_str = ""
    rest_table = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[0][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[1][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[2][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[3][i])
    # print(tmp_str)
    # print(rest_table)
    rest_list = list(rest_table)
# next round
    tmp_str = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        elif(guess1_list[0][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[0][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        elif(guess1_list[1][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[1][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        elif(guess1_list[2][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[2][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        elif(guess1_list[3][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[3][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str)

    break

while True:
    guess1 = raw_input("guess3:\n")
    guess1_list = guess1.split(" ")
    if(len(guess1_list) != 4):
        print("成语长度错误")
        continue
    elif(len(guess1_list[0])) != count1:
        print("第1个字拼音长度错误")
        continue
    elif(len(guess1_list[1])) != count2:
        print("第2个字拼音长度错误")
        continue    
    elif(len(guess1_list[2])) != count3:
        print("第3个字拼音长度错误")
        continue
    elif(len(guess1_list[3])) != count4:
        print("第4个字拼音长度错误")
        continue
    elif(str(guess1_list[0]) not in ii):
        print("第1个字拼音拼写错误")
        continue
    elif(str(guess1_list[1]) not in ii):
        print("第2个字拼音拼写错误")
        continue
    elif(str(guess1_list[2]) not in ii):
        print("第3个字拼音拼写错误")
        continue
    elif(str(guess1_list[3]) not in ii):
        print("第4个字拼音拼写错误")
        continue
    # print(guess1_list)
    # print(answer)
    tmp_str = ""
    rest_table = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[0][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[1][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[2][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[3][i])
    # print(tmp_str)
    # print(rest_table)
    rest_list = list(rest_table)
# next round
    tmp_str = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        elif(guess1_list[0][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[0][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        elif(guess1_list[1][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[1][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        elif(guess1_list[2][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[2][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        elif(guess1_list[3][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[3][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str)

    break

while True:
    guess1 = raw_input("guess4:\n")
    guess1_list = guess1.split(" ")
    if(len(guess1_list) != 4):
        print("成语长度错误")
        continue
    elif(len(guess1_list[0])) != count1:
        print("第1个字拼音长度错误")
        continue
    elif(len(guess1_list[1])) != count2:
        print("第2个字拼音长度错误")
        continue    
    elif(len(guess1_list[2])) != count3:
        print("第3个字拼音长度错误")
        continue
    elif(len(guess1_list[3])) != count4:
        print("第4个字拼音长度错误")
        continue
    elif(str(guess1_list[0]) not in ii):
        print("第1个字拼音拼写错误")
        continue
    elif(str(guess1_list[1]) not in ii):
        print("第2个字拼音拼写错误")
        continue
    elif(str(guess1_list[2]) not in ii):
        print("第3个字拼音拼写错误")
        continue
    elif(str(guess1_list[3]) not in ii):
        print("第4个字拼音拼写错误")
        continue
    # print(guess1_list)
    # print(answer)
    tmp_str = ""
    rest_table = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[0][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[1][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[2][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[3][i])
    # print(tmp_str)
    # print(rest_table)
    rest_list = list(rest_table)
# next round
    tmp_str = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        elif(guess1_list[0][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[0][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        elif(guess1_list[1][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[1][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        elif(guess1_list[2][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[2][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        elif(guess1_list[3][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[3][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str)

    break

while True:
    guess1 = raw_input("guess5:\n")
    guess1_list = guess1.split(" ")
    if(len(guess1_list) != 4):
        print("成语长度错误")
        continue
    elif(len(guess1_list[0])) != count1:
        print("第1个字拼音长度错误")
        continue
    elif(len(guess1_list[1])) != count2:
        print("第2个字拼音长度错误")
        continue    
    elif(len(guess1_list[2])) != count3:
        print("第3个字拼音长度错误")
        continue
    elif(len(guess1_list[3])) != count4:
        print("第4个字拼音长度错误")
        continue
    elif(str(guess1_list[0]) not in ii):
        print("第1个字拼音拼写错误")
        continue
    elif(str(guess1_list[1]) not in ii):
        print("第2个字拼音拼写错误")
        continue
    elif(str(guess1_list[2]) not in ii):
        print("第3个字拼音拼写错误")
        continue
    elif(str(guess1_list[3]) not in ii):
        print("第4个字拼音拼写错误")
        continue
    # print(guess1_list)
    # print(answer)
    tmp_str = ""
    rest_table = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[0][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[1][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[2][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[3][i])
    # print(tmp_str)
    # print(rest_table)
    rest_list = list(rest_table)
# next round
    tmp_str = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        elif(guess1_list[0][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[0][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        elif(guess1_list[1][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[1][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        elif(guess1_list[2][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[2][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        elif(guess1_list[3][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[3][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str)

    break

while True:
    guess1 = raw_input("guess6:\n")
    guess1_list = guess1.split(" ")
    if(len(guess1_list) != 4):
        print("成语长度错误")
        continue
    elif(len(guess1_list[0])) != count1:
        print("第1个字拼音长度错误")
        continue
    elif(len(guess1_list[1])) != count2:
        print("第2个字拼音长度错误")
        continue    
    elif(len(guess1_list[2])) != count3:
        print("第3个字拼音长度错误")
        continue
    elif(len(guess1_list[3])) != count4:
        print("第4个字拼音长度错误")
        continue
    elif(str(guess1_list[0]) not in ii):
        print("第1个字拼音拼写错误")
        continue
    elif(str(guess1_list[1]) not in ii):
        print("第2个字拼音拼写错误")
        continue
    elif(str(guess1_list[2]) not in ii):
        print("第3个字拼音拼写错误")
        continue
    elif(str(guess1_list[3]) not in ii):
        print("第4个字拼音拼写错误")
        continue
    # print(guess1_list)
    # print(answer)
    tmp_str = ""
    rest_table = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[0][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[1][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[2][i])
    # print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        else:
            tmp_str+=("0")
            rest_table+=str(answer[3][i])
    # print(tmp_str)
    # print(rest_table)
    rest_list = list(rest_table)
# next round
    tmp_str = ""
    for i in range(count1):
        if(answer[0][i] == guess1_list[0][i]):
            tmp_str+=str("1")
        elif(guess1_list[0][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[0][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count2):
        if(answer[1][i] == guess1_list[1][i]):
            tmp_str+=str("1")
        elif(guess1_list[1][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[1][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count3):
        if(answer[2][i] == guess1_list[2][i]):
            tmp_str+=str("1")
        elif(guess1_list[2][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[2][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str),
    tmp_str = ""
    for i in range(count4):
        if(answer[3][i] == guess1_list[3][i]):
            tmp_str+=str("1")
        elif(guess1_list[3][i] not in rest_list):
            tmp_str+=("0")
        else:
            rest_list.remove(guess1_list[3][i])
            # print(rest_list)
            tmp_str+=str("2")
    print(tmp_str)

    break

