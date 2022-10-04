# Lab 1: Bio

Write up a short bio webpage for someone or something. It can be about a celebrity, a fictionary character, a place, a species, etc. Check out the [examples](https://github.com/PdxCodeGuild/class_bumble_bee/tree/main/2%20HTML%20%2B%20CSS/labs/images)

## Part 1

- A written introduction
- A link to a Wikipedia article
- A picture of them
- A list of places where they've lived
- A quote from them

## Part 2

- Center the entire content of the body
- Modify the padding and margins on your paragraphs to look better
- Use a custom font
- Add a background image

## Part 3

- Pick a color scheme and modify the background, body text, and link text color.
- Change the typeface of the quote. You can use the **font-family** [property](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)
- Add a rounded border to the picture.
- Change the bullet points on the list of places. You can use the example below to help yourself.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <style>
      ul {
        list-style: none;
      } /* Remove default bullets */

      li::before {
        font-family: "Font Awesome 5 Free";
        content: "\f35a";
        color: green;

        margin-right: 10px; /* Optional tweak */
      }
    </style>
    <ul>
        <li>Sun</li>
        <li>Rain</li>
        <li>Snow</li>

    </ul>
  </body>
</html>
```
