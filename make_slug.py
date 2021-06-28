import re
def make_slug(text):
    pattern = '[^a-zA-Z0-9\s]'
    slug = re.sub(pattern, '', text)
    slug = re.sub('\s', '-', slug.strip())
    slug = re.sub('-{2,}', '-', slug)
    return slug
   
print(make_slug("hello world"))
print(make_slug("hello  world!"))
print(make_slug(" --hello-  world--"))
    
    
