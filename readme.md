# Run

## windows

```
pip install -r requirements.txt
python run.py
```

## linux

```
pip3 install -r requirements.txt
gunicorn run:app
```

## tests

| **route**      | **get** | **post** | **delete** | **patch** |
|----------------|:-------:|:--------:|:----------:|:---------:|
| **register**   |    x    |  success |      x     |     x     |
| **login**      |    x    |  success |      x     |     x     |
| **meta**       | success |  success |   success  |  success  |
| **characters** | success |  success |   success  |  success  |
| **dictionary** | success |  success |   success  |  success  |
| **weapons**    | success |  success |   success  |  success  |
| **wishes**     | success |  success |   success  |  success  |

### TODO
- add create relationship for wishes and characters in post and patch
- add get relationship for wishes and characters in get