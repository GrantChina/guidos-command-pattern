from enum import Enum, unique


class StringCommand:
    def do_cmd(self, command: str, data: str) -> str:
        method_name = f"_cmd_{command.lower()}"
        try:
            # See if this class has a method named `method_name`.
            method = getattr(self, method_name)
        except AttributeError:
            raise ValueError(f"{command}") from None

        result = method(data)

        print(f"{method_name}({data}) = {result}")

        return result

    def _cmd_hello(self, data: str) -> str:
        return f"Hello, {data}"

    def _cmd_goodbye(self, data: str) -> str:
        return f"Goodbye, {data}"


@unique
class Command(Enum):
    ADD = 0
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 3


class MathCommand:
    """
    The StringCommand example uses commands passed in as strings but it's good
    to note that any object that has a usable `__str__` or `__repr__` method
    can be used as a command. Or in this case, here's an example of the pattern
    that dispatches commands passed in as an Enum, which has a `.name` property
    """

    def do_cmd(self, command: Command, arg1: int, arg2: int) -> int:
        if not isinstance(command, Command):
            raise TypeError(
                f"command must be a Command enum member, got {type(command).__name__}"
            )

        method_name = "_cmd_" + command.name.lower()

        try:
            method = getattr(self, method_name)
        except AttributeError:
            raise ValueError(f"{command}") from None

        result = method(arg1, arg2)

        print(f"{method_name}({arg1}, {arg2}) = {result}")

        return result

    def _cmd_add(self, arg1: int, arg2: int) -> int:
        return arg1 + arg2

    def _cmd_subtract(self, arg1: int, arg2: int) -> int:
        return arg1 - arg2

    def _cmd_multiply(self, arg1: int, arg2: int) -> int:
        return arg1 * arg2

    # NOTE: _cmd_divide() is deliberately left unimplemented to
    # illustrate raising an exception on an unimplemented command.


if __name__ == "__main__":
    # Instantiate a StringCommand() object and pass it a few commands.
    cmd_handler = StringCommand()
    cmd_handler.do_cmd("Hello", "Alice")
    cmd_handler.do_cmd("Goodbye", "Bob")

    # Now try a string command that hasn't been implemented yet.
    try:
        cmd_handler.do_cmd("Foo", "Carol")
    except ValueError as exc:
        print(f"{exc = }")

    # Instantiate a MathCommand() object and pass it a few commands.
    math_cmd = MathCommand()
    math_cmd.do_cmd(Command.ADD, 6, 3)
    math_cmd.do_cmd(Command.SUBTRACT, 6, 3)
    math_cmd.do_cmd(Command.MULTIPLY, 6, 3)

    # Now try a math command that hasn't been implemented yet.
    try:
        math_cmd.do_cmd(Command.DIVIDE, 6, 3)
    except ValueError as exc:
        print(f"{exc = }")
