import click

@click.group
def my_command_group():
    pass

@my_command_group.command()
@click.argument("count", type=click.INT)
def say_testing(count):
    for i in range(count):
        print("Testing!")


