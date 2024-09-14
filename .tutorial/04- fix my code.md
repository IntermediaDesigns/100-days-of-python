# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## HTML File

```html

<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  
</head>

<body>
  
  <h1>Baldies Page 2</h1>
  <p>The continuation of the epic website showing the best of the bald bunch.</p>

  <h2>Yul Brynner</h2>
  <img src="yulBrynner.jpg" width ="200px">
  <p class = "blurb">Yul Brynner is another amazing baldie, a famous actor in the 20th Century, he is most remembered for his roles in "The King and I", and the original "Westworld".</p>
  
</body>

</html>

```

## CSS File

```css
html, body {
  height: 100%;
  width: 100%;
  background-color: #e4e2e2;
}

h1, h2{
  font-family: sans-serif;
  font-size: 24px
  color: blue
  background-color: #d3d345;
  text-align:center;
    
}

h2{
  font-size: 12px;
  
}

p{
  font-family: monospace;
  font-size: 10px;
  color: blue;
   text-align:center;
    
}

{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  
}

.blurb{
  font-style: italic;
  font-weight: bold;
}
```
<details> <summary> 👀 Answer </summary>
  
## HTML File

```html

<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" /> ## Missing link to style sheet
</head>

<body>
  
  <h1>Baldies Page 2</h1>
  <p>The continuation of the epic website showing the best of the bald bunch.</p>

  <h2>Yul Brynner</h2>
  <img src="yulBrynner.jpg" width ="200px">
  <p class = "blurb">Yul Brynner is another amazing baldie, a famous actor in the 20th Century, he is most remembered for his roles in "The King and I", and the original "Westworld".</p>
  
</body>

</html>

```

## CSS File

```css
html, body {
  height: 100%;
  width: 100%;
  background-color: #e4e2e2;
}

h1, h2{
  font-family: sans-serif;
  font-size: 24px; ## Missing semi colon
  color: blue; ## Missing semi colon
  background-color: #d3d345;
  text-align:center;
    
}

h2{
  font-size: 12px;
  
}

p{
  font-family: monospace;
  font-size: 10px;
  color: blue;
  text-align:center;
    
}

img{ ## No style name
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  
}

.blurb{
  font-style: italic;
  font-weight: bold;
}
```

</details