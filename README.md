# SI-UKKW-SIWP2005_OOP_2024 Object-Oriented Programming

> <img width="20" height="20" src="https://img.icons8.com/fluency/48/writer-male.png" alt="writer-male"/> *Hendrik Tampubolon*
> <img width="20" height="20" src="https://img.icons8.com/nolan/64/new-post.png" alt="new-post"/> <a href="mailto:hendrik.gian@gmail.com">Reach Me!</a>
 
![header](asset/header.png)


## Overview
> "Effective software development begins with a robust design. Object-oriented design serves as a blueprint for developers to conceptualize applications before writing any code, facilitating the breakdown of ideas into reusability and mantainable code which through **F**unctionality, **U**sability,**R**eliability, **P**erformances, and **S**upportability **(FURPS)** analysis.  This course is dedicated to mastering the foundational principles of object-oriented design, delivered in an engaging and interactive manner to accelerate your learning process. This Course (SIWP2005) will cover an introduction to OOP Princples including objects, classes, *Abstraction, Polymorphism, Inheritance,and Encapsulation* **(APIE)**. Beside, a practical hand-on will be introduced in Python & Javascript. In addition, FURPS requirements and analysis will be delivered with *Universal Modeling Language(**UML**)* such as use cases diagram and class diagram. 

## Learning Objectives
- understanding the idea of object-oriented programming design and its terminology 
- understanding on how to implement OOP in python
- able to build your own python package
- able to develop endpoint REST API

## SIWP2005_PBO Course Roadmaps

```mermaid
gantt
    title Roadmaps
    dateFormat YYYY-MM-DD
    Section Part I 
        Object-Oriented Fundamentals :a1, 2024-02-15, 35d
    Section Part II
        Practical OOP with Python :b1, 2024-02-29, 59d
    Section Mid-Term Exam
        UTS :ut, 2024-04-25, 1d
    Section Part III
        Build Python Package Project :c1, 2024-04-25, 35d
    Section Part IV
        Build REST API Endpoint with Flask :d1, 2024-04-25, 49d
    Section Final Project
        UAS :us, 2024-06-14, 1d
```


## Part I Object-Oriented Fundamentals
```mermaid
journey
    title Part I: Object-Oriented Fundamentals
    section Object-Oriented Fundamentals    
        Object-oriented Thinking: 5: Learning
        Objects: 3: Learning
        Classes: 3: Learning
        Instance Methods & Attributes: 3: Learning
        Class Methods & Members: 3: Learning
        APIE: 4: Learning
        Analysis & Design :4: Learning
        UML: 3: Learning
```


### Object-Oriented Thinking
> seeing everything is an object

***Fun fact
> Did you know that everything in Python is an object?
> Indeed!, all data types, structures, functions and classes are treated as objects. event Null, None is a type of object. Hence,  makes it very flexible

### Objects and Classes
- Classes:
    - one of the building-blocks of Object-Oriented Programming that acts as a ***Blueprint*** where the *data* and the *actions* of the *objects* are defined
    
- Instance:
    - a concrete object that is created from the class ***Blueprint***
- Methods:
    - an “action” defined in the class that the instances of
        the class can perform. 
- Object:
    - a concrete instance of a class stored in memory


- More about Methods, Attributes, and Members

### The Fourth of APIE Components 
> 

```mermaid
    mindmap
    APIE
        Abstraction
          Key Points
             Focuses on the 'what' rather than the 'how'
             Allows users to interact with objects without needing to understand their internal complexities
        Polymorphism
            Key Points
                Enables methods to do different things based on the object that they are acting upon.
                Enhances code reusability and flexibility
        Inheritance
            Key Points
                Establishes an "is-a" relationship between classes
                Subclasses can extend or override behavior of the superclass
        Encapsulation
            Key Points
                Protects data from unauthorized access
                Enhances maintainability by localizing changes
```
### FURPS Analysis and Design
> FURPS is crucial step when developed a well-structured, reusable, and maintainable software into end product. 

```mermaid
    mindmap
    FURPS
        Functionality
          Capability
          Reusability
          Security
        Usability
            Human Factors
            Consistency
            Documentation
        Reliability
            Availability
            Failure Rate & Duration
            Predictability            
        Performance
            Speed
            Efficiency
            Resource Consumption
            Scalability
        Supportability
            Testability
            Extensibility
            Serviceability
            Configurability             
```

### Converted all into Use Case and Class Diagram with UML
> In this section, we only cover a short introduction to UML, how to prepare requirement analysis, provide a simple use case diagram, then translate it into Class Diagram. 

- Use Case Diagram

- Class Diagram


## Part II: Practical OOP with Python

```mermaid
journey
    title Hands-on
    section Object-Oriented Programing in Python    
        Revisited Python Data Types: 3: Coding
        Class and Object: 3: Coding
        Abstraction: 3: Coding
        Polymorhpism: 3: Coding
        Inheritance: 3: Coding
        Encapsulation: 3: Coding
        Memory Handling: 3: Coding
```

### Revisited Python Data Types
- Integers (int): Used for whole numbers.

```python!
x = 10
print(x)
print(type(x))

```

- Floating Point Numbers (float): Used for decimal numbers.
```python
y = 10.5
print(y)
print(type(y))

```
- Strings (str): Used for sequences of characters.
```python
name = "Katerine"
print(name)
print(type(name))

```

- Booleans (bool): Used for true/false values.

```python
is_active = True
print(is_active)
print(type(is_active))

```

- Lists: Used for ordered sequences of values.

```python
courses = ["OOP", "Intro to Programing", "Data Structure", "Data Science"]
print(courses)
print(type(courses))


```

- Tuples: Similar to lists, but immutable.

```python
coordinates = (10, 20)
print(coordinates)
print(type(coordinates))
```

- Sets: Used for unordered collections of unique elements.

```python
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # Duplicates will be removed
print(type(unique_numbers))

```

- Dictionaries (dict): Used for unordered collections of key-value pairs.
```python
siswa = {"nama": "KATHERIN", "nim": 4x2023xxx, "enrolled": siwp2005}
print(siswa)
print(type(siswa))

```


> Note:
> HW#1 and HW2 will be posted on UVC, stay tuned!

## From Mid-Term ~ Final Project

## Part III: Build Your Very First Python Package
```mermaid
journey
    title Build Your Very First Python Package
    section Build Your Very First Python Package     
        Step 1 FURPS Analysis Plan Your Package : 3: Coding
        Step 2 Creating the package structure : 3: Coding
        Step 3 Creating test directory : 3: Coding
        Step 4 Setup : 3: Coding
        Step 5 Build & Distribute Your Package : 3: Coding
        Step 6 Creating Docs & README.md : 3: Coding
```
> HW#3 will be posted on UVC, stay tuned!

## Part IV: Build REST API Endpoint with Flask

```mermaid
journey
    title Build REST API Endpoint with Flask
    section Flask Framework at the glances
        Environmet-Setup-Prerequisite : 3: Coding
        Quick Start : 3: Coding
        Modular-Object-Class : 3: Coding
        DB : 3: Coding
        REST API : 3: Coding
```
