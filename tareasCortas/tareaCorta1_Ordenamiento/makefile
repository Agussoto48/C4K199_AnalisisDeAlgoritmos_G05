VENV = .venv 
REQ = requirements.txt


setup:
	uv venv
	uv pip install -r $(REQ)

run:
	@uv run python ./main.py

clean:
	@rm -rf $(VENV)