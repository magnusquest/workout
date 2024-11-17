## Running the Project Locally

First install [uv](https://docs.astral.sh/uv/), the hyper modern Python package manager.

1. Create & Sync Astra UV environment: `uv init && uv sync`

2. Add necessary API keys to your environment using the export command:
    ```shell
    export API_KEY_NAME=your_api_key_value
    ```

4. Run the Streamlit application: `streamlit run main.py`

5. Navigate to [http://localhost:8501/](http://localhost:8501/) in your web browser.