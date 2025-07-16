
# MPLUM: Multi-objective Prompt Learning for English and Urdu Summarization

## Project Folder Structure

```
Datasets/
    task1290_xsum_summarization.json    
    task1357_xlsum_summary_generation.json
    urdu_xlsum.json
Kaggle_files/
    English/
        new-llama3-1-8b-instruct-English.ipynb
        new-llama3-1-8b-instruct-multi_good-English.ipynb
        new-ministral-8b-instruct-English.ipynb
        new-ministral-8b-instruct-multi_good-English.ipynb
        new-qwen-2-5-English.ipynb
        new-qwen-2-5-multi_good-English.ipynb
        new-qwen3-8b-instruct-English.ipynb
        new-qwen3-8b-instruct-multi_good-English.ipynb
    Urdu/
        new-bloomz7b-urdu-summarization.ipynb
        new-urdu-gemini-summarization.ipynb
        new-urdu-llama-3-1-summarization.ipynb
```

## Running Notebooks
- All notebooks are designed to be run on Kaggle. Upload the desired notebook from `Kaggle_files/English/` or `Kaggle_files/Urdu/` to your Kaggle account.

## Required Setup
1. **WandB Key**: Set up your own [Weights & Biases](https://wandb.ai/) account and add your API key in the notebook/code.
2. **API Keys & Tokens**:
    - Add your Hugging Face token.
    - Add any other required API keys (e.g., for model access).
3. **Initial Prompt**: The initial prompt needs to be taken by the user itself based on the scenario(Good to good, worst to good etc) they want. For multi good, the user has to generate different paraphrases equivalent to the population size and add them at required place. 
4. **Parameter Configuration**: Change the following parameters in the code:
    - Population size
    - Number of instances to be taken
    - Number of iterations
    - Number of operations
    - Patience criteria
    - WandB file names
5. **Kaggle Path**: Set up the correct Kaggle dataset path in the notebook/code.

**Note for English Dataset Selection:**
- To switch between XSum and XLSum datasets in English scripts, change the `task-idx` parameter:
    - `task-idx=0` for XSum
    - `task-idx=1` for XLSum

## Instructions
- Before running, ensure all required keys and tokens are set.
- Adjust parameters for your experiments as needed.
- Refer to comments in the code for locations to update prompts, keys, and parameters.

  Update the value in your script or notebook command as needed.

