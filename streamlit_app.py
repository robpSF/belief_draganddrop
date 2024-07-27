import streamlit as st
import streamlit.components.v1 as components

# Title of the app
st.title("Drag and Drop Quadrant with Custom Axes")

# Input fields for axes of uncertainty
belief1 = st.text_input("Enter Belief 1 (left-right axis):", "#Defence")
belief2 = st.text_input("Enter Belief 2 (top-bottom axis):", "#Defence")

# Generate labels for the quadrants based on the input
belief1_left = f"{belief1}_Champion"
belief1_right = f"{belief1}_Skeptic"
belief2_top = f"{belief2}_Champion"
belief2_bottom = f"{belief2}_Skeptic"

# Define the labels for each quadrant
quadrant1_label = f"{belief1_left} <> {belief2_top}"
quadrant2_label = f"{belief1_right} <> {belief2_top}"
quadrant3_label = f"{belief1_left} <> {belief2_bottom}"
quadrant4_label = f"{belief1_right} <> {belief2_bottom}"

# Define the drag-and-drop JavaScript and HTML
drag_drop_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            gap: 10px;
            height: 400px;
            position: relative;
            margin-top: 50px;
        }}
        .quadrant {{
            border: 2px solid #ccc;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            background-color: #f9f9f9;
            min-height: 100px;
        }}
        .draggable {{
            padding: 10px;
            margin: 5px;
            background-color: #007bff;
            color: #fff;
            border-radius: 5px;
            cursor: move;
            margin-top: 20px;
        }}
        .label {{
            position: absolute;
            font-size: 14px;
            font-weight: bold;
        }}
        #belief1_left {{
            left: -100px;
            top: 50%;
            transform: translateY(-50%);
            text-align: left;
        }}
        #belief1_right {{
            right: -100px;
            top: 50%;
            transform: translateY(-50%);
            text-align: right;
        }}
        #belief2_top {{
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
        }}
        #belief2_bottom {{
            bottom: -30px;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
        }}
    </style>
</head>
<body>

<div class="container">
    <div id="quadrant1" class="quadrant" ondrop="drop(event)" ondragover="allowDrop(event)">{quadrant1_label}</div>
    <div id="quadrant2" class="quadrant" ondrop="drop(event)" ondragover="allowDrop(event)">{quadrant2_label}</div>
    <div id="quadrant3" class="quadrant" ondrop="drop(event)" ondragover="allowDrop(event)">{quadrant3_label}</div>
    <div id="quadrant4" class="quadrant" ondrop="drop(event)" ondragover="allowDrop(event)">{quadrant4_label}</div>

    <div id="belief1_left" class="label">{belief1_left}</div>
    <div id="belief1_right" class="label">{belief1_right}</div>
    <div id="belief2_top" class="label">{belief2_top}</div>
    <div id="belief2_bottom" class="label">{belief2_bottom}</div>
</div>

<div class="draggable" draggable="true" ondragstart="drag(event)" id="item1">Item 1</div>
<div class="draggable" draggable="true" ondragstart="drag(event)" id="item2">Item 2</div>

<script>
    function allowDrop(event) {{
        event.preventDefault();
    }}

    function drag(event) {{
        event.dataTransfer.setData("text", event.target.id);
    }}

    function drop(event) {{
        event.preventDefault();
        var data = event.dataTransfer.getData("text");
        event.target.appendChild(document.getElementById(data));
    }}
</script>

</body>
</html>
"""

# Display the drag-and-drop HTML/JS
components.html(drag_drop_html, height=600)
