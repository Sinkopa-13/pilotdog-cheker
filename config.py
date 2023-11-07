#то что ниже обязательно заполнить своими данными
proxy_use = 0 #  0 - не использовать, 1 - ротируемый прокси
proxy_login = 'pfd56464'
proxy_password = '9caa07'
proxy_address = 'noroxy.com'
proxy_port = '107'

amount_wallets_in_batch = 5

#то что ниже можно менять только если понимаешь что делаешь
proxies = { 'all': f'http://{proxy_login}:{proxy_password}@{proxy_address}:{proxy_port}',}
if proxy_use:
    request_kwargs = {"proxies":proxies, "timeout": 1200}
else:
    request_kwargs = {"timeout": 120}

