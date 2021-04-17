from types import SimpleNamespace, MethodType


class ConstantNamespace(SimpleNamespace):
    """
    This method is an extension of the SimpleNamespace class and should be used
    only for storing constants (variables written with upper case) through
    creating a new class based on this.

    Example:
    ```
    class MyNs(ConstantNamespace):
        CONST1 = "My Constant"
        CONST2 = 3.14
    ```

    Creating instance of the class will retur n a dictionary with specified
    variables

    Example: MyNs() will return a dictionary:
        {'CONST1': 'My Constant', 'CONST2': 3.14}
    """
    def __new__(cls):
        return cls._get_dictionary()

    @classmethod
    def _get_dictionary(cls) -> dict:
        d = {}
        for attr_name in cls.__dict__.keys():
            attr = getattr(cls, attr_name)
            if attr_name.isupper():
                if not isinstance(attr, MethodType):
                    d[attr_name] = attr
        return d

    @classmethod
    def get_const_with_val(cls, value) -> dict:
        """
        Returns dictionary of constants with the specified value

        :param value: Value of a constant
        :return: Dictionary of constants with the specified value
        :rtype: dict or None
        """
        d = {key: value for key, value in cls._get_dictionary().items() if value == value}
        if not len(d):
            return None
        return d

    @classmethod
    def contains(cls, value: str) -> bool:
        """
        Checks if the namespace contains a variable with value.

        :param value: Value
        :type value: str
        :return: Result of the check
        :rtype: bool
        """
        return value in list(cls._get_dictionary().values())

    @classmethod
    def contains_const(cls, name: str) -> bool:
        """
        Checks if the namespace contains a variable with value.

        :param value: Name of a constant
        :type name: str
        :return: Result of the check
        :rtype: bool
        """
        return name in list(cls._get_dictionary().keys())
