"""CLI entrypoint for chatvideo."""

from __future__ import annotations

import click

from chatvideo import __version__


_TREE_PARAM_PURPOSES = {
    "help": "Show CLI help and registered options.",
    "version": "Print the current package version.",
    "show_tree": "Print the registered CLI tree.",
}


def _command_help(command: click.Command) -> str:
    if command.help:
        return command.help.strip().splitlines()[0]
    if command.short_help:
        return command.short_help.strip()
    if command.callback and command.callback.__doc__:
        return command.callback.__doc__.strip().splitlines()[0]
    return ""


def _param_signature(param: click.Parameter) -> str:
    if isinstance(param, click.Option):
        return ", ".join(param.opts)
    return param.name or "<argument>"


def _param_purpose(param: click.Parameter) -> str:
    if param.name in _TREE_PARAM_PURPOSES:
        return _TREE_PARAM_PURPOSES[param.name]
    if isinstance(param, click.Option) and param.help:
        return param.help.rstrip(".") + "."
    return "Command option."


def _tree_line(prefix: str, connector: str, label: str, purpose: str) -> str:
    suffix = f"  # {purpose}" if purpose else ""
    return f"{prefix}{connector}{label}{suffix}"


def _render_command(command: click.Command, name: str, prefix: str = "") -> list[str]:
    rows: list[tuple[str, str]] = []
    rows.append(("--help", _TREE_PARAM_PURPOSES["help"]))
    for param in command.params:
        if getattr(param, "hidden", False):
            continue
        rows.append((_param_signature(param), _param_purpose(param)))

    if isinstance(command, click.Group):
        for child_name in command.list_commands(click.Context(command)):
            child = command.get_command(click.Context(command), child_name)
            if child is None or getattr(child, "hidden", False):
                continue
            rows.append((child_name, _command_help(child)))

    lines: list[str] = []
    for index, (label, purpose) in enumerate(rows):
        last = index == len(rows) - 1
        connector = "└── " if last else "├── "
        lines.append(_tree_line(prefix, connector, label, purpose))
    return lines


def render_command_tree(command: click.Command, name: str = "chatvideo") -> str:
    title = f"{name}  # {_command_help(command)}"
    lines = [title]
    lines.extend(_render_command(command, name))
    return "\n".join(lines)


@click.group(invoke_without_command=True)
@click.version_option(__version__, prog_name="chatvideo")
@click.option("--tree", "show_tree", is_flag=True, is_eager=True, help="Print the registered CLI tree.")
@click.pass_context
def main(ctx: click.Context, show_tree: bool) -> None:
    """ChatVideo command line interface."""
    if show_tree:
        click.echo(render_command_tree(ctx.command, "chatvideo"))
        ctx.exit(0)
    # Real tool commands belong here after they operate on video workflows.


if __name__ == "__main__":
    main()
