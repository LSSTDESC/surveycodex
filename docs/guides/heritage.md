# Extend galcheat objects

## Frozen dataclasses

The goal of galcheat is to provide a **sourced reference** for survey parameters. Therefore the `Survey` and `Filter` objects have been implemented as frozen dataclasses. This means that trying to modify the attributes of an instance of a `Survey` or a `Filter` will raise a `FrozenInstanceError`.

Nevertheless, one might possibly want to modify or extend the instances of the dataclasses found in galcheat for specific purposes. This can be achieved through inheritance.

## Inheritance

A frozen dataclass creates a class for which the call to the `__setattr__` method raises a `FrozenInstanceError`. A short way to bypass that feature is to inherit from the main class and modify the `__setattr__` method to recover its classic behavior.

```python
class ExtensibleSurvey(Survey):
     def __setattr__(self, x, val):
         self.__dict__[x] = val
```

The `ExtensibleSurvey` will behave just as the galcheat `Survey` and will be extendable or modifiable. This is also true for the `Filter` class.

!!! warning "To be used at you own risk"
