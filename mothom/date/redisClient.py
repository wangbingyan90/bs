import redis

r = redis.StrictRedis(host='69.171.79.70', port=6379, db=0)
r.set('foo', 'bar')
print(r.get('foo'))
 lpush dangdang:start_urls http://book.dangdang.com/ 