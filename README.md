# MPLUM: Multi-objective Prompt Learning for English and Urdu Summarization

## Project Structure

```
MPLUM-Multi_objective_prompt_learning_for_English_and_Urdu_Summarization/
│
├── README.md
├── requirements.txt
├── Datasets/
│   ├── urdu__xlsum.json
│   ├── english_xlsum.json
│   └── english_xsum.json
├── src/
│   ├── english/
│   │   ├── xsum/
│   │   │   ├── llama3_good_to_good.py
│   │   │   ├── llama3_multi_good.py
│   │   │   ├── ministral_good_to_good.py
│   │   │   ├── ministral_multi_good.py
│   │   │   ├── qwen2_good_to_good.py
│   │   │   ├── qwen2_multi_good.py
│   │   │   ├── qwen3_good_to_good.py
│   │   │   ├── qwen3_multi_good.py
│   │   └── xlsum/
│   │       ├── llama3_good_to_good.py
│   │       ├── llama3_multi_good.py
│   │       ├── ministral_good_to_good.py
│   │       ├── ministral_multi_good.py
│   │       ├── qwen2_good_to_good.py
│   │       ├── qwen2_multi_good.py
│   │       ├── qwen3_good_to_good.py
│   │       ├── qwen3_multi_good.py
│   └── urdu/
│       └── xlsum/
│           ├── bloomz7b_good_to_good.py
│           ├── bloomz7b_worst_to_good.py
│           ├── gemini_good_to_good.py
│           ├── gemini_worst_to_good.py
│           ├── llama3_good_to_good.py
│           └── llama3_worst_to_good.py
```


## Important

**API Keys:**
This repository does not include any personal API keys for wandb, huggingface, or gemini. Please insert your own API keys in the relevant scripts before running. Look for comments like:

```python
# NOTE: Please insert your own API keys for wandb, huggingface, or gemini where required.
```

## Installation

Install all dependencies using:

```bash
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu124
```

## Usage

- Scripts are organized by language, dataset, model, and scenario.
- For English:
  - `task-idx=0` for XSum
  - `task-idx=1` for XLSum
- For Urdu:
  - Only XLSum (default)

Example run:

```bash
python src/english/xsum/llama3_good_to_good.py --task-idx 0 --population_size 50 --num_train 150
python src/urdu/xlsum/gemini_good_to_good.py --population_size 50 --num_train 150
```


## Contributing

Feel free to fork, open issues, and submit pull requests.

## License

MIT
# multi_objective_prompt_optimization