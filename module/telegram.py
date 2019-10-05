import module.database_wrapper as database_wrapper
from contextlib import contextmanager

def search_picture(picture):
    pass

class User(object):
    def __init__(self, uid):
        self.uid = str(uid)
        try:
            userdata = self.read_user()
        except:
            self._premium = False
            self.update_user()
        else:
            self._premium = userdata[0]

    @property
    def premium(self):
        return self._premium
    @premium.setter
    def _(self, value):
        self._premium = value

    def update_user(self):
        database_wrapper.writefile("users.json", self.uid, [self._premium])

    def read_user(self):
        user = database_wrapper.readfile("users.json")[self.uid]
        return user

if __name__ == "__main__":
    u = User(123)
    print(u.premium)