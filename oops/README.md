day 1 


Leo AI: # Object-Oriented Programming (OOP) - Summary Notes

## What is OOP?
- A programming approach that organizes code around **objects** (real-world entities) rather than just functions and data
- Objects have **attributes** (properties) and **methods** (behaviors)

---

## Object = Attributes + Methods
| Term | Meaning | Example |
|------|---------|---------|
| **Attributes/Properties** | What an object *has* | Human → height, weight, gender |
| **Methods/Behaviors** | What an object *can do* | Human → walk, sing, dance |

---

## Procedural vs OOP

| Procedural | OOP |
|-----------|-----|
| Just functions + variables mixed together | Data + functions bundled into objects |
| Gets messy with 1000s of functions ("noodle code") | Clean, organized, modular |
| Hard to manage large projects | Easy collaboration between teams |

---

## Class vs Object
- **Class** = Blueprint/Template (e.g., exam question paper format)
- **Object** = Instance created from that class (e.g., actual question papers Q1, Q2, Q3)

```python
class Human:
    pass

chanadan = Human()  # Object
darshan = Human()   # Object
```

---

## Key Benefits of OOP
- ✅ **Modularity** – Code split into separate modules
- ✅ **Code Reusability** – Use inheritance to reuse existing class features
- ✅ **Encapsulation** – Car functions stay inside Car object; Human functions stay inside Human object

---

## Simple Code Example
```python
class Human:
    def __init__(self, name):
        self.name = name      # Attribute

    def walk(self):           # Method
        print(self.name + " is walking")

chanadan = Human("Chanadan")
chanadan.walk()  # Output: Chanadan is walking
```

---

## 4 Key Terms to Remember
1. **Class** – Blueprint/template
2. **Object** – Instance of a class
3. **Attribute** – Property/variable of an object
4. **Method** – Function inside a class