import streamlit as st
import random
import os
import time
import csv





# Open the CSV file
with open("data/words.csv", 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Assuming the words are in the first row (change the index if necessary)
    row = next(csv_reader)
    
    # Extract words from the row and save them into a list
    words = list(row)





def show(test_words,no_ques):
    
    # Display the image using placeholder
    image_placeholder = st.empty()
    image_placeholder3 = st.empty()
    
    
    for i in range(no_ques):
        for j in range(0,15):

            image_placeholder.subheader(f"Word {i+1} : {test_words[i]}")
            image_placeholder3.write(f"Time left: {15 - j} seconds")
            
            
            time.sleep(1)
    
        print('\a')
        
            
            
    image_placeholder = st.empty()
    image_placeholder3=st.empty()
    
    


# Main function to run the Streamlit app
def wat():
    wat_description = """
    <div ">
        <h1>Welcome to WAT</h1>
        <p>The Word Association Test (WAT) is a psychological assessment test that evaluates personality and cognitive ability. 
        It's the second test in the series of psychological tests at the Service Selection Board (SSB). The WAT evaluates an individual's:</p>
        <ul>
            <li><strong>Personality</strong></li>
            <li><strong>Cognitive ability</strong></li>
            <li><strong>Thought patterns</strong></li>
            <li><strong>Underlying beliefs at a subconscious level</li>
        </ul>
    </div>
    """
    st.markdown(wat_description, unsafe_allow_html=True)
    
    no_ques = int(st.number_input("Enter a words(you want to test):",step=5,value=60,min_value=0,max_value=2000))
    test_words = random.sample(words, no_ques)
    if st.button("Start"):
        show(test_words,no_ques)
    
   

if __name__ == "__main__":
    wat()
    
