#!/usr/bin/python3

import simplejson as json
from simplejson.compat import StringIO


json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(json.dumps("\"foo\bar"))
print(json.dumps(u'\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))


io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()
print(io.getvalue())
print ("\n")

obj = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(obj[0])
print(obj[1])
print ("\n")

io = StringIO('["streaming API"]')
print(io.getvalue())
print ("\n")
