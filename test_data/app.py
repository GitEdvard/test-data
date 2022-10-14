from importlib.resources import files


def start():
    contents = files('test_data').joinpath('data.csv').read_text()
    print(contents)
    # print("hello")
