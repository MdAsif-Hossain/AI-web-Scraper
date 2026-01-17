import streamlit as st
from scrape import scrape_website
from scrape import extract_body_content
from scrape import clean_body_content
from scrape import split_som_content

from parse import parse_with_ollama

st.title("AI web Scraper")
url = st.text_input("Enter a website URL: ")


if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url) 
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("Scraped Content"):
        st.text_area("DOM content", cleaned_content, height=300)


    

if "dom_content" in st.session_state:
    parser_description = st.text_area("Descrive what you want to parse?")


    if st.button("Parse Content"):
        st.write("Parsing the content")
        
        dom_chunks = split_som_content(st.session_state.dom_content)
        result = parse_with_ollama(dom_chunks, parser_description)
        st.write(result)    