import gradio as gr
def text_analyzer(text):
    char_count = len(text)                
    word_count = len(text.split())       
    sentence_count = text.count('.') + text.count('!') + text.count('?')  
    return f"Characters: {char_count}\nWords: {word_count}\nSentences: {sentence_count}"
app = gr.Interface(
    fn=text_analyzer,                 
    inputs=gr.Textbox(lines=5, placeholder="Enter your text here..."),
    outputs="text",
    title="Text Analyzer App",
    description="Enter text and get character, word, and sentence counts instantly."
)
app.launch()
