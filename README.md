# 智慧青科大健康打卡腾讯云版

### 下载
```
git clone https://github.com/crazy-zxx/HealthRecordCloud.git
```
或者直接 code --> Download Zip ，然后解压

### 使用

#### 配置

```
# 进入目录，直接下载的解压后文件夹名字可能是HealthRecord-master
cd HealthRecordCloud
```
修改main.py中的用户名密码
```
# ------------------  只需要在此处设置你的智慧青科大账号和密码即可   ------------------------
# 用户名
un = '4021110075'
# 密码
pd = '12345678qwer'
```
修改sendEmail.py的邮箱配置
```
# 使用第三方 SMTP 服务（请自行参照邮箱厂商提供信息修改）
# 以QQ为例
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1934109821@qq.com"  # 用户名（你的QQ账号@qq.com）
mail_pass = "qwertyuiopasdfgh"  # 口令（先要开启SMTP，口令是16位字母）

# 发件人邮箱
sender = '1934109821@qq.com'
# 收件人邮箱(设置为自己接受邮件通知的邮箱)
receivers = ['1934109821@qq.com']
```

#### 环境搭建
[点击进入腾讯云函数服务官网](https://cloud.tencent.com/product/scf)
直接QQ登录，右上角进控制台


### 声明
对于用户使用该项目可能造成的不良后果，本人概不负责！！！