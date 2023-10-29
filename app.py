import streamlit as st
import os
from PIL import Image
import time
st.set_page_config(layout="wide")

# Path to the folder containing the images
folder_path = "/images"

# Get a list of image files in the folder
image_files = [filename for filename in os.listdir(folder_path) if filename.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

def show(image_path):
    # Open the image using PIL
    image = Image.open(image_path)
    
    # Display the image using placeholder
    image_placeholder = st.empty()
    image_placeholder.image(image, caption='Image Caption')
    
    image_placeholder2 = st.empty()
    image_placeholder2.text("")
    
    time_left=10
    col1, col2 = st.columns(2)
    # Wait for 30 seconds before removing the image
    for i in range(11):
        time.sleep(1)
        # Update the image dynamically after 1 second delay
        with col1:
            image_placeholder.image(image, caption='Image Caption')
        with col2:
            image_placeholder2.header(time_left-i)
    
    # After 30 seconds, remove the image
    image_placeholder.empty()
    image_placeholder2.empty()
    time_left=240
    for i in range(241):
        time.sleep(1)
        image_placeholder.header("Writting time")
        image_placeholder2.write(time_left-i)
        
    image_placeholder.empty()
    image_placeholder2.empty()
    
    
    
# Function to display the selected image
def show_image(image_path):
    image = Image.open(image_path)
    resized_image = image.resize((400, 400))
    st.image(resized_image, caption='Image Caption')

# Function to handle previous page navigation
def previous_page(current_page):
    if current_page > 1:
        st.experimental_set_query_params(page=current_page - 1)

# Function to handle next page navigation
def next_page(current_page):
    st.experimental_set_query_params(page=current_page + 1)

# Main function to run the Streamlit app
def main():
    st.title("Display Images with Navigation")
    
    # Get the page number from the URL parameter
    page_number = st.experimental_get_query_params().get("page", 1)
    page_number = int(page_number[0]) if isinstance(page_number, list) else int(page_number)
    
    # Calculate start and end indices for the displayed images
    start_index = (page_number - 1) * 8
    end_index = min(start_index + 8, len(image_files))
    
    # Create a row to display buttons corresponding to image names
    row = st.columns(11)
    
    # Display buttons with names corresponding to images
    buttons = []
    for i in range(start_index, end_index):
        with row[i - start_index].container():
            buttons.append(st.button(image_files[i]))
    
    # Show selected image when a button is clicked
    for i in range(start_index, end_index):
        if buttons[i - start_index]:
            show(os.path.join(folder_path, image_files[i]))
            
    col1,col2=st.columns(2)
    with col1:
        if st.button("Previous"):
            previous_page(page_number)
    with col2:
        if st.button("Next"):
            next_page(page_number)
    
   
   
   

# Run the app
if __name__ == "__main__":
    main()
    
