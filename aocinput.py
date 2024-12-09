import requests,os
class AOCInput:
    def __init__(self,year,day,actual=True):
        self.year = year
        self.day = day
        self.url = f'https://adventofcode.com/{year}/day/{day}/input'
        self.actual = actual

    def lines(self):
        if not self.actual:
            f = open('../input','r')
            for line in f:
                yield line.strip()
        else:
            response = requests.get(self.url, headers={'Cookie': f'{os.getenv('AOC_COOKIE')}'})
            if response.status_code != 200:
                raise ConnectionError('Something went wrong getting input.')

            for line in response.iter_lines(decode_unicode=True):
                yield line.strip()