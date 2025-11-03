import itertools

import pytest

from tests.utils import RunCmdError, run_cli


def test_cli_help() -> None:
    stdout = run_cli("--help")
    assert "Commands:" in stdout


def test_required_option() -> None:
    with pytest.raises(RunCmdError) as e:
        run_cli("greet")
        assert "Missing option '--name'" in str(e.value)


def test_option_with_default() -> None:
    stdout = run_cli("greet --name John")
    assert "John" in stdout
    assert "USA" in stdout


@pytest.mark.parametrize(
    "name,birth_place", itertools.product(["Alice", "Bob"], ["UK", "Germany"])
)
def test_option_with_value(name: str, birth_place: str) -> None:
    stdout = run_cli(f"greet --name {name} -b {birth_place}")
    assert name in stdout
    assert birth_place in stdout


@pytest.mark.parametrize("count", [1, 2, 3])
def test_verbose(count: int) -> None:
    vee = "v" * count
    _, stderr = run_cli(f"greet --name John -{vee}", stderr=True)

    num_of_lines = stderr.strip().split("\n")
    assert len(num_of_lines) == count


def test_command_with_arg_validation() -> None:
    with pytest.raises(RunCmdError) as e:
        run_cli("copy")
    assert "Error: Missing argument" in e.value.stderr, e.value.stderr
