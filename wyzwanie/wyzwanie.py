from inspect import isfunction

__all__ = ['Wyzwanie']


class Wyzwanie:  # TODO singleton?
    def __init__(self, exercise_id=None, difficulty=None, **kwargs):
        self._validate_init_args(exercise_id, difficulty)
        self._exercise_id = exercise_id
        self._exercise_difficulty = difficulty

    def _validate_init_args(self, exercise_id, difficulty):
        if not exercise_id or not difficulty:
            raise ValueError('Both exercise id and difficulty have to be specified')
        try:
            difficulty = difficulty.lower()
        except AttributeError:
            raise TypeError('Difficulty has to be one of ("easy", "hard")')
        if difficulty not in ('easy', 'hard'):
            raise TypeError('Difficulty has to be one of ("easy", "hard")')

    def main_function(self, func):
        self._validate_main_function(func)
        self._main_function = func
        return func

    def _validate_main_function(self, f):
        if not isfunction(f):
            raise TypeError('Wyzwanie.main_function has to be used as a function decorator')

    def run(self):
        pass
