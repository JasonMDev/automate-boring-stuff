try:
    float("hello")
except Exception as exc:
    print(type(exc))

# <class 'ValueError'>