# import ssl
#
#
# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
# ssl_context.load_cert_chain(certfile='newcert.pem', keyfile='newkey.pem', password='secret')

_RUN_SETTING = {
    'host':'0.0.0.0',
    'port':5555,
#     'ssl_context':ssl_context
}

_MONGO_SETTING = {
    'db':'ReServeTest',
    'host':'127.0.0.1',
    'port':27017
}