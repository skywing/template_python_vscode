import ctypes

while 1:
    print('App is in pause mode. Ctrl+C to exit.')
    ctypes.CDLL(None).pause()
