import streamlit as st
import streamlit.components.v1 as components

# Define the drag-and-drop JavaScript and HTML
drag_drop_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            gap: 10px;
            height: 400px;
        }
        .quadrant {
            border: 2px solid #ccc;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            background-color: #f9f9f9;
            min-height: 100px;
        }
        .draggable {
            padding: 10px;
            margin: 5px;
            background-color: #007bff;
            color: #fff;
            border-radius: 5px;
            cursor: move;
        }
    </style>
</head>
<body>

<div class="container">
    <div id="quadrant1" class="quadrant" ondrop="drop(event)" ondragover="allowDrop(event)">Quadrant 1</div>
    <div id="quadrant2" class="quadrant" ondrop="drop(event)" ondragover="allowDrop(event)">Quadrant 2</div>
    <div id="quadrant3" class="quadrant" ondrop="drop(event)" ondragover="allowDrop(event)">Quadrant 3</div>
    <div id="quadrant4" class="quadrant" ondrop="drop(event)" ondragover="allowDrop(event)">Quadrant 4</div>
</div>

<div class="draggable" draggable="true" ondragstart="drag(event)" id="item1">Item 1</div>
<div class="draggable" draggable="true" ondragstart="drag(event)" id="item2">Item 2</div>

<script>
    function allowDrop(event) {
        event.preventDefault();
    }

    function drag(event) {
        event.dataTransfer.setData("text", event.target.id);
    }

    function drop(event) {
        event.preventDefault();
        var data = event.dataTransfer.getData("text");
        event.target.appendChild(document.getElementById(data));
    }
</script>

</body>
</html>
"""

# Create a Streamlit app
st.title("Drag and Drop Demo with Streamlit")

# Display the drag-and-drop HTML/JS
components.html(drag_drop_html, height=600)
