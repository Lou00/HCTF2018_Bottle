#   Bottle 
> 这题改的非常艰辛，bot老挂，为了方(fang)便(zhi)运(bei)维(da)甚至改了题目，tcl
> hint1 */3 */10
> hint2 firefox 

## payload
```
http://bottle.hctf.2018.io/path?path=http://bottle.hctf.2018.io:0/%0a%0d%0a%0d<script>alert `1` </script>`
```
一个clrf头注入,当端口小与80时firefox会跳转
![-w416](media/15420333517622/15420392256228.jpg)
![-w416](media/15420333517622/15420392645478.jpg)
利用这个特性使其加载js达到xss
## 正解
应该都会发现有csp,改题之后csp直接在location下面
其实如果是原题的话csp基本是在location上面
hint1 是  */3 */10
这是服务器重启的两个时间
如果用过bottle的话，可能会发现bottle每次重启时响应头顺序可能会变化
为了防止非预期(非预期已经变成正解,o(╥﹏╥)o)人为干预成功率
*/3 为csp在上面location在下面的服务重启时间
*/10 为csp在下面location在上面的服务重启时间
算一下一小时也就6分钟能xss
所以正解是要在指定时间内进行xss
或者写个脚本什么的
## 题目
题目已经搭好原题的环境，求轻喷

