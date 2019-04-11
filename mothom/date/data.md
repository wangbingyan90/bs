### 数据库设计



新闻表 new
* id
* 来源
* 时间
* 作者
* 内容
* 类型


create database bs;


CREATE TABLE Person 
(
name varchar(20),
Age int
) 

attitudes_count //表态数
comments_count  //评论数
created_at      //status创建时间
id              //微博ID
picture         //图片地址
pictures        //图片介绍
raw_text        //摘要
reposts_count   //转发数
source          //微博来源
text            //微博内容
thumbnail       //缩略图
user            //用户

CREATE TABLE weiboNew{
    attitudes_count int;
    comments_count  int;
    id 
    
}


