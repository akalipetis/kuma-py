# kuma-py

Python wrapper for Kuma; the Django app behind MDN

## Usage

    import kuma
    
    client = kuma.Client()
    web_api = kuma.client.docs.web.api
    
    print web_api.window.summary
    
    for child in web_api.children()['subpages']:
        print child['title']
