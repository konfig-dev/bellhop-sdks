# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from bellhop.paths.user_login import Api

from bellhop.paths import PathValues

path = PathValues.USER_LOGIN