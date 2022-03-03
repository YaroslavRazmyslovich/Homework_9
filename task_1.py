import click
from datetime import datetime

day = (datetime (2022, 12, 31, 23, 59, 59) - datetime.now ()).days
hour = datetime (2022, 12, 31, 23, 59, 59).hour - datetime.now ().hour

@click.command()
@click.argument ('newyear')
@click.option ('--hours/--no-hours')
def days (newyear, hours):
    if hours:
        click.echo (f'{day} days, {hour} hours')
    else:
        click.echo (f'{day} days')
        
if __name__ == '__main__':
    days()

# python task_1.py newyear --hours
# python task_1.py newyear
