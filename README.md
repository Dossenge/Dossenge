# Dossenge - 一个包含很常用功能的Python库


## 项目介绍
Dossenge 是一个为 Python 开发者设计的实用工具库，旨在提供一些常用的功能，帮助开发者快速解决问题。这个库特别适合初学者和需要快速实现某些功能的开发者。

## 主模块

### 方法列表

**引入方法：**
`from Dossenge import Dossenge as Dossenge`或`from Dossenge.Dossenge import *`

**方法列表：**
```python
Dossenge.equal(x, y, roundnum=3) # 判断x与y的差是否小于10**-roundnum（精度影响，可自行设置精度）
Dossenge.chicken_rabbit(head, foot) # 计算鸡兔同笼问题，head个头，foot条腿 返回[(chicken,rabbit)]
Dossenge.fibonacci(number) #计算斐波那契数列的第number项
```

## 字符串处理

**引入Dossenge.string方法：**
`from Dossenge import string`或`from Dossenge.string import *`

**方法列表：**
```python
Dossenge.string.String # 类： 目前没有用处，敬请期待
Dossenge.string.countstr(string) # 以字典形式返回字符串中字符的个数
Dossenge.string.save_add(filepath,string) # 往filepath文件中增加写入string然后返回新的内容
```

## HTTP 请求

**引入方法：** `from Dossenge.http import *`

**方法列表：**
```python
Dossenge.http.header_request(url, **headers) # 发送带有自定义请求头的 HTTP 请求
```

**示例：**

```python
from Dossenge.http import header_request

# 自定义请求头
headers = {
    "User-Agent": "MyApp/1.0",
    "Authorization": "Bearer mytoken",
    "Accept": "application/json"
}

# 发送请求
response = header_request("https://api.example.com/data", **headers)

# 打印响应内容
if response:
    print(response.json())
	
```
## 可执行文件
```bash
dossenge equal 0.1+0.2 0.3 5
```
判断x与y的差是否小于10\*\*-5

```bash
dossenge cr head foot
```
解决鸡兔同笼问题

*配置文件：（已弃用）*
*config.toml*
*lang 文件名*
*path 文件路径*
*ext 扩展名*

*可自定义语言包（已弃用）*
*格式为*
*"*
*判断两数是否相等*
*解决鸡兔同笼问题*
*"*
