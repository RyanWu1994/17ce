
#17ce 多組domain網路品質監控


database name : 17CE


table name : main_information
column definition :
    URL 網址 char
    時間    date	datetime
    線路    line	char
    最快節點	Fastest node    float
    最快節點秒數	Fastest node seconds    float
    最慢節點	Slowest node    float
    最慢節點秒數	Slowest node seconds    float
    平均響應    Average response    float

table name : node_information
column definition :
    URL 網址 char
    時間    date	datetime
    监测点
    ISP
    省份
    解析IP
    解析IP所在地
    Http状态
    总时间
    解析时间
    连接时间	
    下载时间
    首字节时间
    文件大小
    下载大小
    下载速度	
