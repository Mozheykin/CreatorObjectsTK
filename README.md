# CreatorObjectsTK

## Description
CreatorObjectsTK is a module for converting XML instructions into Tkinter classes. It allows you to easily create a user interface using XML files and Tkinter.

## Installation
To install the CreatorObjectsTK module, run the following command:

 
pip install git+https://github.com/Mozheykin/CreatorObjectsTK.git\
or\
poetry add git+https://github.com/Mozheykin/CreatorObjectsTK.git\

## Usage

```python
from CreatorObjectsTK import CreateWindow, CreateButton

# Creating a CreatorObjectsTK window
window_create = CreateWindows(name='WIN_1')
window_create.parse(pr=input_dict, ud=user_dict)
window_create.create()

# Creating a CreatorObjectsTK button
button_create = CreateButton(name='BUT_1')
button_create.parse(pr=input_dict, ud=user_dict)
button_create(command=function)
```

# Converting an XML file to a Tkinter class and saving it to a file
creator_objects_tk.convert('input.xml', 'output.py')

## XML File Format

The XML file should have the following structure:

 xml
<window>
    <title>Window Title</title>
    
    <button>
        <text>Click Me</text>
        
        <command>button_clicked</command>
    </button>
    
    <label>
        <text>Hello, World!</text>
    </label>
</window>

This XML file contains instructions for creating a window with a title, a button, and a label. The Tkinter class created using the CreatorObjectsTK module will have a method named button_clicked, which will be called when the button is clicked.

## Limitations

The CreatorObjectsTK module has the following limitations:

- The XML file must have the correct structure as specified above.
- The XML tag names must correspond to the available Tkinter classes (e.g., "window", "button", "label", etc.).
- Nested tags must be in the correct order.
- To add attributes to the widgets, use additional tags with the name "attribute".

## License
The CreatorObjectsTK module is distributed under the MIT license. You can find more information in the LICENSE file.
