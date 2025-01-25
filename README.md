## Chatish
Chatish is a string of ideas that explore light webapps that can adequately prove the implications
of large language models in recurrent jobs as well as contextual retrieval for discreet and 
immediate relevance.

### How it works
Launch your terminal:

* Create a virtual environment `python3 -m venv <venv_name>`
* Install  requirements with `pip install -r requirements.txt`
* Run the application: `streamlit run app.py`

### Features:
- Deploy and Interact with Cohere API: Enter your Cohere API Key to start using the application.
- Upload Files for Additional Context: Choose files such as PDFs or CSVs to provide additional context for the language model.
- Conversation History: View and manage your conversation history to keep track of interactions.
- Generate Responses: Use the uploaded files to generate responses based on the provided context.

### Remember to:
- Retrieve your own API Key.
- Keep in mind that LLMs are prone to hallucinations.

### Future Improvements:
- Error Handling: Improve error handling for invalid API tokens and other potential issues.
- User Interface: Enhance the user interface for a more intuitive and user-friendly experience.
- Additional File Types: Support more file types for context, such as images and audio files.
- Advanced Features: Implement advanced features like sentiment analysis, summarization, and more.

Feel free to build upon this foundation and make it even better!

### Remember to:
Retrieve your own [API Key](https://dashboard.cohere.com/api-keys)
and that _LLMs are prone to hallucinations_

### Deployed web application
[Chatish UI](https://chatish.streamlit.app/)