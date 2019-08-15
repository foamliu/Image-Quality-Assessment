import os

from brisque import BRISQUE

if __name__ == "__main__":
    brisque = BRISQUE()
    print('good:')
    good_folder = 'images/good'
    files = [file for file in os.listdir(good_folder) if file.endswith('.jpg')]
    for file in files:
        path = os.path.join(good_folder, file)
        score = brisque.get_score(path)
        print(score)

    print('bad:')
    bad_folder = 'images/bad'
    files = [file for file in os.listdir(bad_folder) if file.endswith('.jpg')]
    for file in files:
        path = os.path.join(bad_folder, file)
        score = brisque.get_score(path)
        print(score)
