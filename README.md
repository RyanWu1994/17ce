
# 17ce 多組domain網路品質監控


## database name : 17CE


### table name : main_information
* column definition :
   * 網址 URL char
   * 時間    Date	datetime
   * 線路    Line	char
   * 最快節點	Fastest node    float
   * 最快節點秒數	Fastest node seconds    float
   * 最慢節點	Slowest node    float
   * 最慢節點秒數	Slowest node seconds    float
   * 平均響應    Average response    float

### table name : node_information
* column definition :
   * 網址 URL char
   * 時間    Date	datetime 
   * 监测点  Node
   * ISP  ISP
   * 省份   Province
   * 解析IP IP
   * 解析IP所在地 DNS_position
   * Http状态  Ststus
   * 总时间    Total_time
   * 解析时间     Resolution_time
   * 连接时间	   Connection_time
   * 下载时间     Download_time
   * 首字节时间   First_byte_time
   * 文件大小     File_size
   * 下载大小     Download_size
   * 下载速度	   Download_speed

