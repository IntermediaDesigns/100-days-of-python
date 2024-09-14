# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Broken Links

👉 What's the problem here?


```html
<p><a href = "memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>
```

<details> <summary> 👀 Answer </summary>

We didn't include the **https** part of the URL in the link.

```html
<p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>
```

</details>

## No Image

👉 What is the problem here?
```html
<img src="images/picard" width = 30%>
<p>Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</p>
```

<details> <summary> 👀 Answer </summary>

We forgot the file extension.

```html
<img src="images/picard.jpg" width = 30%>
<p>Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</p>
```
</details>

## A Massive Problem

👉 What is the problem here?
```html
<h1>Dave's World of Baldies
Welcome to our website!

<p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

<h2>Gallery of Baldies</h2>
<p>Here are some of the legends of the bald world.</p>
```

<details> <summary> 👀 Answer </summary>

Because we forgot to close the `<h1>` tag, the rest of the page gets treated as headings.

```html
<h1>Dave's World of Baldies</h1>
<h2>Welcome to our website!</h2>

<p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

<h2>Gallery of Baldies</h2>
<p>Here are some of the legends of the bald world.</p>
```
</details>