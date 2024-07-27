import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# Title of the app
st.title("Drag and Drop Quadrant with Custom Axes")

# Step 1: Upload Excel File
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)

    # Step 2: Select Faction
    factions = df['Faction'].unique()
    selected_faction = st.selectbox("Select a Faction", factions)

    if selected_faction:
        # Filter the dataframe by the selected faction
        filtered_df = df[df['Faction'] == selected_faction]

        # Display the filtered data (optional, for verification)
        st.write("Filtered Data:", filtered_df)

        # Step 3: Enter axes of uncertainty and continue with the program
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

        # Create draggable items for each row in the filtered dataframe
        draggable_items_html = ""
        for index, row in filtered_df.iterrows():
            item_id = f"item{index}"
            name = row["Name"]
            image_url = row["Image"]
            draggable_items_html += f"""
            <div class="draggable" draggable="true" ondragstart="drag(event)" id="{item_id}">
                <img src="{image_url}" alt="{name}" width="50" height="50"><br>{name}
            </div>
            """

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
                    height: 500px;
                    position: relative;
                    margin-top: 50px;
                }}
                .quadrant {{
                    border: 2px solid #ccc;
                    border-radius: 10px;
                    padding: 10px;
                    text-align: center;
                    background-color: #f9f9f9;
                    min-height: 200px;
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    grid-template-rows: repeat(3, auto);
                    gap: 10px;
                }}
                .draggable {{
                    padding: 5px;
                    background-color: #007bff;
                    color: #fff;
                    border-radius: 5px;
                    cursor: move;
                    text-align: center;
                    display: inline-block;
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

        <div style="margin-top: 20px;">
            {draggable_items_html}
        </div>

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
        components.html(drag_drop_html, height=800)
