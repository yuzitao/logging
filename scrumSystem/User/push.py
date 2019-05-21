import jpush
from jpush import common

_jpush = jpush.JPush('f7b11a3dbd7677d41cd77cdb', '739fd6536b1df8e6eb825934')
push = _jpush.create_push()
# if you set the logging level to "DEBUG",it will show the debug logging.
_jpush.set_logging("DEBUG")
push.audience = jpush.all_
push.notification = jpush.notification(alert="hello python jpush api")
push.platform = jpush.all_
try:
    response=push.send()
except common.Unauthorized:
    raise common.Unauthorized("Unauthorized")
except common.APIConnectionException:
    raise common.APIConnectionException("conn error")
except common.JPushFailure:
    print ("JPushFailure")
except:
    print ("Exception")