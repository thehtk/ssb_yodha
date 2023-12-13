import streamlit as st
import random
import os
import time
import csv
import winsound
import pandas as pd


# Specify the file path
file_path = r"data/srt_final.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

new_data=list(df)

def show(srt_ques,no_ques,srt_ans):
    
    # Display the image using placeholder
    
    image_placeholder1 = st.empty()
    image_placeholder2 = st.empty()
    image_placeholder3 = st.empty()
    image_placeholder4 = st.empty()
    image_placeholder1.empty()
    image_placeholder2.empty()
    image_placeholder3.empty()
    image_placeholder4.empty()
    
    
    for i in range(no_ques):
        for j in range(0,30):

            image_placeholder1.subheader(f"S{i+1} : {srt_ques[i]}")
            image_placeholder2.write(f"Time left: {30 - j} seconds")
            
            
            time.sleep(1)
        winsound.Beep(2000, 300)
            
            
    image_placeholder1.empty()
    image_placeholder2.empty()
    
    image_placeholder3.subheader("Answers")
    table_data = {'Questions': srt_ques, 'Answers': srt_ans}
    image_placeholder4.table(table_data)
    


def srt():
    
    
    srt_description = """
    <div >
        <h1>Welcome to SRT</h1>
        <p>The Situation Reaction Test (SRT) is a psychological test that's part of the SSB interview. 
        It's conducted on the second day of the interview. The SRT assesses a candidate's:</p>
        <ul>
            <li><strong>Thought Process</strong></li>
            <li><strong>Decision-making Abilities</strong> </li>
            <li><strong>Handling Different Situations</strong></li>
        </ul>
        
    </div>
"""
    st.markdown(srt_description, unsafe_allow_html=True)
    all_srt_ques = df['Ques'].tolist()
    all_srt_ans= df['Ans'].tolist()
    size=len(all_srt_ques)
    
    # Limit the number of questions to the maximum available
    no_ques = int(st.number_input("Enter a number of questions (you want to test):", step=5, value=60, min_value=0, max_value=size))
    
    # Check if the selected number of questions is greater than the available questions
    random_numbers = random.sample(range(1, size + 1), no_ques)
    
    srt_ques=[]
    srt_ans=[]
    for i in random_numbers:
        srt_ques.append(all_srt_ques[i])
        srt_ans.append(all_srt_ans[i])
    
        
    if st.button("Start"):
        show(srt_ques, no_ques,srt_ans)
        
    

if __name__ == "__main__":
    srt()
   

    
