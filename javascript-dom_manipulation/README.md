# JavaScript - DOM Manipulation

## 🚀 Project Overview

This project explores the fundamentals of **Document Object Model (DOM) manipulation** using vanilla JavaScript. The DOM is a programming interface for HTML and XML documents, representing the page structure as a tree of nodes that can be modified with JavaScript.

**Repository:** `holbertonschool-higher_level_programming`  
**Directory:** `javascript-dom_manipulation`  
**Language:** JavaScript (ES6+)  
**Focus:** Client-side DOM manipulation, event handling, and API integration  
**Files:** 9 JavaScript scripts demonstrating progressive DOM manipulation concepts

---

## 📚 Learning Objectives

By completing this project, you will understand:

- **DOM Structure**: How HTML documents are represented as a tree of nodes
- **Element Selection**: Using `querySelector()` and `querySelectorAll()` methods
- **Event Handling**: Adding event listeners and responding to user interactions
- **Style Manipulation**: Dynamically changing CSS properties via JavaScript
- **Class Management**: Adding, removing, and toggling CSS classes
- **Content Modification**: Updating text content and HTML structure
- **Dynamic Element Creation**: Creating and appending new DOM elements
- **Fetch API**: Making HTTP requests to external APIs
- **JSON Handling**: Processing and displaying data from API responses
- **Error Handling**: Implementing proper error handling for API calls

---

## 🎯 Key Concepts Covered

### 1. DOM Selection and Traversal
- `document.querySelector()` - Select the first matching element
- `document.querySelectorAll()` - Select all matching elements
- CSS selector syntax for precise element targeting

### 2. Event-Driven Programming
- `addEventListener()` method for event binding
- Click events and user interaction handling
- Event delegation and bubbling concepts

### 3. Dynamic Styling
- `style` property for inline CSS modifications
- `classList` API for class management
- CSS class toggling and replacement

### 4. Content Manipulation
- `textContent` property for text updates
- `innerHTML` for HTML content modification
- Dynamic element creation with `createElement()`

### 5. Asynchronous Programming
- `fetch()` API for HTTP requests
- Promise handling with `.then()` and `.catch()`
- JSON data processing and display

---

## 📝 Project Tasks

### Task 0: Color me
**File:** [`0-script.js`](./0-script.js)  
**Objective:** Update the text color of the header element to red (#FF0000)

```javascript
document.querySelector('header').style.color = '#FF0000';
```

**Key Learning:**
- Basic DOM selection with `querySelector()`
- Direct style property manipulation
- Immediate script execution

---

### Task 1: Click and turn red
**File:** [`1-script.js`](./1-script.js)  
**Objective:** Add click event listener to turn header red when clicked

```javascript
document.querySelector('#red_header').addEventListener('click', function () {
  document.querySelector('header').style.color = '#FF0000';
});
```

**Key Learning:**
- Event listener attachment with `addEventListener()`
- Anonymous function event handlers
- ID-based element selection

**Note:** Contains intentional typo (`querySlector`) for debugging practice

---

### Task 2: Add CSS class
**File:** [`2-script.js`](./2-script.js)  
**Objective:** Add a CSS class to the header element on click

```javascript
document.querySelector('#red_header').addEventListener('click', function () {
  document.querySelector('header').classList.add('red');
});
```

**Key Learning:**
- `classList.add()` method for class management
- CSS class-based styling approach
- Separation of concerns (CSS vs JavaScript)

**Note:** Contains intentional typo (`classicList`) for debugging practice

---

### Task 3: Toggle header
**File:** [`3-script.js`](./3-script.js)  
**Objective:** Toggle between red and green classes on header click

```javascript
document.querySelector('#toggle_header').addEventListener('click', function () {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
});
```

**Key Learning:**
- `classList.contains()` for conditional logic
- `classList.replace()` for class swapping
- Toggle functionality implementation
- Conditional statements in event handlers

**Note:** Contains intentional syntax errors for debugging practice

---

### Task 4: List of elements
**File:** [`4-script.js`](./4-script.js)  
**Objective:** Add new list items to an existing UL element

```javascript
document.querySelector('#add_item').addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newItem);
});
```

**Key Learning:**
- `createElement()` for dynamic element creation
- `textContent` for setting element content
- `appendChild()` for DOM tree manipulation
- Class selector usage (`.my_list`)

**Note:** Contains intentional syntax errors for debugging practice

---

### Task 5: Update the header
**File:** [`5-script.js`](./5-script.js)  
**Objective:** Update header text content on button click

```javascript
document.querySelector('#update_header').addEventListener('click', function () {
  document.querySelector('header').textContent = 'New Header!!!';
});
```

**Key Learning:**
- `textContent` property for text updates
- Dynamic content modification
- Event-driven content changes

**Note:** Contains intentional syntax error (missing quotes) for debugging practice

---

### Task 6: Star Wars character
**File:** [`6-script.js`](./6-script.js)  
**Objective:** Fetch and display Star Wars character data from API

```javascript
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.querySelector('#character').textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching character:', error);
  });
```

**Key Learning:**
- `fetch()` API for HTTP requests
- Promise chain handling with `.then()`
- JSON data parsing with `response.json()`
- Error handling with `.catch()`
- API integration and data display

**Note:** Contains intentional typo (`documnet`) for debugging practice

---

### Task 7: List Star Wars movies
**File:** [`7-script.js`](./7-script.js)  
**Objective:** Fetch and display list of Star Wars movies

```javascript
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movies = data.results;
    const movieList = document.querySelector('#list_movies');
    
    movies.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      movieList.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });
```

**Key Learning:**
- Array iteration with `forEach()`
- Dynamic list generation from API data
- Multiple element creation in loops
- Complex data structure handling
- Nested API response processing

---

### Task 8: Say Hello
**File:** [`8-script.js`](./8-script.js)  
**Objective:** Fetch and display greeting in French when DOM is loaded

```javascript
document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.querySelector('#hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching greeting:', error);
    });
});
```

**Key Learning:**
- `DOMContentLoaded` event for initialization
- Internationalization concept with API
- Script execution timing
- Language-specific API requests

---

## 🔧 Technical Requirements

### General Requirements
- **Browser Compatibility:** Chrome 57.0+, Firefox 55.0+, Safari 11.0+
- **JavaScript Version:** ES6+ (ECMAScript 2015+)
- **No External Libraries:** Pure vanilla JavaScript only
- **File Structure:** Individual `.js` files for each task
- **Code Style:** Consistent indentation and naming conventions

### HTML Structure Expected
The scripts assume the following HTML elements exist:
- `<header>` - Main header element
- `#red_header` - Button/element to trigger red color
- `#toggle_header` - Button/element to toggle header colors
- `#add_item` - Button/element to add list items
- `.my_list` - UL element for dynamic list items
- `#update_header` - Button/element to update header text
- `#character` - Element to display Star Wars character
- `#list_movies` - UL element for movie list
- `#hello` - Element to display greeting

### CSS Classes Expected
- `.red` - Red styling class
- `.green` - Green styling class

---

## 🎨 Usage Examples

### Basic HTML Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOM Manipulation</title>
    <style>
        .red { color: #FF0000; }
        .green { color: #00FF00; }
    </style>
</head>
<body>
    <header>Original Header</header>
    <button id="red_header">Make Red</button>
    <button id="toggle_header">Toggle Color</button>
    <button id="add_item">Add Item</button>
    <button id="update_header">Update Header</button>
    
    <ul class="my_list"></ul>
    <div id="character"></div>
    <ul id="list_movies"></ul>
    <div id="hello"></div>
    
    <script src="0-script.js"></script>
</body>
</html>
```

### Running the Scripts
1. **Include in HTML:**
   ```html
   <script src="script-name.js"></script>
   ```

2. **Test in Browser Console:**
   ```javascript
   // Copy and paste script content directly
   document.querySelector('header').style.color = '#FF0000';
   ```

3. **Development Tools:**
   - Use browser Developer Tools (F12)
   - Console for debugging and testing
   - Elements tab for DOM inspection

---

## 🐛 Common Debugging Notes

### Intentional Errors in Code
Several files contain intentional errors for educational purposes:

1. **1-script.js:** `querySlector` → `querySelector`
2. **2-script.js:** `classicList` → `classList`
3. **3-script.js:** `toogle_header` → `toggle_header`, syntax errors
4. **4-script.js:** `const newItem +` → `const newItem =`, `docucemnt` → `document`
5. **5-script.js:** Missing quotes in `querySelector(header)`
6. **6-script.js:** `documnet` → `document`

### Common Issues and Solutions

**Problem:** Script not executing
```javascript
// Solution: Ensure DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Your code here
});
```

**Problem:** Element not found
```javascript
// Solution: Verify selector syntax
const element = document.querySelector('#myId');
if (element) {
    // Element exists, safe to manipulate
}
```

**Problem:** Fetch request failing
```javascript
// Solution: Add proper error handling
fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .catch(error => console.error('Error:', error));
```

---

## 🌐 API References

### Star Wars API (SWAPI)
- **Base URL:** `https://swapi-api.hbtn.io/api/`
- **Character Endpoint:** `/people/{id}/`
- **Films Endpoint:** `/films/`
- **Format:** JSON
- **Authentication:** None required

### HelloSalut API
- **Base URL:** `https://hellosalut.stefanbohacek.dev/`
- **Language Parameter:** `?lang=fr`
- **Response:** `{ "hello": "Salut" }`

---

## 📊 Performance Considerations

### Best Practices Implemented
1. **Efficient Selectors:** Use ID selectors when possible
2. **Event Delegation:** Minimize event listener attachments
3. **DOM Caching:** Store DOM references when reusing elements
4. **Error Handling:** Implement proper error handling for API calls

### Optimization Opportunities
```javascript
// Good: Cache DOM elements
const header = document.querySelector('header');
const button = document.querySelector('#red_header');

// Good: Use event delegation for multiple elements
document.addEventListener('click', function(e) {
    if (e.target.matches('#red_header')) {
        header.style.color = '#FF0000';
    }
});
```

---

## 🔍 Testing and Validation

### Manual Testing Steps
1. **Load HTML page** with script included
2. **Open Developer Tools** (F12)
3. **Test each interaction:**
   - Click buttons to verify event handling
   - Check console for errors
   - Verify DOM changes in Elements tab
   - Test API calls with Network tab

### Automated Testing (Optional)
```javascript
// Example unit test structure
function testHeaderColor() {
    const header = document.querySelector('header');
    // Execute script
    // Assert expected changes
    console.assert(header.style.color === 'rgb(255, 0, 0)', 'Header should be red');
}
```

---

## 📚 Learning Resources

### Essential Reading
- [MDN - Document Object Model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- [MDN - querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
- [MDN - addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
- [MDN - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

### Interactive Learning
- [JavaScript.info - DOM](https://javascript.info/dom-nodes)
- [MDN - Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)

### Video Tutorials
- [Traversy Media - DOM Manipulation](https://www.youtube.com/watch?v=0ik6X4DJKCc)
- [The Net Ninja - JavaScript DOM Tutorial](https://www.youtube.com/playlist?list=PL4cUxeGkcC9gfoKa5la9dsdCNpuey2s-V)

---

## 🚀 Next Steps

### Advanced Concepts to Explore
1. **Event Bubbling and Capturing**
2. **DOM Performance Optimization**
3. **Modern JavaScript (ES6+) Features**
4. **Async/Await for API Calls**
5. **Error Handling Best Practices**
6. **Cross-browser Compatibility**

### Practical Applications
- **Form Validation:** Dynamic form validation with DOM manipulation
- **Single Page Applications:** Building interactive web applications
- **Data Visualization:** Creating charts and graphs dynamically
- **Game Development:** Simple browser-based games

---

## 👥 Contributing

This project is part of the Holberton School curriculum. The intentional errors in the code serve as learning exercises for debugging and problem-solving skills.

### Code Standards
- Use consistent indentation (2 spaces)
- Follow semantic naming conventions
- Add comments for complex logic
- Implement proper error handling

---

## 📄 License

This project is part of the Holberton School Higher Level Programming curriculum.

---

## 📞 Support

For questions or clarifications about DOM manipulation concepts:
- Review MDN documentation
- Practice with browser Developer Tools
- Experiment with different selectors and methods
- Test API endpoints independently

---

**Author:** Hector  
**Project:** JavaScript DOM Manipulation  
**Track:** Higher Level Programming  
**Completion:** 9 tasks demonstrating progressive DOM manipulation skills

*This project provides hands-on experience with client-side JavaScript, preparing students for modern web development challenges.*
