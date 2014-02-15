# kuma-py

Python wrapper for Kuma; the Django app behind MDN

## Usage

    import kuma
    
    client = kuma.Client()
    web_api = client.docs.web.api
    
    for page in web_api.subpages:
        print '%s\n%s\n' % (page, page.summary)
