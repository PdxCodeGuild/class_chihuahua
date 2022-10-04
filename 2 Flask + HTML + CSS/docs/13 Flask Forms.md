
# Flask Forms

When a Flask view receives a form submission, it's transformed into a dictionary and is accessable as `request.form`. By default, routes only respond to GET requests, we can allow them to respond to requests using other methods by passing them to the `route`.

**index.html**
```html
<form action="" method="post">
  <input type="text" name="input_text" placeholder="enter some text"/>
  <button type="submit">submit</button>
</form>
```

**app.py**
```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        contact_name = request.form['input_text']
        print(contact_name)
    return render_template('index.html')
```


You can also use two separate views, one for rendering a template, and another for receiving a form submission and redirecting back to the first view.


**index.html**
```html
<form action="/receive_form/" method="post">
    <input type="text" name="person_name" value="Jane"/>
    <input type="text" name="person_age" value="34"/>
    <button type="submit">submit</button>
</form>
```

**app.py**
```python
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_form/', methods=['POST'])
def temperature():
    print(request.form) # {'person_name': 'Jane', 'person_age': 34}
    person_name = request.form['person_name'] # Jane
    person_age = request.form['person_age'] # 34
    return redirect('/')
```

# Grab input from common HTML elements

```html
<div class="form-group row">
    <div class="form-group row">
    <select name='select-elements'  class="form-select" aria-label="Default select example">
    <option selected>Open this select menu</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
    </select>
    </div>
      <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label>
      <div class="col-sm-10">
        <input
          type="text"
          name="text"
          class="form-control"
          id="inputEmail3"
          placeholder="type here"
        />
      </div>
    </div>
    <fieldset class="form-group">
      <div class="row">
        <legend class="col-form-label col-sm-2 pt-0">Radios</legend>
        <div class="col-sm-10">
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="gridRadios"
              id="gridRadios1"
              value="option1"
              checked
            />
            <label class="form-check-label" for="gridRadios1">
              First radio
            </label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="gridRadios"
              id="gridRadios2"
              value="option2"
            />
            <label class="form-check-label" for="gridRadios2">
              Second radio
            </label>
          </div>
        </div>
      </div>
    </fieldset>
    <div class="form-group row">
      <div class="col-sm-2">Checkbox</div>
      <div class="col-sm-10">
        <div class="form-check">
          <input name='check' value ='blue' class="form-check-input" type="checkbox" id="gridCheck1" />
          <label checkclass="form-check-label" for="gridCheck1">
            Blue
          </label>
        </div>
        <div class="form-check">
            <input name='check' value ='red' class="form-check-input" type="checkbox" id="gridCheck2" />
            <label class="form-check-label" for="gridCheck2">
              Red
            </label>
          </div>
      </div>
    </div>
    <div class="form-group row">
      <div class="col-sm-10">
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
    </div>
```

```python
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('<your-template>.html')
    elif request.method == "POST":
        text = request.form['text'] #text field
        radio = request.form['gridRadios'] #radio buttons
        checks = request.form.getlist('check') #check boxe
        select = request.form.get('select-elements') # select element
        print('TEXT', text)
        print('radio', radio)
        print('checkboxes', checks)
        print('select', select)
        return render_template('<your-template>', text=text, radio=radio,checks=checks, select=select)

```
# Conditional Rendering

We can conditionally render CSS classes using if/ else statements

```python
@app.route('/test/')
def test():
    color = "red"
    return render_template('test.html',color=color)

```

```html
<div class="container mt-5">
    <button type="button" class="btn btn-{% if color=='red'%}danger{%else%}warning{% endif%}">Primary</button>
</div>
```

You can also dinamically render any element

```python
@app.route('/test/')
def test():
    options = ['volvo','saab','toyota']
    return render_template('test.html',options=options)

```

```html
<select class="form-select" aria-label="Default select example">
    <option selected>Open this select menu</option>
    {%for option in options%}
    <option value="{{option}}">{{option}}</option>
    {%endfor%}
  </select>
```