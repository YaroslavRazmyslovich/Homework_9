import click
import random 
from enum import Enum


@click.command()
@click.argument ('toy')
def toy (toy):
    class Color (Enum):
        a = 'yellow'
        b = 'orange'
        c = 'blue'
        d = 'grey'
        e = 'red'
        f = 'black'
    color = random.choice (list(Color)).value
    class Toys (Enum):
        a = 'star'
        b = 'angel'
        c = 'candy cane'
        d = 'bell'
        e = 'ball'
    toy = random.choice (list(Toys)).value    
    print (color, toy)


if __name__ == '__main__':
    toy()

# python task_2.py toy
