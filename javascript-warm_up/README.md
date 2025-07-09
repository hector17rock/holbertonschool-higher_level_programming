# JavaScript Warm-Up

> A comprehensive collection of JavaScript exercises and concepts for beginners, covering fundamental programming constructs, functions, objects, and advanced JavaScript features.

## Author

**Hector** - *Project Developer*

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [Exercises](#exercises)
  - [Basic Exercises (0-13)](#basic-exercises-0-13)
  - [Advanced Exercises (100-103)](#advanced-exercises-100-103)
- [Key Concepts](#key-concepts)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)

## Overview

This directory contains a series of JavaScript exercises designed to introduce fundamental programming concepts and JavaScript-specific features. The exercises progress from basic syntax and variable declarations to more advanced topics like functions, objects, and scope manipulation.

## Learning Objectives

By completing these exercises, you will learn:

- **JavaScript Basics**: Variables, constants, and data types
- **Control Flow**: Conditional statements and loops
- **Functions**: Declaration, parameters, return values, and scope
- **Objects**: Creation, property manipulation, and methods
- **Arrays**: Manipulation and iteration
- **Module System**: Exports and imports
- **Advanced Concepts**: Closures, callbacks, and higher-order functions

## Requirements

- **Node.js**: JavaScript runtime environment
- **Semistandard**: JavaScript linting tool (for some exercises)
- **Ubuntu/Linux**: Primary development environment (compatible with macOS)

## File Structure

```
javascript-warm_up/
├── README.md                    # This file
├── 0-javascript_is_amazing.js   # First constant and console output
├── 1-multi_languages.js         # Multiple console.log statements
├── 2-arguments.js               # Command line argument handling
├── 3-value_argument.js          # First argument processing
├── 4-concat.js                  # String concatenation
├── 5-to_integer.js              # Type conversion (string to integer)
├── 6-multi_languages_loop.js    # Loops and arrays
├── 7-multi_c.js                 # Conditional loops
├── 8-square.js                  # Nested loops for patterns
├── 9-add.js                     # Function definition and usage
├── 10-factorial.js              # Recursive functions
├── 11-second_biggest.js         # Array sorting and manipulation
├── 12-object.js                 # Object property modification
├── 13-add.js                    # Module exports
├── 13-main.js                   # Module imports and testing
├── 100-let_me_const.js          # Advanced: Variable scope
├── 100-main.js                  # Test file for scope exercise
├── 101-call_me_moby.js          # Advanced: Higher-order functions
├── 101-main.js                  # Test file for higher-order functions
├── 102-add_me_maybe.js          # Advanced: Callbacks
├── 102-main.js                  # Test file for callbacks
└── 103-object_fct.js            # Advanced: Dynamic method addition
```

## Exercises

### Basic Exercises (0-13)

#### 0. First constant, first print
**File**: `0-javascript_is_amazing.js`
- **Purpose**: Introduction to constants and console output
- **Concepts**: `const` declaration, `console.log()`
- **Output**: "JavaScript is amazing"

#### 1. 3 languages
**File**: `1-multi_languages.js`
- **Purpose**: Multiple console.log statements
- **Concepts**: Sequential execution, string literals
- **Output**: Three lines about C, Python, and JavaScript

#### 2. Arguments
**File**: `2-arguments.js`
- **Purpose**: Command line argument processing
- **Concepts**: `process.argv`, conditional logic
- **Features**: Handles 0, 1, or multiple arguments differently

#### 3. Value of my argument
**File**: `3-value_argument.js`
- **Purpose**: First argument extraction and validation
- **Concepts**: Array indexing, `undefined` checking
- **Restrictions**: Cannot use `var` or `length`

#### 4. Create a sentence
**File**: `4-concat.js`
- **Purpose**: String concatenation
- **Concepts**: Template literals, argument handling
- **Output**: "arg1 is arg2" format

#### 5. An Integer
**File**: `5-to_integer.js`
- **Purpose**: Type conversion and validation
- **Concepts**: `parseInt()`, `isNaN()`, error handling
- **Features**: Converts strings to integers with validation

#### 6. Loop to languages
**File**: `6-multi_languages_loop.js`
- **Purpose**: Arrays and iteration
- **Concepts**: `for...of` loops, array iteration
- **Restrictions**: No `if/else`, only one `console.log`

#### 7. I love C
**File**: `7-multi_c.js`
- **Purpose**: Conditional loops
- **Concepts**: `for` loops, input validation
- **Features**: Prints "C is fun" x times

#### 8. Square
**File**: `8-square.js`
- **Purpose**: Nested loops and pattern creation
- **Concepts**: String repetition, 2D patterns
- **Output**: Square patterns using 'X' character

#### 9. Add
**File**: `9-add.js`
- **Purpose**: Function definition and parameters
- **Concepts**: Function declaration, return values
- **Features**: Adds two integers using a function

#### 10. Factorial
**File**: `10-factorial.js`
- **Purpose**: Recursive functions
- **Concepts**: Recursion, base cases, mathematical operations
- **Features**: Calculates factorial recursively

#### 11. Second biggest!
**File**: `11-second_biggest.js`
- **Purpose**: Array manipulation and sorting
- **Concepts**: Array methods, sorting algorithms
- **Features**: Finds second largest number in arguments

#### 12. Object
**File**: `12-object.js`
- **Purpose**: Object property modification
- **Concepts**: Object properties, value assignment
- **Features**: Updates object value from 12 to 89

#### 13. Add file
**Files**: `13-add.js`, `13-main.js`
- **Purpose**: Module system and exports
- **Concepts**: `exports`, `require()`, module structure
- **Features**: Exportable function for external use

### Advanced Exercises (100-103)

#### 100. Const or not const
**Files**: `100-let_me_const.js`, `100-main.js`
- **Purpose**: Variable scope and global modification
- **Concepts**: Global scope, variable hoisting
- **Features**: Modifies global variable from another module

#### 101. Call me Moby
**Files**: `101-call_me_moby.js`, `101-main.js`
- **Purpose**: Higher-order functions
- **Concepts**: Function parameters, callback execution
- **Features**: Executes a function x times

#### 102. Add me maybe
**Files**: `102-add_me_maybe.js`, `102-main.js`
- **Purpose**: Callbacks and function composition
- **Concepts**: Callbacks, parameter transformation
- **Features**: Increments value and calls function

#### 103. Increment object
**File**: `103-object_fct.js`
- **Purpose**: Dynamic method addition
- **Concepts**: Object methods, `this` keyword
- **Features**: Adds increment method to object

## Key Concepts

### 🔤 **Variables and Constants**
- `const` for immutable bindings
- No `var` usage (ES6+ practices)
- Proper scoping and hoisting

### 🔄 **Control Flow**
- Conditional statements (`if/else`)
- Loops (`for`, `for...of`)
- Argument validation

### 📝 **Functions**
- Function declarations vs expressions
- Parameters and return values
- Recursive functions
- Higher-order functions

### 🏗️ **Objects and Arrays**
- Object creation and modification
- Array manipulation and sorting
- Dynamic property/method addition

### 📦 **Modules**
- `exports` and `require()`
- Module structure and organization
- Code reusability

### 🎯 **Advanced Topics**
- Variable scope and closures
- Callback functions
- Function composition
- Global variable manipulation

## Usage

### Running Individual Exercises

```bash
# Make file executable (if not already)
chmod +x filename.js

# Run the script
./filename.js [arguments]
```

### Examples

```bash
# Basic execution
./0-javascript_is_amazing.js

# With arguments
./2-arguments.js Hello World

# Factorial calculation
./10-factorial.js 5

# Module testing
./13-main.js
```

### Testing with Node.js

```bash
# Alternative execution method
node filename.js [arguments]
```

## Testing

### Manual Testing
Each exercise includes expected output examples. Test by running with various inputs.

### Automated Testing
Some exercises include companion test files (e.g., `13-main.js` tests `13-add.js`).

### Linting
Certain exercises must pass semistandard linting:

```bash
semistandard filename.js
```

## 🔧 **Development Guidelines**

### Code Standards
- No `var` declarations (use `const`/`let`)
- Proper error handling
- Clear, readable code structure
- Consistent indentation and formatting

### Best Practices
- Validate input parameters
- Handle edge cases
- Use descriptive variable names
- Follow JavaScript naming conventions

## 📊 **Exercise Progression**

1. **Beginner** (0-5): Basic syntax, variables, console output
2. **Intermediate** (6-10): Loops, functions, recursion
3. **Advanced** (11-13): Objects, modules, complex logic
4. **Expert** (100-103): Scope, callbacks, advanced patterns

## 🎓 **Learning Outcomes**

After completing these exercises, you will have:

- **Solid Foundation**: Understanding of JavaScript fundamentals
- **Problem-Solving Skills**: Ability to break down complex problems
- **Code Organization**: Knowledge of modules and structure
- **Advanced Concepts**: Familiarity with closures, callbacks, and scope

## Contributing

This project demonstrates progressive JavaScript learning. To contribute:

1. Follow existing code style and patterns
2. Maintain backward compatibility
3. Add comprehensive comments for complex logic
4. Test thoroughly with various inputs
5. Update documentation for new features

---

**Project developed by Hector**  
*Demonstrating JavaScript fundamentals and advanced concepts*

> This project serves as a comprehensive introduction to JavaScript programming, covering everything from basic syntax to advanced functional programming concepts. Perfect for beginners and those looking to solidify their JavaScript foundation.

---

*Part of the Holberton School Higher Level Programming curriculum*
