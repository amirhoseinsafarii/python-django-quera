class Proxy:
    def __init__(self, obj: object) -> None:
        self._obj = obj
        self._last_accessed = None
        self._access_counts = {}

    def last_accessed_attribute(self) -> str:
        if self._last_accessed == None:
            raise Exception("No attribute was accessed.")
        return self._last_accessed

    def count_of_accesses(self, attribute_name: str) -> int:
        if (
            not hasattr(self._obj, attribute_name)
            or not attribute_name in self._access_counts
        ):
            return 0
        return self._access_counts[attribute_name]

    def was_accessed(self, attribute_name: str) -> bool:
        if (
            not hasattr(self._obj, attribute_name)
            or not attribute_name in self._access_counts
        ):
            return False
        if attribute_name in self._access_counts:
            return True

    def __getattr__(self, attr):

        if not hasattr(self._obj, attr):
            raise Exception("No such attribute.")
        self._last_accessed = attr
        self._access_counts[attr] = self._access_counts.get(attr, 0) + 1

        return getattr(self._obj, attr)


class Radio:
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel

    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on

    def __str__(self):
        return (
            f"Radio(channel={self._channel}, is_on={self.is_on}, volume={self.volume})"
        )


radio = Radio()
radio_proxy = Proxy(radio)
radio_proxy.set_channel(95)
radio_proxy.power()
radio_proxy.set_channel(100)
print(radio_proxy.is_on)  # True
print(radio_proxy.last_accessed_attribute())  # is_on
print(radio_proxy.count_of_accesses("set_channel"))  # 2
print(radio_proxy.was_accessed("power"))  # True
print(radio_proxy.count_of_accesses("non_existent_method"))  # 0
print(radio_proxy.was_accessed("volume"))
