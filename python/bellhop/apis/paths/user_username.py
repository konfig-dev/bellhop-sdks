from bellhop.paths.user_username.get import ApiForget
from bellhop.paths.user_username.put import ApiForput
from bellhop.paths.user_username.delete import ApiFordelete


class UserUsername(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
