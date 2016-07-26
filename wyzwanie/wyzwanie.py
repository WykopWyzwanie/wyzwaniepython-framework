from inspect import isfunction

import requests

__all__ = ['Wyzwanie']


class Wyzwanie:  # TODO singleton?
    config_url = None

    def __init__(self, exercise_id=None, difficulty=None, python_version=3, **kwargs):
        self._validate_init_args(exercise_id, difficulty, python_version)
        self._exercise_id = exercise_id
        self._exercise_difficulty = difficulty

    def _validate_init_args(self, exercise_id, difficulty, python_version):
        if not exercise_id or not difficulty:
            raise ValueError('Both exercise id and difficulty have to be specified')
        try:
            difficulty = difficulty.lower()
        except AttributeError:
            raise TypeError('Difficulty has to be one of ("easy", "hard")')
        if difficulty not in ('easy', 'hard'):
            raise TypeError('Difficulty has to be one of ("easy", "hard")')
        if python_version not in (2, 3):
            raise ValueError('Python version has to be one of (2, 3)')

    def main_function(self, func):
        self._validate_main_function(func)
        self._main_function = func
        return func

    def _validate_main_function(self, f):
        if not isfunction(f):
            raise TypeError('Wyzwanie.main_function has to be used as a function decorator')

    def run(self):
        self._config = self._get_config_file()
        args = self._get_cli_arguments()
        pass

    def _get_cli_arguments(self):
        pass

    def _get_config_file(self):
        return requests.get(config_url.format(self._exercise_id)).json()
