# Markdown Cheat Sheet By Sơn Hoàng 
## Italics and Bold
- _Chữ Nghiêng_ : đặt "_" ||| "*" ||| `<em>` hai đầu của văn bản
  `ví dụ:  _chữ nghiêng _`
   
- **Chữ Đậm** : đặt "**" ||| "__" ||| `<strong>` hai đầu văn bản
  `ví dụ: **Chữ Đậm**`
  
## Headers
có tổng cộng 6 size header ứng với số lượng "#"

## Links
- có 2 kiểu link đó là "[]" và "()" dùng cùng nhau
  `[anything]: tên hiển thị link`
  `(link): link thực tế`
  
[**Kết Quả**] để truy cập Github dùng [**_link này_**](https://github.com/sonhoang23)

[**Thực Tế**] `để truy cập Github dùng [**_link này_**](https://github.com/sonhoang23)`
  
- kiểu còn lại là **_link tham chiếu_** :

[**Kết Quả**] ví dụ vào trang [GitHub của Hoàng Sơn][link github Hoàng Sơn]

[link github Hoàng Sơn]: https://github.com/sonhoang23

[**Thực Tế**] \*ví dụ vào trang [GitHub của Hoàng Sơn][link github Hoàng Sơn] <- cái này trùng cái ở dưới -> tham chiếu\*
<p>[link github Hoàng Sơn]: https://github.com/sonhoang23`

## Images
_Có 2 dạng: _
### _Inline Image Link_
cấu trúc: !+[title]+(link ảnh)

<img src="https://scontent-hkg4-1.xx.fbcdn.net/v/t1.6435-9/73372369_130166728404961_4785021647134392320_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=QuX_cS5epBcAX_5drsw&_nc_ht=scontent-hkg4-1.xx&oh=632cd71f9e7a021169dad0ec2c730df0&oe=60CFC508" width="100" height="100">
  
[**Thực Tế:**] ` ![Sơn Hoàng](https://scontent-hkg4-1.xx.fbcdn.net/v/t1.6435-9/73372369_130166728404961_4785021647134392320_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=QuX_cS5epBcAX_5drsw&_nc_ht=scontent-hkg4-1.xx&oh=632cd71f9e7a021169dad0ec2c730df0&oe=60CFC508)` **Cách này có vẻ không resize ảnh được**

### Kiểu tham chiếu
[**Kết Quả:**] ![Sơn Hoàng 1][link avatar]

`[link avatar]: https://scontent-hkg4-1.xx.fbcdn.net/v/t1.6435-9/73372369_130166728404961_4785021647134392320_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=QuX_cS5epBcAX_5drsw&_nc_ht=scontent-hkg4-1.xx&oh=632cd71f9e7a021169dad0ec2c730df0&oe=60CFC508` **Kiểu này chưa tìm thấy cách resize ảnh**
 
## Blockquotes
### Chỉ sử dụng dấu ">" ở đầu một đoạn văn hoặc câu văn nằm riêng biệt
### dùng nhiều dấu ">" với mỗi đoạn/ câu văn để qoute cả nhiều đoạn văn
[**Kết Quả:**] 
> đây là ví dụ nhé các frend
>> cách vào 1 ô nè
>>> cách thêm nè  

[**Thực Tế:**] > đây là ví dụ nhé các frend

## Lists
> 2 loại list là list không thứ tự và list có thứ tự
  list không thứ tự sử dụng bullet points
  list có thứ tự dùng số
### list không thứ tự
Cấu trúc: "*"+"dấu cách"+"tên"
[**Kết Quả:**] 

* con chó
* con meo
* con vịt

[**Thực Tế:**]

`* con chó`

`* con meo`

`* con vịt`

### list có thứ tự
Cấu trúc: "số"+"."+"dấu cách"+"tên"
[**Kết Quả:**] 

1. con chó
2. con meo
3. con vịt

[**Thực Tế:**]

`1. con chó`

`2. con meo`

`3. con vịt`

### kiểu lồng nhau
* con chó
  * con chó con
  * con chó xám
* con mèo
  * con mèo vằn
    * con mèo vằn con  
* con vịt
### kiểu nhiều dòng

1. Crack three eggs over a bowl.

 Now, you're going to want to crack the eggs in such a way that you don't make a mess.

 If you _do_ make a mess, use a towel to clean it up!

2. Pour a gallon of milk into the bowl.

 Basically, take the same guidance as above: don't be messy, but if you are, clean it up!

3. Rub the salmon vigorously with butter.

   By "vigorous," we mean a strictly vertical motion. Julia Child once quipped:
   > Up and down and all around, that's how butter on salmon goes.
4. Drop the salmon into the egg-milk bowl.

   Here are some techniques on salmon-dropping:

   * Make sure no trout or children are present
   * Use both hands
   * Always have a towel nearby in case of messes
  
## Paragraphs
> Các cách để xuống dòng
### Cách ra một dòng
dòng 1

dòng 2

### Dùng _hard break_
> đó là dùng "dấu cách" 2 lần ở chỗ xuống dòng

Do I contradict myself?  
Very well then I contradict myself,  
(I am large, I contain multitudes.)
