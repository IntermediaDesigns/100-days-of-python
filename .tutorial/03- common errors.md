# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Common Problem 1

👉 What's the problem here?


```css
p{
  font-family: monospace;
  font-size: 10px
  color: blue
   text-align:center;
    
}
```

<details> <summary> 👀 Answer </summary>

We missed some semi colons from the end of lines.

```css
p{
  font-family: monospace;
  font-size: 10px;
  color: blue;
   text-align:center;
    
}
```

</details>

## Common Problem 2

👉 What's the problem here?


```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
</head>
```

<details> <summary> 👀 Answer </summary>

The link to the style page was missing.

Solution 1 is to insert the link.

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>
```

Solution 2 is to have a `style` tag in the head of the html page that contains all the css needed.  This isn't ideal though, because then you can't share your CSS across multiple pages.

</details>