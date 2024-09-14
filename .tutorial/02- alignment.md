# Alignment

Another cool thing that we can do in css is to **align** our text.

👉 Let's align the `<h1>` and `<p>` tag text.  I'm using *center*, but you can also use *left* or *right*.

```css
h1{
  font-family: sans-serif;
  font-size: 24px;
  color: blue;
  background-color: #d3d345;
  text-align:center;
    
}

p{
  font-family: monospace;
  font-size: 10px;
  color: blue;
   text-align:center;
    
}
```
##
👉 I also want to apply the `<h1>` settings to the `<h2>` tag, but instead of creating a whole new style, I can just add the tag name at the top of the `<h1>` style:

```css
h1, h2{
  font-family: sans-serif;
  font-size: 24px;
  color: blue;
  background-color: #d3d345;
  text-align:center;
    
}
```

However, I **do** want `<h2>` to be a bit smaller, so I can define a new style **after** the 'h1, h2' style and just change the font size:

```css
html, body {
  height: 100%;
  width: 100%;
  background-color: #e4e2e2;
}

h1, h2{
  font-family: sans-serif;
  font-size: 24px;
  color: blue;
  background-color: #d3d345;
  text-align:center;
    
}

''' THIS IS THE NEW BIT'''
h2{
  font-size: 12px;
  
}

p{
  font-family: monospace;
  font-size: 10px;
  color: blue;
   text-align:center;
    
}
```
### Look familiar?
This second style for `<h2>` works a bit like sub-classes did in OOP. It **inherits** all the properties from the first style and then applies the new settings as well, prioritizing the settings in the second style if there is a conflict.

## Images

👉 We can also use CSS with our image tags. Centering an image isn't very intuitive, but we can do it like this:

```css
img{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  
}
```

## Tags and Classes

It's also possible to directly address a single tag by giving it a class name.

👉 Here's an example of how I've created the `blurb` class directly in a `<p>` tag in the **index.html** page.

```html
<p class = "blurb">Yul Brynner is another amazing baldie, a famous actor in the 20th Century, he is most remembered for his roles in "The King and I", and the original "Westworld".</p>

```
Now, I can style my `blurb` class in the **style.css** file.  Notice how I've referred to it using **dot**blurb -> .blurb

```css
.blurb{
  font-style: italic;
  font-weight: bold;
}
```


### Try it out!