# Python [Ark](http://ark.com) api

A wrapper for the ark api using requests

If you want to learn more about the api check out their [api_doc](https://github.com/arkcore/api_doc)

## Quickstart

```python
from ark import Ark

ark = Ark('XXXXXXX-XXXX-XXXX-XXXX-XXXXXXX')
print ark.check_token()
print ark.email("email@example.com")
print ark.twitter('handle')
print ark.facebook('fb.url')

```