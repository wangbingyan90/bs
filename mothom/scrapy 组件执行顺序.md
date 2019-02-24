初始化的顺序是 Extension、Download Middleware、Spider Middleware、Item Pipeline。

控件接收signal的顺序也是 Extension、Download Middleware、Spider Middleware、Item Pipeline

默认scrapy遵守robot协议

在setting改变ROBOTSTXT_OBEY为False，让scrapy不遵守robot协议