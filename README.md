# wyzwaniepython-framework

Przykład użycia:
```python
from wyzwanie_wykop import Wyzwanie

app = Wyzwanie(2, 'easy', 3)  # numer zadania, poziom trudności, wersja pythona


def add(a, b):
  return a + b


@app.main_function
def sample_function(console_arg1, console_arg2):
  return add(console_arg1, console_arg2)


if __name__ == '__main__':
  app.run()

```
